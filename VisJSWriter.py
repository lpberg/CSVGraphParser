class VisJSWriter:
	def __init__(self,nodes,edges,outputFilePath):
		self.nodes = nodes
		self.edges = edges
		self.colors = ["#0059b3","#0080ff","#3399ff","#66b3ff","#99ccff","#cce6ff","#ffffff"]
		self.headerString = '''<!doctype html>
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

		self.footerString = '''
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
		self.writeToFile(outputFilePath)

	def writeToFile(self,outputFilePath):
		outfile = open(outputFilePath,"w")
		outfile.write(self.headerString)
		outfile.write("\n")
		outfile.write("  var nodes = new vis.DataSet(["+"\n")
		for node in self.nodes:
			outfile.write(self.getGraphMLNodeString(node)+"\n")
		outfile.write("  ]);")
		outfile.write("\n")
		outfile.write("  var edges = new vis.DataSet(["+"\n")
		for edge in self.edges:
			outfile.write(self.getGraphMLEdgeString(edge)+"\n")
		outfile.write("  ]);")		
		outfile.write(self.footerString)
		outfile.close()

	def getGraphMLEdgeString(self,edge):
		return "    {from: "+edge.source.id+", to: "+edge.destination.id+"},"
	
	def getGraphMLNodeString(self,node):
		return "    {id: "+node.id+", label: '"+node.name+"'},"
	
		

