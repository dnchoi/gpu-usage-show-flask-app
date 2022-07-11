import subprocess


class get_gpus_info:
    def __init__(self):
        self.key = ["index", "uuid", "name", "timestamp", "memory.total", "memory.free", "memory.used"]
        self.use_key = ["memory.total", "memory.used"]
        self._return = []

    def get_gpu_info(self, server, nvidia_smi_path="nvidia-smi", no_units=True):
        nu_opt = "" if not no_units else ",nounits"
        cmd = "ssh %s '%s --query-gpu=%s --format=csv,noheader%s'" % (
            server,
            nvidia_smi_path,
            ",".join(self.key),
            nu_opt,
        )
        output = subprocess.check_output(cmd, shell=True)
        lines = output.decode().split("\n")
        lines = [line.strip() for line in lines if line.strip() != ""]
        return [{k: v for k, v in zip(self.key, line.split(", "))} for line in lines]

    def function(self, server):
        while True:
            tmp = []
            for i in server:
                out = self.get_gpu_info(i)
                for j in out:
                    rate = 1
                    for q in self.key:
                        if q == self.use_key[0]:
                            rate = int(j[q])
                            tmp.append(int(j[q]) / rate * 100)
                        if q == self.use_key[1]:
                            tmp.append(int(j[q]) / rate * 100)
                if len(out) == 2:
                    tmp.append(100)
                    tmp.append(0)
                if len(out) == 1:
                    tmp.append(100)
                    tmp.append(0)
                    tmp.append(100)
                    tmp.append(0)
            self._return = tmp
