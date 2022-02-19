
from Location import Location
from Node import Node

class field(object):
    
    def __init__(self, radius):
        self.nodes = {}
        self.radius = radius
        
    def addNode(self, node, x, y):
        print(f'Hangi node geldi -->{node}')
        self.nodes[node] = Location(x, y)
        print(self.__str__())
        print('------------------')
        for FieldNode in self.nodes.copy():
            # print(self.nodes.copy(), f'Listedeki Node --> {FieldNode},  normal Node --> {node}')
            if FieldNode != node:
                print('aynı değil')
                if (abs(self.nodes[FieldNode].getX() - x) < self.radius) and (abs(self.nodes[FieldNode].getY() - y) < self.radius):
                    # print((abs(self.nodes[FieldNode].getX() - x) < self.radius))
                    # print((abs(self.nodes[FieldNode].getY() - y) < self.radius))   #Debugging
                    # print(f"{node}'u siliyorum")
                    self.removeNode(node)
                    return False #For condition in DrawingNodes.py 
        
                
    def clearNodes(self):
        self.nodes = {}
    def removeNode(self, node):
        if not node in self.nodes:
            raise KeyError('Node not in Field')
        self.nodes.pop(node)
        

    def updateRadius(self, radius):
        self.radius = radius

    def moveNode(self, node, delX, delY):
        self.nodes[node] = self.nodes[node].MoveLocation(delX,delY)
        
    def get_loc(self, node):
        print('beni çağırdılar', node)
        return self.nodes[node]
    
    def getNodes(self):
        return self.nodes
    
    def __str__(self):
        strr = ''
        for x in self.nodes:
            strr = strr + f"'{x}' --> {self.nodes[x].getX()}, {self.nodes[x].getY()}\n"
        return strr[:-1]
     