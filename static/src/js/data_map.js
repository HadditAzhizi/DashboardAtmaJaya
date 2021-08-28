
odoo.define('dashboard_web.templates', function (require) {
"use strict"; 
    var ajax = require('web.ajax'); 
    var url = window.location.pathname;
    if(url=="/dashboard" || url=="/id/dashboard")
    {
            var peta_prov = 11;
            $.ajax({ 
             url: "/get_map",                 
             success: function(result){

                    var data = [result];
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
                                    if (this.point.color) {
                                        return this.point.color ;
                                    }
                                }
                            },
                            tooltip: {
                                headerFormat: '',
                                pointFormat: '{point.value}'
                            }
                        }],
                           plotOptions:{
                            series:{
                                point:{
                                    events:{
                                        click: function(){
                                            $(".prov_txt").text(this.name);
                                            peta_prov = this.id;
                                            get_data(peta_prov,"");
                                        }
                                    }
                                }
                            }
                        }
                    });  
                },
            });

        get_data(peta_prov,"");

        $('.oncheck_config').click(function(){
            var val = $(this).val();
            if($(this).is(":checked")){
                get_data(peta_prov,val);     
            }
            else if($(this).is(":not(:checked)")){
                $("#tmpjen"+val).remove("");
            }
        });

        function get_data(id_prov,id_jenis)
        { 
            url = ""
            if(id_jenis=="" || id_jenis < 6)
            {
                url = "/get_sumber_air";
            }
            else if(id_jenis==6)
            {
                url = "/get_bb_utama";
            }
            else if(id_jenis==7)
            {
                url = "/get_bb_cadangan";
            }
            else if(id_jenis==8)
            {
                url = "/get_pemilahan_sampah";
            }
            else if(id_jenis==9)
            {
                url = "/get_perlakuan_sb3";
            }
            else if(id_jenis==10)
            {
                url = "/get_perlakuan_uts";
            }
            else if(id_jenis==11)
            {
                url = "/get_sumber_pu";
            }
            
            $.ajax({ 
             url: url,
             data: {'id_prov': id_prov, 'id_jenis': id_jenis},
             dataType: 'json',
             success: function(result){
                    $.each(result,function(k,v){
                        var html = '<div class="col-md-6 p-4 box" id="tmpjen'+v["id_jenis"]+'" style="background-color:white;border-radius: 15px;"><center><h6 style="font-size: 14px;">'+v["jenis"]+'</h6><h2><b>'+v["persentase"]+'%</b></h2><h6 style="font-size: 14px;">'+v["kategori"]+'</h6></center></div>'
                        $("#tmp_nilai").append(html)
                    }); 
                },
            });
        } 
    }
 });

