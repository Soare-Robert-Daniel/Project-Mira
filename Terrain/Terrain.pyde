cols = 0
rows = 0
dis = 20  # distance between vertes
w = 600   # width of the grid
h = 600   # height ot the grid
angleX = 60 
terrain_mesh = []
seed = 0


def setup():
    global cols, rows, dis, h, w, terrain_mesh

    cols = w / dis
    rows = h / dis
    # terrain_mesh = [ [0] * cols ] * rows
    terrain_mesh = [[ 0 for i in range(cols)] for j in  range(rows)]
    # print(terrain_mesh)
    
    colorMode(RGB, 255)
    size(600, 600, P3D)

def draw():
    global cols, rows, dis, h, w, angleX, terrain_mesh, seed
    
    background(255)
    stroke(0)
    #noFill();
    
    # wave(seed)
    generate_terrain(seed)
    # drop(seed)
    seed += 0.1
    
    translate(width/2, height/2) # put the origin to the center of the screen
    rotateX(radians(angleX)) # make the perspectiv
    translate(-w/2, -h/2) # introduce the grid
    
    for y in range(rows - 1):
        beginShape(TRIANGLE_STRIP)
        for x in range(cols):
            fill(255, map(terrain_mesh[y][x], -75, 75, 0, 255), 0, map(terrain_mesh[y][x], -75, 75, 0, 255))
            
            vertex(x * dis, y * dis, terrain_mesh[y][x])
            vertex(x * dis, (y+1) * dis, terrain_mesh[y+1][x])
        endShape() 
    if(frameCount < 80):
        saveFrame("frames/image####.png")
        print("Frame Saved",frameCount)
    else:
        print("End")
        noLoop()

# Use perlin noise
def generate_terrain(seed):
    global cols, rows, dis, h, w, angleX, terrain_mesh
    yoff = seed
    for y in range(rows):
        xoff = 0
        beginShape(TRIANGLE_STRIP)
        for x in range(cols):
            terrain_mesh[y][x] = map(noise(xoff, yoff), 0, 1, -75, 75)
            # print(terrain_mesh[x][y])
            xoff += 0.1
        yoff -= 0.1  

# Wave effect
def wave(seed):
    global cols, rows, dis, h, w, angleX, terrain_mesh
    yoff = -1
    for y in range(rows):
        xoff = -1
        beginShape(TRIANGLE_STRIP)
        for x in range(cols):
            r = xoff * xoff + yoff * yoff
            terrain_mesh[y][x] = map(cos(r + seed), -1, 1, -30, 30)
            # print(terrain_mesh[x][y])
            xoff += 0.1
        yoff -= 0.1  

# Drop effect
def drop(seed):
    global cols, rows, dis, h, w, angleX, terrain_mesh

    startX = -10.0
    endX = 10.0
    scaleX = (endX - startX) / cols
    
    startY = -10.0
    endY = 10.0
    scaleY = (endY - startY) / rows

    yoff = -10
    for y in range(rows):
        xoff = -10
        beginShape(TRIANGLE_STRIP)
        for x in range(cols):
            distance = dist(xoff , yoff , 0, 0)
            terrain_mesh[y][x] = map(sin( distance - seed) , -1, 1, -30, 30)
            # terrain_mesh[y][x] = distance
            # print(terrain_mesh[x][y])
            xoff += scaleX
        yoff += scaleY  
