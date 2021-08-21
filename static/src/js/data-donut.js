 
// Create chart instance
var chart = am4core.create("chartdiv", am4charts.PieChart);

// Add data
chart.data = [{
  "country": "Suaka Alam dan Pelestarian Alam",
  "value": 1620000
}, {
  "country": "Kawasan Hutan Lindung",
  "value": 2310000
}, {
  "country": "Kawasan Hutan Produksi Terbatas",
  "value": 2130000
}, {
  "country": "Kawasan Hutan Produksi",
  "value": 2130000
}, {
  "country": "Kawasan Hutan Produksi Konversi",
  "value": 197920
}];

// Add and configure Series
var pieSeries = chart.series.push(new am4charts.PieSeries());
pieSeries.dataFields.value = "value";
pieSeries.dataFields.category = "country";
pieSeries.labels.template.disabled = true;
pieSeries.ticks.template.disabled = false;

chart.legend = new am4charts.Legend();
chart.legend.position = "left"; 

chart.innerRadius = am4core.percent(60);

var label = pieSeries.createChild(am4core.Label);
label.text = "{values.value.sum} ha";
label.horizontalCenter = "middle";
label.verticalCenter = "middle";
label.fontSize = 20; 