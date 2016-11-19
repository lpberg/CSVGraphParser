class GraphMLWriter:
	def __init__(self,nodes,edges,outputFilePath):
		self.nodes = nodes
		self.edges = edges
		self.colors = ["#0059b3","#0080ff","#3399ff","#66b3ff","#99ccff","#cce6ff","#ffffff"]
		self.headerString = '''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
		<graphml
		 xmlns="http://graphml.graphdrawing.org/xmlns"
		 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
		 xmlns:y="http://www.yworks.com/xml/graphml"
		 xmlns:yed="http://www.yworks.com/xml/yed/3"
		 xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns http://www.yworks.com/xml/schema/graphml/1.1/ygraphml.xsd">
		  <key for="node" id="d1" yfiles.type="nodegraphics"/>
		  <graph edgedefault="directed" id="G">'''
		self.footerString = '''</graph>
		</graphml>
		'''
		self.writeToFile(outputFilePath)

	def writeToFile(self,outputFilePath):
		outfile = open(outputFilePath,"w")
		outfile.write(self.headerString)
		for node in self.nodes:
			outfile.write(self.getGraphMLNodeString(node)+"\n")
		for edge in self.edges:
			outfile.write(self.getGraphMLEdgeString(edge)+"\n")
		outfile.write(self.footerString)
		outfile.close()

	def getGraphMLNodeString(self,node):
		return '''
		 <node id="'''+node.id+'''">
	      <data key="d1">
	        <y:ShapeNode>
	          <y:Fill color="'''+self.colors[len(node.parents)]+'''" transparent="false"/>
	          <y:NodeLabel>'''+node.name+'''</y:NodeLabel>
	        </y:ShapeNode>
	      </data>
	    </node>
	    '''
	def getGraphMLEdgeString(self,edge):	
		return '<edge id="'+edge.source.name+edge.destination.name+'" source="'+edge.source.id+'" target="'+edge.destination.id+'"/>'



