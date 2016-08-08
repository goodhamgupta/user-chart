$(document).ready(function() {

    $('#showbutton').click(function(){
    console.log("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&");
    var id = $("#data").val();
    var gtype = $("#graphtype").val();
    $.blockUI("Please wait ...")
            $.ajax(
                {
                    url: '/data/'+id+"/",
                    error: function () {
                        alert("Invalid Option");
                        $.unblockUI();
                    },

                    success: function (data) {
                        console.log(data);
                          var country = [];
                          var fields = [];
                          for (var i=0; i < data[0].length;i++)
                          {
                            country.push(data[0][i]);
                            fields.push(data[1][i]);
                          }
                          switch (gtype){
                            case 1:
                                gtype="bar";
                                break;
                            case 2:
                                gtype="scatter";
                                break;
                            case 3:
                                gtype="pie";
                                break;
                            default:
                                gtype="bar"
                          }
                        if (gtype == "pie"){
                            var trace1 = {
                              labels: country,
                              values: fields,
                              type: gtype
                            };
                            var data = [trace1];
                            Plotly.newPlot('myDiv', data);
                            $.unblockUI();
                        }
                        else{
                          var trace1 = {
                              x: country,
                              y: fields,
                              type: gtype
                            };

                            var layout = {
                              xaxis: {title: 'Countries'},
                              margin: {t: 20},
                            };
                            var data = [trace1];
                            Plotly.newPlot('myDiv', data,layout);
                            $.unblockUI();
                        }
                    },

                    type: 'GET'
                }
            );
    }
}