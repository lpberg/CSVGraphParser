from GraphMLWriter import GraphMLWriter
from VisJSWriter import VisJSWriter
from os import path

class Node:
	def __init__(self, parentList):
		self.name = parentList[-1]
		self.id = str(id(self))
		self.parents = "none"
		if len(parentList) > 1:
			self.parents = parentList[:-1]

class Edge:
	def __init__(self,source,destination):
		self.source = source
		self.destination = destination
	
class CSVGraphParser:
	def __init__(self,inputFilePath,mode):
		self.nodes = []
		self.edges = []
		self.fileContent = []
		head, ext = path.splitext(inputFilePath)
		self.readFile(inputFilePath)
		self.createNodes()
		self.createEdges()
		if mode.lower() == "graphml":
			writer = GraphMLWriter(self.nodes,self.edges,head+".graphml")
			print "Created file: "+head+".graphml ("+str(len(self.nodes))+" nodes, "+str(len(self.edges))+" edges)"
		if mode.lower() == "visjs":
			writer = VisJSWriter(self.nodes,self.edges,head+".html")
			print "Created file: "+head+".html ("+str(len(self.nodes))+" nodes, "+str(len(self.edges))+" edges)"

	def readFile(self,inputFile):
		for line in open(inputFile, 'r'):
			self.fileContent.append(line.strip().split(","))
			
	def createNodes(self):
		for line in self.fileContent:
			self.createNodesFromParentString(line)

	def createEdges(self):
		for node in self.nodes:
			if node.parents != "none":
				e = Edge(node,self.getNodeByName(node.parents[-1]))
				self.edges.append(e)

	def doesNodeExist(self,newNode):
		for node in self.nodes:
			if ((node.name == newNode.name) and (node.parents == newNode.parents)):
				return True
		return False

	def getNodeByName(self,nodeName):
		for node in self.nodes:
			if node.name == nodeName:
				return node
		return False

	def createNodesFromParentString(self,parentList):
		if(len(parentList) == 0):
			 return
		if(len(parentList) > 0):
			newNode = Node(parentList)
			if not(self.doesNodeExist(newNode)):
				self.nodes.append(newNode)
				self.createNodesFromParentString(parentList[:-1])

myParser = CSVGraphParser("/Users/lpberg/Desktop/SampleInput.csv","visjs")
#myParser = CSVGraphParser("/Users/lpberg/Desktop/SampleInput.csv","graphml")


