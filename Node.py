class Node:
    def __init__(self, matrix, dep):
        self.state = matrix
        self.cost = dep
        self.depth = dep
    
    def getMatrix(self):
        return self.state

    def getCost(self):
        return self.cost
    
    def getDepth(self):
        return self.depth
    
    def setDepth(self, num):
        self.depth = num

    def setCost(self, num):
        self.cost = num

    def __lt__(self, other):
        return self.cost < other.cost

