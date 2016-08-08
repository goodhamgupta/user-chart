$(document).ready(function() {

    $('#showbutton').click(function(){
        var id = $("#data").val();
        var gtype = $("#graphtype").val();
        console.log(gtype);
        $.blockUI("Please wait ...")
        $.ajax(
        {
            url: '/charts/data/'+id,
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
                  var graph_type;
                  if (gtype == 1)
                  {
                    graph_type="bar";
                  }
                  else if (gtype == 2)
                  {
                    graph_type="scatter";
                  }
                  else
                  {
                    graph_type="pie";
                  }
                  console.log(graph_type);
                if (graph_type == "pie"){
                    var trace1 = {
                      labels: country,
                      values: fields,
                      type: graph_type
                    };
                    var data = [trace1];
                    Plotly.newPlot('myDiv', data);
                    $.unblockUI();
                }
                else{
                  var trace1 = {
                      x: country,
                      y: fields,
                      type: graph_type
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
    });
});