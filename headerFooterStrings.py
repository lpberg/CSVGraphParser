GraphMLHeaderString = '''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
		<graphml
		 xmlns="http://graphml.graphdrawing.org/xmlns"
		 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
		 xmlns:y="http://www.yworks.com/xml/graphml"
		 xmlns:yed="http://www.yworks.com/xml/yed/3"
		 xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns http://www.yworks.com/xml/schema/graphml/1.1/ygraphml.xsd">
		  <key for="node" id="d1" yfiles.type="nodegraphics"/>
		  <graph edgedefault="directed" id="G">'''
GraphMLFooterString = '''</graph>
		</graphml>
		'''
VisJSHeaderString = '''<!doctype html>
<html>
<head>
  <title>Network | Basic usage</title>

  <script type="text/javascript" src="vis-network.min.js"></script>
  <link href="vis-network.min.css" rel="stylesheet" type="text/css" />

  <style type="text/css">
    #mynetwork {
      width: 800px;
      height: 800px;
      border: 1px solid lightgray;
    }
  </style>
</head>
<body>

<p>
  Create a simple network with some nodes and edges.
</p>

<div id="mynetwork"></div>

<script type="text/javascript">
  // create an array with nodes'''

VisJSFooterString = '''
  // create a network
  var container = document.getElementById('mynetwork');
  var data = {
    nodes: nodes,
    edges: edges
  };
  var options = {
	  layout: {
	    randomSeed: undefined,
	    improvedLayout:true,
	    hierarchical: {
	      enabled:true,
	      levelSeparation: 150,
	      nodeSpacing: 100,
	      treeSpacing: 200,
	      blockShifting: true,
	      edgeMinimization: true,
	      parentCentralization: true,
	      direction: 'UD',        // UD, DU, LR, RL
	      sortMethod: 'directed'   // hubsize, directed
	    }
	  }
  };
  var network = new vis.Network(container, data, options);
</script>

</body>
</html>
'''