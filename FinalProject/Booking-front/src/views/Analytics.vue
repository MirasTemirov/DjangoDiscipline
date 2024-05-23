<template>
  <div>
    <h2 class="text-center mb-4">Аналитика</h2>
    <v-row>
      <v-col cols="6">
        <v-card>
          <v-card-text>
            <highcharts :options="chartOptions.group"></highcharts>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="6">
        <v-card>
          <v-card-text>
            <highcharts :options="chartOptions.object"></highcharts>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="6">
        <v-card>
          <v-card-text>
            <highcharts :options="chartOptions1.group"></highcharts>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="6">
        <v-card>
          <v-card-text>
            <highcharts :options="chartOptions1.object"></highcharts>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="6">
        <v-card>
          <v-card-text>
            <highcharts :options="chartOptions2.group"></highcharts>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="6">
        <v-card>
          <v-card-text>
            <highcharts :options="chartOptions2.object"></highcharts>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import Highcharts from "highcharts";
import { Chart } from "highcharts-vue";

Highcharts.setOptions({
  global: {
    timezone: "Asia/Almaty",
  },
  lang: {
    loading: "Загрузка...",
    months: [
      "Январь",
      "Февраль",
      "Март",
      "Апрель",
      "Май",
      "Июнь",
      "Июль",
      "Август",
      "Сентябрь",
      "Октябрь",
      "Ноябрь",
      "Декабрь",
    ],
    shortMonths: [
      "Янв",
      "Фев",
      "Март",
      "Апр",
      "Май",
      "Июнь",
      "Июль",
      "Авг",
      "Сент",
      "Окт",
      "Нояб",
      "Дек",
    ],
    weekdays: [
      "Воскресенье",
      "Понедельник",
      "Вторник",
      "Среда",
      "Четверг",
      "Пятница",
      "Суббота",
    ],
    shortWeekdays: ["Вс", "Пн", "Вт", "Ср", "Чт", "Пт", "Сб"],
  },
});

export default {
  name: "Analytics",
  components: {
    highcharts: Chart,
  },
  data() {
    return {
      chartOptions: {
        group: {
          colors: [
            "#2f7ed8",
            "#0d233a",
            "#8bbc21",
            "#910000",
            "#1aadce",
            "#492970",
            "#f28f43",
            "#77a1e5",
            "#c42525",
            "#a6c96a",
          ],
          chart: {
            type: "spline",
          },
          credits: {
            enabled: false,
          },
          title: {
            text: "Группы",
          },
          subtitle: {
            text: "Аналитика по дням",
          },
          yAxis: {
            title: {
              text: null,
            },
          },
          xAxis: {
            type: "datetime",
            min: null,
            max: null,
          },
          legend: {
            layout: "horizontal",
          },
          series: [],
        },
        object: {
          chart: {
            type: "spline",
          },
          credits: {
            enabled: false,
          },
          title: {
            text: "Объекты",
          },
          subtitle: {
            text: "Аналитика по дням",
          },
          yAxis: {
            title: {
              text: null,
            },
          },
          xAxis: {
            type: "datetime",
            min: null,
            max: null,
          },
          legend: {
            layout: "horizontal",
          },
          series: [],
        },
      },
      chartOptions1: {
        object: {
          credits: {
            enabled: false,
          },
          chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false,
            type: "pie",
          },
          title: {
            text: "Объекты",
          },
          subtitle: {
            text: "Аналитика по количеству",
          },
          tooltip: {
            pointFormat: "<b>{point.percentage:.1f}% - {point.y}</b>",
          },
          accessibility: {
            point: {
              valueSuffix: "%",
            },
          },
          plotOptions: {
            pie: {
              allowPointSelect: true,
              cursor: "pointer",
              dataLabels: {
                enabled: false,
              },
              showInLegend: true,
            },
          },
          series: [],
        },
        group: {
          colors: [
            "#2f7ed8",
            "#0d233a",
            "#8bbc21",
            "#910000",
            "#1aadce",
            "#492970",
            "#f28f43",
            "#77a1e5",
            "#c42525",
            "#a6c96a",
          ],
          credits: {
            enabled: false,
          },
          chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false,
            type: "pie",
          },
          title: {
            text: "Группы",
          },
          subtitle: {
            text: "Аналитика по количеству",
          },
          tooltip: {
            pointFormat: "<b>{point.percentage:.1f}% - {point.y}</b>",
          },
          accessibility: {
            point: {
              valueSuffix: "%",
            },
          },
          plotOptions: {
            pie: {
              allowPointSelect: true,
              cursor: "pointer",
              dataLabels: {
                enabled: false,
              },
              showInLegend: true,
            },
          },
          series: [],
        },
      },
      chartOptions2: {
        group: {
          colors: [
            "#2f7ed8",
            "#0d233a",
            "#8bbc21",
            "#910000",
            "#1aadce",
            "#492970",
            "#f28f43",
            "#77a1e5",
            "#c42525",
            "#a6c96a",
          ],
          credits: {
            enabled: false,
          },
          chart: {
            type: "column",
          },
          title: {
            text: "Группы",
          },
          subtitle: {
            text: "Аналитика по месяцам",
          },
          xAxis: {
            categories: [],
            crosshair: true,
          },
          yAxis: {
            min: 0,
            title: {
              text: null,
            },
          },
          tooltip: {
            headerFormat:
              '<span style="font-size:10px">{point.key}</span><table>',
            pointFormat:
              '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
              '<td style="padding:0"><b>{point.y}</b></td></tr>',
            footerFormat: "</table>",
            shared: true,
            useHTML: true,
          },
          plotOptions: {
            column: {
              pointPadding: 0.2,
              borderWidth: 0,
            },
          },
          series: [],
        },
        object: {
          credits: {
            enabled: false,
          },
          chart: {
            type: "column",
          },
          title: {
            text: "Объекты",
          },
          subtitle: {
            text: "Аналитика по месяцам",
          },
          xAxis: {
            categories: [],
            crosshair: true,
          },
          yAxis: {
            min: 0,
            title: {
              text: null,
            },
          },
          tooltip: {
            headerFormat:
              '<span style="font-size:10px">{point.key}</span><table>',
            pointFormat:
              '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
              '<td style="padding:0"><b>{point.y}</b></td></tr>',
            footerFormat: "</table>",
            shared: true,
            useHTML: true,
          },
          plotOptions: {
            column: {
              pointPadding: 0.2,
              borderWidth: 0,
            },
          },
          series: [],
        },
      },
    };
  },
  methods: {
    loadData() {
      // load group analytics
      const loader = this.$loading.show(this.$loadingParams);
      this.$restApi
        .get(`handbook/group/analytics`)
        .then((response) => {
          if (response.status === 200) {
            // fill spline chart
            this.chartOptions.group.xAxis.max = Date.parse(
              response.data.spline.max
            );
            this.chartOptions.group.xAxis.min = Date.parse(
              response.data.spline.min
            );
            this.chartOptions.group.series = response.data.spline.series;

            // fix series
            for (let i = 0; i < this.chartOptions.group.series.length; i++) {
              this.chartOptions.group.series[i].marker = {
                symbol: "circle",
              };
              for (
                let j = 0;
                j < this.chartOptions.group.series[i].data.length;
                j++
              ) {
                this.chartOptions.group.series[i].data[j][0] = Date.parse(
                  this.chartOptions.group.series[i].data[j][0]
                );
              }

              // fill pie chart
              this.chartOptions1.group.series = response.data.pie.series;

              // fill column chart
              this.chartOptions2.group.series = response.data.column.series;
              this.chartOptions2.group.xAxis.categories =
                response.data.column.categories;
            }
          }
          loader.hide();
        })
        .catch((error) => {
          console.log(error);
          loader.hide();
        });

      // load object analytics
      this.$restApi
        .get(`handbook/object/analytics`)
        .then((response) => {
          if (response.status === 200) {
            // fill spline chart
            this.chartOptions.object.xAxis.max = Date.parse(
              response.data.spline.max
            );
            this.chartOptions.object.xAxis.min = Date.parse(
              response.data.spline.min
            );
            this.chartOptions.object.series = response.data.spline.series;

            // fix series
            for (let i = 0; i < this.chartOptions.object.series.length; i++) {
              this.chartOptions.object.series[i].marker = {
                symbol: "circle",
              };
              for (
                let j = 0;
                j < this.chartOptions.object.series[i].data.length;
                j++
              ) {
                this.chartOptions.object.series[i].data[j][0] = Date.parse(
                  this.chartOptions.object.series[i].data[j][0]
                );
              }

              // fill pie chart
              this.chartOptions1.object.series = response.data.pie.series;

              // fill column chart
              this.chartOptions2.object.series = response.data.column.series;
              this.chartOptions2.object.xAxis.categories =
                response.data.column.categories;
            }
          }
          loader.hide();
        })
        .catch((error) => {
          console.log(error);
          loader.hide();
        });
    },
  },
  mounted() {
    this.loadData();
  },
};
</script>

<style scoped></style>
