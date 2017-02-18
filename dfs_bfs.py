from collections import deque

class Node:
    def __init__(self, name, val = 0):
        self.val = val
        self.name = name
        self.visited = False
        self. links = []

    def connectNode(self, node):
        self.links.append(node)
        node.links.append(self)

class Search:
    def __init__(self):
       self.valueFound = False
 
class Graph:
    def __init__(self):
        self.nodeA = Node("A")
        self.nodeB = Node("B")
        self.nodeC = Node("C")
        self.nodeD = Node("D")
        self.nodeE = Node("E")
        self.nodeF = Node("F")
        self.nodeG = Node("G")
        self.nodeH = Node("H", 5)
        self.nodeS = Node("S")
        
        self.nodeA.connectNode(self.nodeB)
        self.nodeA.connectNode(self.nodeS)
    
        self.nodeS.connectNode(self.nodeC)
        self.nodeS.connectNode(self.nodeG)
        
        self.nodeC.connectNode(self.nodeD)
        self.nodeC.connectNode(self.nodeE)
        self.nodeC.connectNode(self.nodeF)
    
        self.nodeE.connectNode(self.nodeH)
        
        self.nodeF.connectNode(self.nodeG)
        
        self.nodeG.connectNode(self.nodeH)

    def getNode(self):
        return self.nodeA

class DepthFirstSearch(Search):

    def search(self, val, node):
        if(self.valueFound == True):
            return

        print "DFS Searching node", node.name

        # Is the value in the current node?

        if(node.val == val):
            print "DFS Found the value in node", node.name
            self.valueFound = True
            return

        node.visited = True

        # Difference bewtween BFS and DFS is here
        # Immediately traverse to the the link node (if it exists) 
        # and check it for a search match 

        for link in node.links:
            if(link.visited != True):
                self.search(val, link)

class BreathFirstSearch(Search):

    def __init__(self):
        Search.__init__(self)
        self.queue = deque()

    def search(self, val, node):
        if(self.valueFound == True):
            return

        print "BFS Searching node", node.name

        # Is the value in the current node?

        if(node.val == val):
            print "BFS Found the value in node", node.name 
            self.valueFound = True
            return

        node.visited = True

        # Difference btween BFS and DFS is here
        # Do not immeiately go to the link node
        # check a link for a match, if no match
        # save the link node in a queue and check its links
        # after checking the links node ahead of it in the queue

        for link in node.links:             

            #search each of the linked nodes for the value

            if(link.visited == True):
                continue

            if(link.val == val):
                print "BFS Found the value in node", link.name 
                self.valueFound = True
                return
            else:
                self.queue.appendleft(link)
                
        while(len(self.queue) > 0):
            nextNode = self.queue.pop()
            self.search(val, nextNode)
                
graph1 = Graph()

dfs = DepthFirstSearch()
dfs.search(5, graph1.getNode())

graph2 = Graph()

bfs = BreathFirstSearch()
bfs.search(5, graph2.getNode())
