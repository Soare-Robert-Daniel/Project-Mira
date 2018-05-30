def CircleInsideCircle(x , y , radius):
    stroke(0)
    noFill()
    ellipse(x, y, radius, radius)
    
    if(radius > 15):
        radius *= 0.7 # reduce the radius with 30 %
        CircleInsideCircle(x, y, radius) # Draw again

def CircleCross(x , y , radius):
    stroke(30)
    noFill()
    ellipse(x, y, radius, radius)
    
    if(radius > 15):
        radius *= 0.7 # reduce the radius with 30 %
        CircleInsideCircle(x + radius, y, radius) # Draw again
        CircleInsideCircle(x - radius, y, radius)
        CircleInsideCircle(x , y + radius, radius)
        CircleInsideCircle(x , y - radius, radius)
        CircleInsideCircle(x, y, radius)

def CircleSquare(x , y , radius):
    stroke(30)
    noFill()
    ellipse(x, y, radius, radius)
    
    if(radius > 10):
        radius *= 0.7 # reduce the radius with 30 %
        CircleSquare(x + radius, y, radius) # Draw again
        CircleSquare(x - radius, y, radius)
        CircleSquare(x , y + radius, radius)
        CircleSquare(x , y - radius, radius)
        
