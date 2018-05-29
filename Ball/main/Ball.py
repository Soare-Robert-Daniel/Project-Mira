import Vector

class Ball:
    
    maxVel = 10
    
    def __init__(self, startPos = PVector(0,0), radius = 10, velocity = PVector(0,0), acceleration = PVector(0,0), mass = 1):
        self.radius = radius
        self.pos = startPos     # position
        self.vel = velocity     # velocity
        self.acc = acceleration # acceleration
        self.mass = mass        # mass
        self.dir = self.pos.normalize()
        self.force = self.mass * self.acc
    
    def display(self):
        ellipse(self.pos.x, self.pos.y, self.radius, self.radius)
        
    def move(self):
        
        # Update velocity
        self.vel.add(self.acc)
        self.vel.limit(self.maxVel)
        
        # Reset acceleration
        self.acc.mult(0)     
        
        # Update position
        self.pos.add(self.vel)
        
        
    
    def applyForce(self,force):
        forceAcc = PVector.div(force, self.mass)
        
        # Update the acceleration and direction
        self.acc.add(forceAcc)
        self.dir = forceAcc.normalize()
    
    def setMaxVel(self, vlimit):
        self.maxVel = self.maxVel
