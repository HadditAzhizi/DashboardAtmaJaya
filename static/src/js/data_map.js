
odoo.define('dashboard_web.templates', function (require) {
"use strict"; 
    var ajax = require('web.ajax'); 
    var url = window.location.pathname;

    function my_implode_js(separator,array){
       var temp = '';
       for(var i=0;i<array.length;i++){
           temp +=  array[i] 
           if(i!=array.length-1){
                temp += separator  ; 
           }
       }//end of the for loop

       return temp;
    }//end of the function

    if(url=="/dashboard" || url=="/id/dashboard")
    {
            var peta_prov = 11;
            get_config();
            get_data(peta_prov,"");
            $.ajax({ 
             url: "/get_map",                 
             success: function(result){
                    var data = [['id-ac', '#F2F2F0', '11'], ['id-su', '#F2F2F0', '12'], ['id-sb', '#F2F2F0', '13'], ['id-ri', '#F2F2F0', '14'], ['id-ja', '#F2F2F0', '15'], ['id-sl', '#F2F2F0', '16'], ['id-be', '#F2F2F0', '17'], ['id-1024', '#F2F2F0', '18'], ['id-bb', '#F2F2F0', '19'], ['id-kr', '#F2F2F0', '21'], ['id-jk', '#F2F2F0', '31'], ['id-jr', '#F2F2F0', '32'], ['id-jt', '#F2F2F0', '33'], ['id-yo', '#F2F2F0', '34'], ['id-ji', '#F2F2F0', '35'], ['id-bt', '#F2F2F0', '36'], ['id-ba', '#F2F2F0', '51'], ['id-nb', '#F2F2F0', '52'], ['id-nt', '#F2F2F0', '53'], ['id-kb', '#F2F2F0', '61'], ['id-kt', '#F2F2F0', '62'], ['id-ks', '#F2F2F0', '63'], ['id-ki', '#F2F2F0', '64'], ['id-ku', '#F2F2F0', '65'], ['id-sw', '#F2F2F0', '71'], ['id-st', '#F2F2F0', '72'], ['id-se', '#F2F2F0', '73'], ['id-sg', '#F2F2F0', '74'], ['id-go', '#F2F2F0', '75'], ['id-sr', '#F2F2F0', '76'], ['id-ma', '#F2F2F0', '81'], ['id-la', '#F2F2F0', '82'], ['id-ib', '#F2F2F0', '91'], ['id-pa', '#F2F2F0', '94']]
                    Highcharts.mapChart('container_map', {
                        chart: {
                            map: 'countries/id/id-all',
                            height: 600,
                            events:{
                                load: function(e){
                                   this.mapZoom(0.3,4591,-8000);
                                }
                            }
                        },

                        title: {
                            text: ''
                        }, 
                        mapNavigation: {
                            enabled: true,
                            buttonOptions: {
                                verticalAlign: 'bottom'
                            }
                        },
                        series: [{
                            data: data,
                            name: 'Provinsi',
                            keys: ['hc-key','color','id_prov'],
                           allowPointSelect: true,
                           cursor: 'pointer',
                            states: {
                                hover: {
                                    color: '#4f4f4f'
                                },
                                select: {
                                  color: '#4f4f4f',
                                  borderColor: '#363434',
                                  dashStyle: 'solid'
                                }
                            },
                            dataLabels: {
                                enabled: true,
                                format: '{point.name}'
                            }
                        }],
                       plotOptions:{
                        series:{
                            point:{
                                events:{
                                    click: function(){
                                        $(".prov_txt").text(this.name);
                                        $("#tmp_nilai").html("")
                                        peta_prov = this.id_prov;
                                         var id_jenis = $('.head_conf input:checked').map(function () {
                                              return this.value;
                                          }).get();
                                         get_data(peta_prov,id_jenis);
                                    }
                                }
                            }
                        }
                    }
                });  
            },
        });  


        function get_config()
        { 
            $.ajax({ 
             url: "/get_config",
             dataType: 'json',
             success: function(result){
                $.each(result,function(k,v){
                        var html = '<div class="col-md-12"><label class="switch_input mt-1"><input type="checkbox" id="jen'+v['id_jenis']+'" value="'+v['id_jenis']+'" checked="true" class="oncheck_config"/><span class="slider_input round"></span></label><span class="ml-1 title_conf"> '+v['jenis_survey']+' </span></div>';
                        $(".head_conf").append(html);
                    }); 

                    $('.oncheck_config').click(function(){
                        var val = $(this).val();
                        if($(this).is(":checked")){
                            get_data(peta_prov,val);     
                        }
                        else if($(this).is(":not(:checked)")){
                            $("#tmpjen"+val).remove("");
                        }
                    });
                },
            });
        } 

        function get_data(id_prov,id_jenis)
        {  
            $.ajax({ 
             url: '/post_data',
             data: {'id_prov': id_prov, 'id_jenis': '"'+id_jenis+'"'},
             type: "POST",
             dataType: 'json',
             success: function(result){
                    console.log(result);
                    $.each(result,function(k,v){
                        var html = '<div class="col-md-6 p-3 box" id="tmpjen'+v["id_jenis"]+'" style="background-color:white;border-radius: 15px;"><center><h6 style="font-size: 12px;">'+v["jenis"]+'</h6><h3><b>'+v["persentase"]+'%</b></h3><h6 style="font-size: 12px;">'+v["isi"]+'</h6></center></div>'
                        $("#tmp_nilai").append(html);
                    }); 
                },
            });
        } 
    }
 });

