# School Donations Dashboard - Stream 2 - Back End Development

School Donations Dashboard is my Stream 2 project for my full stack web developer training with the [Code Institute](https://www.codeinstitute.net/). 

## Deployment 

See deployment at [https://frozen-tor-74902.herokuapp.com/](https://frozen-tor-74902.herokuapp.com/)

## About 

School Donations Dashboard is based on data from [DonorChoose.org](https://www.donorschoose.org/), a US based non-profit organisation which allows people donate money to public school classroom projects.

We were given the starting code for the project, and then instructed to redesign the presentation layer of the dashboard and add additional functionality.

## Technologies

The application was built using the following technologies:

- Mongo DB: NoSQL Database used to store and present the data in JSON format.
- Flask: A Python based  micro – framework  used to serve the data from the server to the web based interface.
- D3.js: A JavaScript based visualization engine to render the interactive charts and graphs based on the data.
- Dc.js: A JavaScript based wrapper library for D3.js.
- Crossfilter.js: A JavaScript based data manipulation library that enables two way data binding.
- Queue.js: An asynchronous helper library for JavaScript.

## Challenges Faced

The biggest challenge of the project was creating a composite chart to show the total dollar amount of donations received against number of pupils reached.

Initially I planned to use the composite chart as the range chart, but I discovered this is not yet possible with dc.js. Hence the 'Number of Donations' line chart was kept as the range chart. This can be used to filter all the other elements by time period.

The second challenge was creating the choropleth chart to show the US map with states highlighted. To do this I followed the tutorial at [http://adilmoujahid.com/posts/2015/01/interactive-data-visualization-d3-dc-python-mongodb/] (http://adilmoujahid.com/posts/2015/01/interactive-data-visualization-d3-dc-python-mongodb/).

Finally, it was surprisingly tricky to calculate the average donation amount. I found the way to do so in the dc.js docs at [http://dc-js.github.io/dc.js/docs/stock.html](http://dc-js.github.io/dc.js/docs/stock.html).

## Testing 

Manual testing was carried out to ensure all the dashboard items filtered the way they should.

## Outstanding Issue

The responsive design needs to be tweaked to look better on mobile. The chart items display vertically but are not shrunk down to the size of the screen.



