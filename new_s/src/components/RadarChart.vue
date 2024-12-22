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
        for (let i = 0; i < this.labels.length; i++) {
          if (this.labels[i].includes("姓名") === false) {
            filteredLabels.push(this.labels[i]);
            filteredData.push(this.data[i]);
          }
        }
        const chart = echarts.init(this.$refs.chart);
        const option = {
          radar: {
            indicator: filteredLabels.map((label) => ({
              name: label,
              max: 100,
            })),
          },
          series: [
            {
              type: "radar",
              data: [
                {
                  value: filteredData,
                  name: "数据",
                  label:{
                    show:true,
                    overflow:'none'
                  }
                },
              ],
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
  