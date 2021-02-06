from SimpleGraphics import*  

'''
function : maze init
purpose : draw the maze boundaries fit into the graphic window
in : maze list
return : none
'''
def mazeInit(maze):
    resize(len(maze[0])*40, len(maze)*40) #sets screen to fit maze
    setColor(250,250,250)
    rect(0,0,len(maze[0])*40+1, len(maze)*40+1) #sets off white background to show a grid
    setColor(255, 255, 255)
    #O(height*width)
    for i in range(len(maze)): # height of maze times
        for j in range(len(maze[i])): # width of maze times
            rect(j*40 +1, i*40 +1 , 38, 38)

    
'''
function : path draw
purpose : draw the shortest path from start to end
in : shortest path, node positions
return : none
'''    
def pathDraw(path):
    setColor(81,76,229)
    for node in path: # length of path times
        sleep(0.15) #delays slightly to show step by step
        i = node[0]
        j = node[1]        
        rect(i*40 +1, j*40 +1 , 38, 38)        

'''
function : mouse input
purpose : read the user's mouse input when they pick start and end
in : none
return : maze list position at x and y
'''
def mouseInput():
    while True:
        update()
        sleep(.09)
        if leftButtonPressed(): # when the user clicks their left mouse return the x,y of their cursor
            x = mouseX()
            y = mouseY()
            return x//40, y//40


'''
function : start draw
purpose : draw starting node on maze
in : x and y coordinate of starting position
return : none
'''
def startDraw(x,y): 
    x = x*40
    y = y*40
    setColor(96,251,30)
    ellipse(x+1,y+1,38,38)
    setColor(0,0,0)
    setFont('Arial','20')
    text(x+20,y+20,'S')  

'''
function : goal draw
purpose : draw end node on maze
in : x and y coordinate of end position
return : none
'''
def goalDraw(x,y):
    x = x*40
    y = y*40
    setColor(255,152,26)
    ellipse(x+1,y+1,38,38)
    setColor(0,0,0)
    setFont('Arial','20')
    text(x+20,y+20,'E') 


'''
function : wall draw
purpose : draw walls where the user 
in : x and y of wall
return : none
'''
def wallDraw(maze):      
    setColor(255,0,0)
    rect(1,1,38,38) # make the top left square noticeable
    
    wall = mouseInput()
    while wall != (0,0): # if they select top left tile
        maze[wall[1]][wall[0]] = '1' #sets the node to a wall that cannot be walked over
        x = wall[0]*40
        y = wall[1]*40
        setColor(51,52,60)
        rect(x+1,y+1,38,38)
        wall = mouseInput()

    #set top left rectangle back to white   
    setColor(255,255,255) 
    rect(1,1,38,38)


'''
function : image drawer
purpose : draws title and instruction screen until user clicks to continue
in : name of image
return : none
'''
def titleScreenDraw(imageName):
    resize(1200,720)
    drawImage(imageName, 0, 0)
    sleep(1)
    while leftButtonPressed() == False:
        drawImage(imageName, 0, 0)


'''
function : current draw
purpose : show the current node the maze is testing
in : current node
return : none
'''
def currentDraw(current):
    sleep(.05) #small pause to show step by step
    x = current[0]*40
    y = current[1]*40
    setColor(76,223,229)
    rect(x+1,y+1,38,38)
