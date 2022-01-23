from nodes import Nodes

counter = 0
Heuristic=[]

def heuristic():#συνάρτηση να βρίσκει το heuristic σε μέγεθος του αρχικού πίνακα
    global Heuristic
    Heuristic=[[]for i in range(totalLines)]

    for i in range(totalLines):
        for j in range(totalColumns):
            Heuristic[i].append(0)
    for i in Heuristic:
        print(i)
    gi = -1
    gj = -1
    for i in range(totalLines):
        for j in range(totalColumns):
            if (labyrinth[i][j] != 'G'):
                continue
            else:
                gi=i
                gj=j

    for i in range(totalLines):
        for j in range(totalColumns):
            dy=abs(i-gi)
            dx=abs(j-gj)
            Heuristic[i][j]=dx+dy
    for i in Heuristic:
        print(i)

def makeQueue(node):#συνάρτηση για να βρίσκουμε και να επιστρέφουμε τα παιδιά ενός κόμβου
    tmpQ =[]
    i = node.state[0]
    j = node.state[1]
    print("i=", i, "j=", j)


    if (i + 1 < totalLines and labyrinth[i + 1][j] != "X" and node.fathernode.state != [i + 1,j]):
        tmpNode = Nodes([i + 1, j], node, node.cost, node.depth, labyrinth[i + 1][j],0) # moved "down"
        tmpNode.depth += 1
        tmpNode.cost += 1
        nodecounter()
        if (tmpNode.value == 'D'):
            tmpNode.cost += 1
        tmpNode.Hvalue = Heuristic[i+1][j]+tmpNode.cost
        tmpQ.append(tmpNode)
        del tmpNode

    if (j + 1 < totalColumns and labyrinth[i][j + 1] != "X" and node.fathernode.state != [i,j + 1]):
        tmpNode = Nodes([i, j + 1], node, node.cost, node.depth, labyrinth[i][j + 1],0)  # moved "right"
        tmpNode.depth += 1
        tmpNode.cost += 1
        nodecounter()
        if (tmpNode.value == 'D'):
            tmpNode.cost += 1
        tmpNode.Hvalue = Heuristic[i][j+1]+tmpNode.cost
        tmpQ.append(tmpNode)
        del tmpNode

    if (i - 1 >= 0 and labyrinth[i - 1][j] != "X" and node.fathernode.state != [i-1 , j]):
        tmpNode = Nodes([i - 1, j], node, node.cost, node.depth, labyrinth[i - 1][j],0) # moved "up"
        tmpNode.depth += 1
        tmpNode.cost += 1
        nodecounter()
        if (tmpNode.value == 'D'):
            tmpNode.cost += 1
        tmpNode.Hvalue = Heuristic[i-1][j]+tmpNode.cost
        tmpQ.append(tmpNode)
        del tmpNode

    if (j - 1 >= 0 and labyrinth[i][j - 1] != "X" and node.fathernode.state != [i,j - 1]):
        tmpNode = Nodes([i, j - 1], node, node.cost, node.depth, labyrinth[i][j - 1],0)  # moved "left"
        tmpNode.depth += 1
        tmpNode.cost += 1
        nodecounter()
        if (tmpNode.value == 'D'):
            tmpNode.cost += 1
        tmpNode.Hvalue = Heuristic[i][j-1]+tmpNode.cost
        tmpQ.append(tmpNode)
        del tmpNode
    return tmpQ

def backTracePath(currentNode):#συνάρτηση για να βρίσκουμε το μονοπάτι της λύσης
    """
    backTracePath
    :param currentNode: Ο τορινός κόμβος (κόμβος λύση)
    :return: ένα string με τις καταστάσεις που οδηγούν στην αρχή (μονοπάτι)
    """
    btNode = currentNode #backTraceNode
    path = ''
    # Εκμεταλευεται το fathernode, ξεκινάμε απο τον G και πάμε στον father του (προς τα πίσω κίνηση)
    while (btNode.value != 'S'):
        path = path + str(btNode.state) + ' -> '  # κρατάμε την κατάσταση στο string αυτο
        btNode = btNode.fathernode
        # fathernode απο τον τορινο
        # ο επόμενος γίνεαι ο πατέρας του τορινού
        # Εδώ θα μπορούσε να υπολογιστεί το depth.

    path = path + str(btNode.state)
    return path

def test():
    print(totalLines)
    print(totalColumns)


def nodecounter():#συνάρτηση για να διαβάζει τους κόμβους
    global counter
    counter += 1

def ucs(queue):
    previouslyvisited=[]
    quepos=1
    tmpNode=queue[0]
    while (tmpNode.value != 'G'):
        # for i in queue: #PRINT ton pinaka se kathe epanalhpsh
        #   print("State:",i.state,"Cost:",i.cost,"Depth",i.depth,"Value",i.value)
        print(quepos, ":", tmpNode.value, ":")
        queue.extend(makeQueue(tmpNode))
        previouslyvisited.append(queue.pop(0))
        queue = sorted(queue, key=lambda Nodes: Nodes.cost)
        tmpNode = queue[0]
        quepos += 1

        if (tmpNode.value == "G"):
            quepos += 1
            previouslyvisited.append(tmpNode)
            for i in queue: #print ton pinaka otan bvriskei ton komvo
                print("State:", i.state, "Cost:", i.cost, "Depth", i.depth, "Value", i.value)
            print(quepos,":",tmpNode.value,":")
            print("Congratulations you found it!! State:",tmpNode.state)
    print("Nodes:", counter)
    #print("Path to the GoalNode", backTracePath(tmpNode))
    path = backTracePath(tmpNode)
    return path

def ids(queue):
    tmpNode=queue[0]
    maxdepth=1
    previouslyvisited=[]
    startNode = Nodes([0, 0], Nodes([-1, -1], [-1, -1], -1, -1, "null"), 0, 0, "S")


    while (tmpNode.value != 'G'):
        print("element popped:",queue[0].state)
        previouslyvisited.append(queue.pop(0))
        while(tmpNode.depth==maxdepth):#Ελέγχει ποια στοιχεία έχουν βάθος ίσο με το όριο για να τα διώξει
            # και να μην τα αναπτύξει
            print("eimai sto while")
            if (tmpNode.value=='G'):
                break
            elif(len(queue) == 0 ):
                print("-------")
                print("maxdepth:", maxdepth)  # εκτυπώνει το όριο βάθους των παραπάνω κόμβων
                print("-------")
                previouslyvisited = []
                tmpNode = startNode
                previouslyvisited.append(tmpNode)
                maxdepth += 1
                break
            tmpNode = queue[0]
            print("tmpNode",tmpNode.state)
            previouslyvisited.append(queue.pop(0))
        queue = makeQueue(tmpNode) + queue
        tmpNode = queue[0]



    for i in queue:  # print ton pinaka otan bvriskei ton komvo
        print("State:", i.state, "Cost:", i.cost, "Depth", i.depth, "Value", i.value)
    print(tmpNode.value, ":")
    print("Congratulations you found it!! State:", tmpNode.state)
    print("Nodes: and depth:", counter,maxdepth)
    path=backTracePath(tmpNode)
    return path

def Astar(queue):
    previouslyvisited=[]
    quepos=1
    tmpNode=queue[0]
    while (tmpNode.value != 'G'):
        # for i in queue: #PRINT ton pinaka se kathe epanalhpsh
        #   print("State:",i.state,"Cost:",i.cost,"Depth",i.depth,"Value",i.value)
        print(quepos, ":", tmpNode.value, ":")
        queue.extend(makeQueue(tmpNode))
        previouslyvisited.append(queue.pop(0))
        queue = sorted(queue, key=lambda Nodes: Nodes.Hvalue)
        tmpNode = queue[0]
        quepos += 1

        if (tmpNode.value == "G"):
            quepos += 1
            previouslyvisited.append(tmpNode)
            for i in queue: #print ton pinaka otan bvriskei ton komvo
                print("State:", i.state, "Cost:", i.cost, "Depth", i.depth, "Value", i.value)
            print(quepos,":",tmpNode.value,":")
            print("Congratulations you found it!! State:",tmpNode.state)
    print("Nodes:", counter)
    path=backTracePath(tmpNode)
    return path

lst = []
labyrinth = []
global totalColumns
global totalLines

file1 = open('Λαβύρινθος.txt', 'r')

# diavazoume to arxeio
for i in file1:
    for j in i:
        if (j == '\n'):
            continue
        lst.append(j)
    labyrinth.append(lst)
    lst = []

totalLines = len(labyrinth)

for i in labyrinth:
    totalColumns = 0
    print(i)
    for j in i:
        totalColumns += 1

heuristic()

queue=[]
startNode = Nodes([0, 0],Nodes([-1,-1],[-1,-1],-1,-1,"null"), 0, 0, "S",15)
queue.append(startNode)

#U=ucs(queue)
queue=[]
startNode = Nodes([0, 0],Nodes([-1,-1],[-1,-1],-1,-1,"null"), 0, 0, "S",15)
queue.append(startNode)

I=ids(queue)

queue=[]
startNode = Nodes([0, 0],Nodes([-1,-1],[-1,-1],-1,-1,"null"), 0, 0, "S",15)
queue.append(startNode)

#A=Astar(queue)
#print("Path to the GoalNode from A",A)
#print("Path to the GoalNode from  IDS",I)
#print("Path to the GoalNode from UCS",U)

nodecounter()
counter=0

