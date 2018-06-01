import Circle

img = loadImage("2018.png")
pixelPos = []
theList = []
nrLimit = 2000

def setup():
    size(400, 250)
    frameRate(30)

    # Load a black-white image
    global img
    # img = loadImage("2018.png")
    # img = loadImage("costi.png")
    # img = loadImage("invinctus.png")
    img = loadImage("ivy.png")
    img.loadPixels()
    
    # Take the position of the white pixels
    for x in range(width):
        for y in range(height):
            index = x + width * y 
            if(brightness(img.pixels[index]) > 1):
                pixelPos.append(PVector(x, y))
    print(len(pixelPos))
    
def draw():
    background(255)
    
    # Create
    create()
   
    # Update & Draw
    for circle in theList:
        if(circle.isGrowing):
            circle.grow(0.5)
            circle.update(theList, [width, height])
        circle.display()
    
    # Save frames
    if(frameCount < 80):
        saveFrame("frames/image####.png")
        print("Frame Saved",frameCount)
    else:
        print("End")
        noLoop()

def create():
    global pixelPos, theList, nrLimit
    if(len(theList) < nrLimit and len(pixelPos) - 300 > 0):
        for i in range(300):
           index = int(random(0, len(pixelPos)))
           tmp = (pixelPos[index]).get()
           pixelPos.pop(index)
           
           test = Circle.Circle(tmp.x, tmp.y)
           
           if(test.checkCollision(theList, [width, height]) == False):
              theList.append(test)
    
