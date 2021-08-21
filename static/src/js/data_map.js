
var data = [
    ['id-3700', 0,"#bfbfbf"],
    ['id-ac', 1,"#bfbfbf"],
    ['id-jt', 2,"#bfbfbf"],
    ['id-be', 3,"#bfbfbf"],
    ['id-bt', 4,"#bfbfbf"],
    ['id-kb', 5,"#bfbfbf"],
    ['id-bb', 6,"#bfbfbf"],
    ['id-ba', 7,"#bfbfbf"],
    ['id-ji', 8,"#bfbfbf"],
    ['id-ks', 9,"#bfbfbf"],
    ['id-nt', 10,"#bfbfbf"],
    ['id-se', 11,"#bfbfbf"],
    ['id-kr', 12,"#bfbfbf"],
    ['id-ib', 13,"#bfbfbf"],
    ['id-su', 14,"#bfbfbf"],
    ['id-ri', 15,"#bfbfbf"],
    ['id-sw', 16,"#bfbfbf"],
    ['id-ku', 17,"#bfbfbf"],
    ['id-la', 18,"#bfbfbf"],
    ['id-sb', 19,"#bfbfbf"],
    ['id-ma', 20,"#bfbfbf"],
    ['id-nb', 21,"#bfbfbf"],
    ['id-sg', 22,"#bfbfbf"],
    ['id-st', 23,"#bfbfbf"],
    ['id-pa', 24,"#bfbfbf"],
    ['id-jr', 25,"#bfbfbf"],
    ['id-ki', 26,"#bfbfbf"],
    ['id-1024', 27,"#bfbfbf"],
    ['id-jk', 28,"#bfbfbf"],
    ['id-go', 29,"#bfbfbf"],
    ['id-yo', 30,"#bfbfbf"],
    ['id-sl', 31,"#bfbfbf"],
    ['id-sr', 32,"#bfbfbf"],
    ['id-ja', 33,"#bfbfbf"],
    ['id-kt', 34,"#757575"]
];

// Create the chart
Highcharts.mapChart('container_map', {
    chart: {
        map: 'countries/id/id-all',
        height: 500
    },

    title: {
        text: ''
    },

    subtitle: {
        text: ''
    }, 
    legend: {
        enabled: false
    },   

    mapNavigation: {
        enabled: true,
        buttonOptions: {
            verticalAlign: 'bottom'
        }
    },

    colorAxis: {
        min: 0
    },


    series: [{
        name: 'Country',
        data: data,
        keys: ['hc-key','value', 'color'],
        dataLabels: {
            enabled: true,
            color: '#757575',
            states: {
                hover: {
                    color: '#BADA55'
                }
            },
            formatter: function () {
                if (this.point.value) {
                    return this.point.name ;
                }
            }
        },
        tooltip: {
            headerFormat: '',
            pointFormat: '{point.name}</br> Data Tanah : 123123 </br> Data Penduduk : 9120'
        }
    }],
       plotOptions:{
        series:{
            point:{
                events:{
                    click: function(){
                        $(".prov_txt").text(this.name);
                    }
                }
            }
        }
    }
});


// $('#dropdownYear').each(function() {
//   var year = (new Date()).getFullYear();
//   var current = year;
//   for (var i = 0; i < 6; i++) {
//     year = current - i;
//     if ((year) == current)
//       $(this).append('<option selected value="' + (year) + '">' + (year) + '</option>');
//     else
//       $(this).append('<option value="' + (year) + '">' + (year) + '</option>');
//   }

// }) 



 