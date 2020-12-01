var contenido = document.querySelector('#contenido')
var list_content = document.querySelector('#list-content');
var data_table = document.querySelector('#data-table');
var p_return = document.querySelector('#return')
var requestOptions = {
    method: 'GET',
    redirect: 'follow'
};
function list_price() {
    fetch('http://127.0.0.1:5000/List_price' , requestOptions)
    .then(function(response) {
        return response.json();
    })
    .then(function(myJson) {
    for(let i of myJson){
        console.log(i)
        list_content.innerHTML += `<div class="item">
                                      <p>${i.AAPL}<br>${i.Data2}</p>
                                      <p>${i.Price}<br>${i.data1}</p>
                                    </div>`;
    }
});
} 

fetch('http://127.0.0.1:5000/List_price' , requestOptions)
    .then(function(response) {
        return response.json();
    })
    .then(function(myJson) {
    for(let i of myJson){
        console.log(i)
        list_content.innerHTML += `<div class="item">
                                        <p>${i.AAPL}<br>${i.Data2}</p>
                                        <p>${i.Price}<br>${i.data1}</p>
                                    </div>`;
    }
});

var day_data = [
    {"period": "2012-08-01", "licensed": -200, "sorned": 660},
    {"period": "2012-09-01", "licensed": -100, "sorned": 629},
    {"period": "2012-10-01", "licensed": 0, "sorned": 618},
    {"period": "2012-11-01", "licensed": 89, "sorned": 661},
    {"period": "2012-12-01", "licensed": 200, "sorned": 667},
    {"period": "2013-01-01", "licensed": 2000, "sorned": 627},
    {"period": "2013-02-01", "licensed": 2500, "sorned": 660},
    {"period": "2013-03-01", "licensed": 3000, "sorned": 676},
    {"period": "2013-04-01", "licensed": 3168, "sorned": 656},
    {"period": "2013-06-01", "licensed": 3295, "sorned": 622},
    {"period": "2013-07-01", "licensed": 3415, "sorned": 622},
    {"period": "2013-08-01", "licensed": 3500, "sorned": 622}
];

new Morris.Line({
    // ID of the element in which to draw the chart.
    element: 'myfirstchart',
    // Chart data records -- each entry in this array corresponds to a point on
    // the chart.
    data: day_data,
    // The name of the data record attribute that contains x-values.
    xkey: 'period',
    ykeys: ['licensed', 'sorned'],
    labels: ['Licensed', 'SORN'],
    resize: true
  });

new Morris.Bar({
    // ID of the element in which to draw the chart.
    element: 'graph-bar',
    // Chart data records -- each entry in this array corresponds to a point on
    // the chart.
    data: day_data,
    // The name of the data record attribute that contains x-values.
    xkey: 'period',
    ykeys: ['licensed', 'sorned'],
    labels: ['Licensed', 'SORN'],
    resize: true
  });

  new Morris.Line({
    // ID of the element in which to draw the chart.
    element: 'graph1-line',
    // Chart data records -- each entry in this array corresponds to a point on
    // the chart.
    data: day_data,
    // The name of the data record attribute that contains x-values.
    xkey: 'period',
    ykeys: ['licensed', 'sorned'],
    labels: ['Licensed', 'SORN'],
    resize: true
  });