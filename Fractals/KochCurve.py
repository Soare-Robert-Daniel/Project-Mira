class Line(object):
    
    def __init__(self,start = PVector(0,0), end = PVector(0,0)):
        self.start = start.get()
        self.end = end.get()
    
    def display(self):
        line(self.start.x, self.start.y, self.end.x, self.end.y)
    
    def afisare(self):
        print(self.start, self.end) 
    
    @staticmethod
    def rotatePoint(p, angle = 0):
        angle = radians(angle)
        point = p.get()
        # Rotate the point
        x = point.x *  cos(angle) - point.y * sin(angle)
        y = point.x *  sin(angle) + point.y * cos(angle)
        # Set the precision
        x = round(x, 2)
        y = round(y, 2)
        return PVector( x, y)
    
    def ComputeKochPoints(self):
        
        """
                   C
                 /   \           
        A ----- B     D------E
            1/3   1/3    1/3 
        """
        
        # Point A
        a = self.start.get()
        
        # Point B
        b = PVector.sub(self.end.get(), self.start.get()) # get the line between the end and starting point
        b.div(3) # make the lenght 1/3 of the initial value
        b.add(self.start.get()) # the point location are local (the origin is the starting point) => global 
        
        # Point C
        c = PVector.sub(self.end.get(), self.start.get())
        c.div(3)
        c = self.rotatePoint(c, -60)
        c.add(b)
        
        # Point D
        d = PVector.sub(self.end.get(), self.start.get())
        d.div(3)
        d.add(b)
        
        # Point E
        e = self.end.get()
        
        return [a, b, c, d, e]


def ComputeKochLines(_line):
    a,b,c,d,e = _line.ComputeKochPoints()
    return [Line(a,b), Line(b,c), Line(c,d), Line(d,e)]

def ComputeKoch(lines):
    newLines = []
    for _line in lines:
        newLines.extend(ComputeKochLines(_line))
    return newLines
    
def TestRotate():
    p = PVector(1,0)
    offx = width/2;
    line(0 + offx,0 + offx, p.x * 100 + offx, p.y * 100 + offx)
    q = Line.rotatePoint(p, -90)
    line(0 + offx,0 + offx, q.x * 100 + offx, q.y * 100 + offx)
    print(q)
