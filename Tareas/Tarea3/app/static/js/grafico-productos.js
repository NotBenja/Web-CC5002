Highcharts.chart('container', {
  chart: {
      type: 'bar',
      backgroundColor: '#f4f4f4',
      borderRadius: 15,
      plotBackgroundColor: '#ffffff',
      plotBorderWidth: 1,
  },
  title: {
      text: 'Cantidad de productos por Fruta y Verdura',
      style: {
          color: '#333333',
          fontSize: '20px'
      }
  },
  xAxis: {
      categories: ['Fruta', 'Verdura'],
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
      name: 'Cantidad de productos',
      data: [],
      color: '#7cb5ec'
  }]
});

fetch("http://localhost:5000/get-datos-productos")
  .then((response) => response.json())
  .then((data) => {
    // Get the chart by ID
    const chart = Highcharts.charts.find(
      (chart) => chart && chart.renderTo.id === "container"
    );

    // Update the chart with new data
    chart.update({
      series: [
        {
          data: data,
        },
      ],
    });
  })
  .catch((error) => console.error("Error:", error));