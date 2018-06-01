# Fractals Basics
import Circle
import KochCurve
import Trees

KochLines = []

def setup():
    # test = KochCurve.Line( PVector(0,height*0.8), PVector(width,height*0.8))
    # KochLines.append(test)
    
    size(800,800)
    
    
def draw():
    background(255)
    # Circle.CircleSquare(width/2, height/2, 100)
    # Circle.CircleInsideCircle(width/2, height/2, 100)
    # Circle.CircleCross(width/2, height/2, 100)
    # KochCurve.TestRotate()
    # for i in KochLines:
    #     i.display()
    Trees.Tree(x = width/2, y = height, l = 200, _angle = PI/4, _color = [255, 0, 255])
        
def mousePressed():
    # global KochLines
    # KochLines = KochCurve.ComputeKoch(KochLines)
    
    pass


    
