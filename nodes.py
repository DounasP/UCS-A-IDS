class Nodes:
    def __init__(self,state=[-1, -1], fathernode=[-1, -1], cost=-1, depth=-1, value="null",Hvalue=-1):
        self.state = state
        self.fathernode = fathernode
        self.cost = cost
        self.depth = depth
        self.value = value
        self.Hvalue= Hvalue

    def printclass(self):
        print("State:", self.state,
              "Fathernde:", self.fathernode,
              "Cost:", self.cost,
              "Depth:", self.depth,
              "Value:", self.value)




