$(document).ready(function() {

    $('#detailbutton').click(function(){
        var data_type = $("#data_type").val();
        if (data_type == 1){
            var action_url = "/charts/continent_detail/";
        }
        else
        {
            var action_url = "/charts/country_detail/";
        }
        var id = $("#data_v1").val();
        var id2 = $("#data_v2").val();
        var xtick = $("#data_v1 option:selected").text()
        var ytick = $("#data_v2 option:selected").text()
        var gtype = $("#graphtype").val();
        console.log(gtype);
        $.blockUI("Please wait ...")
        $.ajax(
        {
            url: action_url+id+"/"+id2,
            error: function () {
                alert("Invalid Option");
                $.unblockUI();
            },

            success: function (data) {
                console.log(data);
                  var country = [];
                  var fields = [];
                  var legend_names = []
                  for (var i=0; i < data[0].length;i++)
                  {
                    country.push(data[0][i]);
                    fields.push(data[1][i]);
                    legend_names.push(data[2][i]);
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
                      text : legend_names,
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
                      mode : "markers",
                      text : legend_names,
                      type: graph_type
                    };

                    var layout = {
                      xaxis: {title: xtick},
                      yaxis: {title: ytick},
                      margin: {t: 20},
                    };
                    var data = [trace1];
                    Plotly.newPlot('myDiv', data,layout);
                    $.unblockUI();
                }
            },
            error: function(){
                swal({
                title: "Error!",
                text: "Oops! Something went wrong.",
                type: "error",
                confirmButtonText: "Cool" });
            },
            type: 'GET'
        }
    );
    });
});