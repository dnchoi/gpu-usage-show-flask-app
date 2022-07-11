import json
from time import time
from flask import Flask, render_template, make_response
from gpu_check import get_gpus_info
import threading

gpus = get_gpus_info()
t1 = threading.Thread(target=gpus.function, args=(["nipa_luke", "vcgpu", "vcgpu2", "vcgpu3", "vcgpu5"],))
t1.daemon = True
t1.start()

previous_data = []
app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/live-data")
def live_data():
    global gpus, previous_data
    nipa = gpus._return[:6]
    vcgpu1 = gpus._return[6:12]
    vcgpu2 = gpus._return[12:18]
    vcgpu3 = gpus._return[18:24]
    vcgpu4 = gpus._return[24:30]

    gpus._return = []

    real_data = []

    if len(nipa) > 0:
        T_gpu1 = [nipa[0], vcgpu1[0], vcgpu2[0], vcgpu3[0], vcgpu4[0]]
        U_gpu1 = [nipa[1], vcgpu1[1], vcgpu2[1], vcgpu3[1], vcgpu4[1]]
        T_gpu2 = [nipa[2], vcgpu1[2], vcgpu2[2], vcgpu3[2], vcgpu4[2]]
        U_gpu2 = [nipa[3], vcgpu1[3], vcgpu2[3], vcgpu3[3], vcgpu4[3]]
        T_gpu3 = [nipa[4], vcgpu1[4], vcgpu2[4], vcgpu3[4], vcgpu4[4]]
        U_gpu3 = [nipa[5], vcgpu1[5], vcgpu2[5], vcgpu3[5], vcgpu4[5]]
        data = []
        data.append(T_gpu1)
        data.append(U_gpu1)
        data.append(T_gpu2)
        data.append(U_gpu2)
        data.append(T_gpu3)
        data.append(U_gpu3)
        print(
            "GPU1 T : {}\nGPU1 U : {}\nGPU2 T : {}\nGPU2 U : {}\nGPU3 T : {}\nGPU3 U : {}\n".format(
                data[0], data[1], data[2], data[3], data[4], data[5]
            )
        )
        previous_data = data
        real_data = data
    else:
        real_data = previous_data
    response = make_response(json.dumps(real_data))
    response.content_type = "application/json"
    return response


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5555)
