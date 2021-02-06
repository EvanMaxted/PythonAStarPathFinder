import mazeDrawer

parent = {} # keeps track of each node's parent node
            # (the node that is before them in the path)

'''
function : A star search
purpose : find the shortes path between start and end
in : maze, start, end
return : shortest path
'''
def aStarSearch(maze, start, end):
    openList = {}
    closedList = {}
                    ###F,G,H
    openList[start] = [0,0,0]

    while len(openList) > 0:
        minF = 9999
        #finds the node that has the lowest F value and assigns it to current
        for node in openList: # length of open list times O(n)
            if openList[node][0] < minF:
                minF = openList[node][0]
                minNode = node
        current = minNode
        #current gets added to closed list
        closedList[current] = None

        # draws current node unless node is start or end
        if current != start and current != end: 
            mazeDrawer.currentDraw(current)
        # if end is in closed list that means it was found in the best possible path   
        if end in closedList:
            return findPath(start, end)
        
        #x,y of current so neighbors are easier to find
        x = current[0]
        y = current[1] #N        E       S       W
        currentnbrs = [(x,y-1),(x+1,y),(x,y+1),(x-1,y)]
        
        for node in currentnbrs: #goes through each neighbor of current
            
            if node[0] < 0 or node[0] > len(maze[0])-1 or node[1] < 0 or node[1] > len(maze)-1: # node is out of bounds off the maze
                continue
            
            elif node in closedList: # already been visited
                continue
            
            elif maze[node[1]][node[0]] != '0': # anything that isn't 0 is a wall
                continue
            
            elif node not in openList: # if node is not in open list
                parent[node] = current # current node is its new parent
                nodeG = openList[current][1] + 10 #distance from start node (each step is worth 10)
                nodeH = manhattan(end, node) * 10 #manhattan heuristic
                nodeF = nodeG + nodeH
                openList[node] = [nodeF, nodeG, nodeH] #add it to open list with its 3 values
                
            elif node in openList: #if node is already in open list
                if openList[node][1] > 10 + openList[current][1]: #this is if the path we are currently checking is better than its previous path
                    parent[node] = current #update its parent
                    nodeG = openList[current][1] + 10 #update G
                    nodeH = manhattan(end, node) * 10 #update H
                    nodeF = nodeG + nodeH
                    openList[node] = [nodeF, nodeG, nodeH] # update node's 3 values in the open list
                    
        # removes current node from open list since it and its 4 neighbors have all been checked         
        del openList[current]
        
    #this only happens if no path is found from start to end
    return None

'''
function : manhattan
purpose : find the distance from the node to the end
in : end, node
return : manhattan distance
'''
def manhattan(end, node):
    endX = end[0]
    endY = end[1]
    nodeX = node[0]
    nodeY = node[1]
    return ((endX-nodeX)**2)**.5 + ((endY-nodeY)**2)**.5
'''
function : find path
purpose : goes through parents from end to start to find the path
in : start, end
return : path
'''
def findPath(start, end):
    path = []
    node = end     
    while node != start:
        path.append(node)
        node = parent[node]
    path.append(start)   

    return path[::-1] # returns path backwards because it is given from end to start originally since it follows the parents
