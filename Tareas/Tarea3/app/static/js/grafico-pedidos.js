Highcharts.chart('container', {
    chart: {
        type: 'bar',
        backgroundColor: '#f4f4f4',
        borderRadius: 15,
        plotBackgroundColor: '#ffffff',
        plotBorderWidth: 1,
    },
    title: {
        text: 'Cantidad de pedidos por comuna',
        style: {
            color: '#333333',
            fontSize: '20px'
        }
    },
    xAxis: {
        categories: [],
        labels: {
            style: {
                color: '#333333',
                fontSize: '12px'
            }
        }
    },
    yAxis: {
        title: {
            text: 'Total',
            style: {
                color: '#333333',
                fontSize: '16px'
            }
        },
        labels: {
            style: {
                color: '#333333',
                fontSize: '12px'
            }
        }
    },
    series: [{
        name: 'Cantidad de pedidos',
        data: [],
        color: '#7cb5ec'
    }]
});

fetch("http://localhost:5000/get-datos-pedidos")
  .then((response) => response.json())
  .then((data) => {
    // Extraemos las comunas y cantidades de los datos
    const comunas = Object.keys(data);
    const cantidades = Object.values(data);
    // Get the chart by ID
    const chart = Highcharts.charts.find(
      (chart) => chart && chart.renderTo.id === "container"
    );

    // Update the chart with new data
    chart.update({
      xAxis: {
        categories: comunas 
        },  
      series: [
        {
          data: cantidades,
        },
      ],
    });
  })
  .catch((error) => console.error("Error:", error));