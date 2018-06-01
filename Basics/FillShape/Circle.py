class Circle(object):
    isGrowing = True
    isOverlapping = False
    
    def __init__(self, startX, startY, radius = 1, _color = [30, 60, 90], _offset = 2, _radiusLimit = 9):
        self.x = startX
        self.y = startY
        self.r = radius
        self.strokeColor = _color
        self.offset = _offset # this will increase the distance between circles
        self.radiusLimit = _radiusLimit
        
    def grow(self, amount):
        # print(self.isGrowing)
        if(self.isGrowing and self.radiusLimit > self.r):
            self.r += amount
    
    def display(self):
        stroke(self.strokeColor[0], self.strokeColor[1], self.strokeColor[2])
        fill(int(random(255)), int(random(255)), int(random(255)))
        ellipse(self.x, self.y, self.r * 2, self.r * 2)
        
    def update(self, others, winBorders): 
        
        if(self.isGrowing == True and self.checkCollision(others, winBorders)):
            self.isGrowing = False
        
    def checkCollision(self, others, winBorders):
        # Check distance between circles
        for other in others:
            if(other is not self):
                d = dist(self.x, self.y, other.x, other.y)
                if( d - self.offset < self.r + other.r ):
                    # print(self.x, self.y, other.x, other.y, d)
                    self.isOverlapping = True
                    return True
                
        # Check if the circle touch the window's borders  
        if( self.x - self.r < 0 or self.x + self.r > winBorders[0] or self.y - self.r < 0 or self.y + self.r > winBorders[1]):
            self.isOverlapping = True
            return True
        
        return False
        
