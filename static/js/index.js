var chart;

function requestData() {
    $.ajax({
        url: '/live-data',
        success: function (point) {
            var series = chart.series[0],
                shift = series.data.length > 20;

            chart.series[0].setData(point[0], true, true, true);
            chart.series[1].setData(point[1], true, true, true);
            chart.series[2].setData(point[2], true, true, true);
            chart.series[3].setData(point[3], true, true, true);
            chart.series[4].setData(point[4], true, true, true);
            chart.series[5].setData(point[5], true, true, true);
            setTimeout(requestData, 1000);
        },
        cache: false
    });
}


$(document).ready(function () {
    chart = new Highcharts.Chart({
        chart: {
            renderTo: 'data-container',
            type: 'column',
            events: {
                load: requestData
            }
        },
        title: {
            text: 'GPU Servers'
        },
        xAxis: {
            title: {
                text: 'Server Name'
            },
            categories: [
                'NIPA',
                'VCGPU-1',
                'VCGPU-2',
                'VCGPU-3',
                'VCGPU-4',
            ],
        },
        yAxis: [{
            min: 0,
            max: 100,
            title: {
                text: 'Total'
            }
        }, {
            min: 0,
            max: 100,
            title: {
                text: 'Used'
            },
            opposite: true
        }],
        legend: {
            shadow: true
        },
        tooltip: {
            shared: false
        },
        plotOptions: {
            column: {
                grouping: false,
                shadow: false,
                borderWidth: 0
            },
        },
        series: [{
            name: 'GPU1 Total Memory',
            color: 'rgba(165,170,217,1)',
            data: [],
            tooltip: {
                valuePrefix: '',
                valueSuffix: '%'
            },
            pointPadding: 0.35,
            pointPlacement: -0.4
        }, {
            name: 'GPU1 Used Memory',
            color: 'rgba(126,86,134,.9)',
            data: [],
            tooltip: {
                valuePrefix: '',
                valueSuffix: '%'
            },
            pointPadding: 0.4,
            pointPlacement: -0.4,
            yAxis: 1
        }, {
            name: 'GPU2 Total Memory',
            color: 'rgba(248,161,63,1)',
            data: [],
            tooltip: {
                valuePrefix: '',
                valueSuffix: '%'
            },
            pointPadding: 0.35,
            pointPlacement: -0.05,
        }, {
            name: 'GPU2 Used Memory',
            color: 'rgba(186,60,61,.9)',
            data: [],
            tooltip: {
                valuePrefix: '',
                valueSuffix: '%'
            },
            pointPadding: 0.4,
            pointPlacement: -0.05,
            yAxis: 1
        }, {
            name: 'GPU3 Total Memory',
            color: 'rgba(11,245,113,.9)',
            data: [],
            tooltip: {
                valuePrefix: '',
                valueSuffix: '%'
            },
            pointPadding: 0.35,
            pointPlacement: 0.3,
        }, {
            name: 'GPU3 Used Memory',
            color: 'rgba(45,148,90,9)',
            data: [],
            tooltip: {
                valuePrefix: '',
                valueSuffix: '%'
            },
            pointPadding: 0.4,
            pointPlacement: 0.3,
            yAxis: 1

        }],
    });
});
