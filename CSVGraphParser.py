import headerFooterStrings as strs

class Node:
	def __init__(self, parentList):
		self.name = parentList[-1]
		self.id = str(id(self))
		self.parents = "none"
		if len(parentList) > 1:
			self.parents = parentList[:-1]
		self.colors = ["#0059b3","#0080ff","#3399ff","#66b3ff","#99ccff","#cce6ff","#ffffff"]
	def getGraphMLString(self):
		return '''
		 <node id="'''+self.name+'''">
	      <data key="d1">
	        <y:ShapeNode>
	          <y:Fill color="'''+self.colors[len(self.parents)]+'''" transparent="false"/>
	          <y:NodeLabel>'''+self.name+'''</y:NodeLabel>
	        </y:ShapeNode>
	      </data>
	    </node>
	    '''
    def getVisJSString(self):
    	return "    {id: "+self.id+", label: '"+self.name+"'},"

class Edge:
	def __init__(self,source,destination):
		self.source = source
		self.destination = destination
	def getGraphMLString(self):	
		return '<edge id="'+self.source+self.destination+'" source="'+self.destination+'" target="'+self.source+'"/>'

class CSVGraphParser:
	def __init__(self,inputFile,outputFile,mode):
		self.nodes = []
		self.edges = []
		self.fileContent = []	
		self.readInCSV(inputFile)
		self.createNodes()
		self.createEdges()
		if mode.lower() == "graphml":
			self.writeOutToGraphMLFile(outputFile)
		if mode.lower() == "visjs":
			self.writeOutToVisJSFile(outputFile)

	def readInCSV(self,inputFile):
		for line in open(inputFile, 'r'):
			self.fileContent.append(line.strip().split(","))
			
	def createNodes(self):
		for line in self.fileContent:
			self.createNodesFromParentString(line)

	def createEdges(self):
		for node in self.nodes:
			if node.parents != "none":
				self.edges.append(Edge(node.name,node.parents[-1]))

	def writeOutToGraphMLFile(self,outputFile):
		outfile = open(outputFile,"w")
		outfile.write(strs.GraphMLHeaderString)
		for node in self.nodes:
			outfile.write(node.getGraphMLString())
		for edge in self.edges:
			outfile.write(edge.getGraphMLString()+"\n")
		outfile.write(strs.GraphMLFooterString)
		outfile.close()

	def nodeAlreadyExists(self,newNode):
		for node in self.nodes:
			if ((node.name == newNode.name) and (node.parents == newNode.parents)):
				return True
		return False

	def createNodesFromParentString(self,parentList):
		if(len(parentList) == 0):
			 return
		if(len(parentList) > 0):
			newNode = Node(parentList)
			if not(self.nodeAlreadyExists(newNode)):
				self.nodes.append(newNode)
				self.createNodesFromParentString(parentList[:-1])
				print("Creating Node: " + newNode.name)

myParser = CSVGraphParser("/Users/lpberg/Desktop/L1L2.csv","/Users/lpberg/Desktop/outfile.graphml","GraphML")


