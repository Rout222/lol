<!DOCTYPE html>
<meta charset="utf-8">
<style>
.link {
    stroke: #ffff00;
    stroke-dasharray: 5, 10, 5;
    stroke-width: 2;
}
.linkWeak {
    stroke: #800000;
    stroke-width: 1;
}
.linkStrong {
    stroke: #009933;
    stroke-width: 4;
    stroke-dasharray: 2,2,2;

}
.node text {
    pointer-events: none;
    font: 10px sans-serif;
}

</style>
<svg width="2000" height="1800"></svg>
<script src="//d3js.org/d3.v4.min.js"></script>
<script>

var svg = d3.select("svg"),
    width = +svg.attr("width"),
    height = +svg.attr("height");

var simulation = d3.forceSimulation()
    .force("charge", d3.forceManyBody().strength(-200))
    .force("link", d3.forceLink().id(function(d) { return d.id; }).distance(40))
    .force("x", d3.forceX(width / 2))
    .force("y", d3.forceY(height / 2))
    .on("tick", ticked);

var link = svg.selectAll(".link"),
    node = svg.selectAll(".node");

d3.json("output.json", function(error, graph) {
  if (error) throw error;

  simulation.nodes(graph.nodes);
  simulation.force("link").links(graph.links);
  simulation.force("charge", d3.forceManyBody().strength(-200))
    .force("link", d3.forceLink().id(function(d) { return d.id; }).distance(40))
    .force("x", d3.forceX(width / 2))
    .force("y", d3.forceY(height / 2))
    .on("tick", ticked);

  link = link
    .data(graph.links)
    .enter().append("line")
      .attr("class", function(d) { 
        if (d.win > 0.7) {return "linkStrong";}
        else if (d.win > 0.5){
          return "link";}
        else{
          return "linkWeak"
        }
        ; })

  node = node
    .data(graph.nodes)
    .enter().append("image")
    .attr("class", "node")
    .attr("xlink:href", function(d) { return "https://ddragon.leagueoflegends.com/cdn/8.1.1/img/champion/" + d.id + ".png"; })


    .attr("x", -16)
    .attr("y", -16)
    .attr("width", 32)
    .attr("height", 32)
    .call(d3.drag()
          .on("start", dragstarted)
          .on("drag", dragged)
          .on("end", dragended))
;
});

function ticked() {
  link.attr("x1", function(d) { return d.source.x; })
      .attr("y1", function(d) { return d.source.y; })
      .attr("x2", function(d) { return d.target.x; })
      .attr("y2", function(d) { return d.target.y; });

  node.attr("cx", function(d) { return d.x; })
      .attr("cy", function(d) { return d.y; });
      node.attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });
}
function dragstarted(d) {
  if (!d3.event.active) simulation.alphaTarget(0.3).restart();
  d.fx = d.x;
  d.fy = d.y;
}

function dragged(d) {
  d.fx = d3.event.x;
  d.fy = d3.event.y;
}

function dragended(d) {
  if (!d3.event.active) simulation.alphaTarget(0);
  d.fx = null;
  d.fy = null;
}

</script>