<template>
    <div>
      <div ref="chart" style="width: 100%; height: 400px;"></div>
    </div>
  </template>
  <script>
  import * as echarts from "echarts";
  export default {
    props: {
      labels: Array,
      data: Array,
    },
    mounted() {
      this.renderChart();
    },
    methods: {
      renderChart() {
        const filteredLabels = [];
        const filteredData = [];
        this.labels.forEach((label, index) => {
          if (!label.includes("姓名")) {
            filteredLabels.push(label);
            filteredData.push(this.data[index]);
          }
        });
  
        const chart = echarts.init(this.$refs.chart);
        const option = {
          xAxis: {
            type: "category",
            data: filteredLabels,
          },
          yAxis: {
            type: "value",
          },
          series: [
            {
              data: filteredData,
              type: "line",
              label: {
                show: true,
                position: "top",
              },
            },
          ],
        };
        chart.setOption(option);
        console.log("Filtered Labels:", filteredLabels);
        console.log("Filtered Data:", filteredData);
      },
    },
  };
  </script>
  