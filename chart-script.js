// Set the dimensions of the canvas / graph
var margin = {top: 30, right: 20, bottom: 30, left: 80},
    width = 800 - margin.left - margin.right,
    height = 300 - margin.top - margin.bottom;

// Set the ranges
var x = d3.scale.linear().range([0, width]);
var y = d3.scale.linear().range([height, 0]);

// Define the axes
var xAxis = d3.svg.axis().scale(x)
    .orient("bottom").ticks(5)
    ;

var yAxis = d3.svg.axis().scale(y)
    .orient("left").ticks(5);

// Define the line
var valuelineO = d3.svg.line()
    .x(function(d) { return x(d.n); })
    .y(function(d) { return y(d.operation_error); });

// Another one.
var valuelineS = d3.svg.line()
    .x(function(d) { return x(d.n); })
    .y(function(d) { return y(d.solution_error); });
    
// Adds the svg canvas
var svg = d3.select("body")
    .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
    .append("g")
        .attr("transform", 
              "translate(" + margin.left + "," + margin.top + ")");

var ordinalLU = d3.scale.ordinal()
  .domain(["||LU - P|| error", "||Px - b| error"])
  .range([ "red", "blue"]);

var ordinalQR = d3.scale.ordinal()
  .domain(["||QR - P|| error", "||Px - b|| error"])
  .range([ "red", "blue"]);

// svg.append("g")
//   .attr("class", "legendOrdinal")
//   .attr("transform", "translate(20,20)")
//   .call(legendOrdinal)

// svg.select(".legendOrdinal")
//   .call(legendOrdinal);

var legendLU = d3.legend.color()
  .shapePadding(10)
  .scale(ordinalLU);

var legendQR = d3.legend.color()
  .shapePadding(10)
  .scale(ordinalQR);

var legendGiv = d3.legend.color()
  .shapePadding(10)
  .scale(ordinalQR);


// Select the HH div
var svgHh = d3.select("#hh")
    .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
    .append("g")
        .attr("transform", 
              "translate(" + margin.left + "," + margin.top + ")");

svgHh.append("g")
  .attr("class", "ordinalQR")
  .attr("transform", "translate(20,20)");

svgHh.select(".ordinalQR").call(legendQR);

// Select the LU div
var svgLU = d3.select("#lu")
    .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
    .append("g")
        .attr("transform", 
              "translate(" + margin.left + "," + margin.top + ")");

svgLU.append("g")
  .attr("class", "legendOrdinal")
  .attr("transform", "translate(20,20)")
  .call(legendLU)

// Select the Giv div
var svgGiv = d3.select("#giv")
    .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
    .append("g")
        .attr("transform", 
              "translate(" + margin.left + "," + margin.top + ")");

svgGiv.append("g")
  .attr("class", "legendOrdinal")
  .attr("transform", "translate(20,20)")
  .call(legendLU)

svgHh.append("g")
  .attr("class", "ordinalQR")
  .attr("transform", "translate(20,20)");

svgHh.select(".ordinalQR").call(legendQR);

// Get the data
d3.csv("./data/qr_error_data.csv", function(error, data) {
    data.forEach(function(d) {
        d.n = Number(d.n);
        d.operation_error = Math.round(Number(d.operation_error));
        d.solution_error = Math.round(Number(d.solution_error));
    });
    // Scale the range of the data
    x.domain(d3.extent(data, function(d) { return d.n; }));
    y.domain([0, d3.max(data, function(d) { return Math.max(d.operation_error, d.solution_error); })]);

    // Add the valueline path.
    svgHh.append("path")
        .attr("class", "line")
        .attr("id", "op")
        .attr("d", valuelineO(data));

    // Add the valueline path for the solution error
    svgHh.append("path")
        .attr("class", "line")
        .attr("id", "sol")
        .attr("d", valuelineS(data));

    // Add the scatterplot
    svgHh.selectAll("dot")
        .data(data)
      .enter().append("circle")
        .attr("r", 3.5)
        .attr("cx", function(d) { return x(d.n); })
        .attr("cy", function(d) { 
            return y(d.operation_error);
        });

    // Add the scatterplot
    svgHh.selectAll("dot")
        .data(data)
      .enter().append("circle")
        .attr("r", 3.5)
        .attr("cx", function(d) { return x(d.n); })
        .attr("cy", function(d) { 
            return y(d.solution_error);
        });

    // Add the X Axis
    svgHh.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis);

    // Add the Y Axis
    svgHh.append("g")
        .attr("class", "y axis")
        .call(yAxis);

svgHh.append("text")
    .attr("class", "x label")
    .attr("text-anchor", "end")
    .attr("x", width / 2)
    .attr("y", height + 30)
    .text("N");

svgHh.append("text")
    .attr("class", "y label")
    .attr("text-anchor", "end")
    .attr("y", 6)
    .attr("dy", ".75em")
    .attr("transform", "rotate(-90)")
    .text("Error");
});

/////////////////
// For LU data //
/////////////////

// Get the data
d3.csv("./data/lu_error_data.csv", function(error, data) {
    data.forEach(function(d) {
        d.n = Number(d.n);
        d.operation_error = Math.round(Number(d.operation_error));
        d.solution_error = Math.round(Number(d.solution_error));
    });
    // Scale the range of the data
    x.domain(d3.extent(data, function(d) { return d.n; }));
    y.domain([0, d3.max(data, function(d) { return Math.max(d.operation_error, d.solution_error); })]);

    // Add the valueline path.
    svgLU.append("path")
        .attr("class", "line")
        .attr("d", valuelineS(data));

    // Add the valueline path.
    svgLU.append("path")
        .attr("class", "line")
        .attr("id", "op")
        .attr("d", valuelineO(data));

    // Add the scatterplot
    svgLU.selectAll("dot")
        .data(data)
      .enter().append("circle")
        .attr("r", 3.5)
        .attr("cx", function(d) { return x(d.n); })
        .attr("cy", function(d) { 
            return y(d.operation_error);
        });

    // Add the scatterplot
    svgLU.selectAll("dot")
        .data(data)
      .enter().append("circle")
        .attr("r", 3.5)
        .attr("cx", function(d) { return x(d.n); })
        .attr("cy", function(d) { 
            return y(d.solution_error);
        });

    // Add the X Axis
    svgLU.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis);

    // Add the Y Axis
    svgLU.append("g")
        .attr("class", "y axis")
        .call(yAxis);

    svgLU.append("text")
        .attr("class", "x label")
        .attr("text-anchor", "end")
        .attr("x", width / 2)
        .attr("y", height + 30)
        .text("N");

    svgLU.append("text")
        .attr("class", "y label")
        .attr("text-anchor", "end")
        .attr("y", 6)
        .attr("dy", ".75em")
        .attr("transform", "rotate(-90)")
        .text("Error");
});

/////////////////////
// For Givens data //
/////////////////////

// Get the data
d3.csv("./data/givens_error_data.csv", function(error, data) {
    data.forEach(function(d) {
        d.n = Number(d.n);
        d.operation_error = Math.round(Number(d.operation_error));
        d.solution_error = Math.round(Number(d.solution_error));
    });
    // Scale the range of the data
    x.domain(d3.extent(data, function(d) { return d.n; }));
    y.domain([0, d3.max(data, function(d) { return Math.max(d.operation_error, d.solution_error); })]);

    // Add the valueline path.
    svgGiv.append("path")
        .attr("class", "line")
        .attr("d", valuelineS(data));

    // Add the valueline path.
    svgGiv.append("path")
        .attr("class", "line")
        .attr("id", "op")
        .attr("d", valuelineO(data));

    // Add the scatterplot
    svgGiv.selectAll("dot")
        .data(data)
      .enter().append("circle")
        .attr("r", 3.5)
        .attr("cx", function(d) { return x(d.n); })
        .attr("cy", function(d) { 
            return y(d.operation_error);
        });

    // Add the scatterplot
    svgGiv.selectAll("dot")
        .data(data)
      .enter().append("circle")
        .attr("r", 3.5)
        .attr("cx", function(d) { return x(d.n); })
        .attr("cy", function(d) { 
            return y(d.solution_error);
        });

    // Add the X Axis
    svgGiv.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis);

    // Add the Y Axis
    svgGiv.append("g")
        .attr("class", "y axis")
        .call(yAxis);

    svgGiv.append("text")
        .attr("class", "x label")
        .attr("text-anchor", "end")
        .attr("x", width / 2)
        .attr("y", height + 30)
        .text("N");

    svgGiv.append("text")
        .attr("class", "y label")
        .attr("text-anchor", "end")
        .attr("y", 6)
        .attr("dy", ".75em")
        .attr("transform", "rotate(-90)")
        .text("Error");
});

