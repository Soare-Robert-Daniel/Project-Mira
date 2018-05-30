
class Ball(object):

    maxVel = 5

    def __init__(self,id = -1, startPos = PVector(300,300), radius = 10, velocity = PVector(0,0), acceleration = PVector(0,0), mass = 1, color = [255, 255, 255], turnRate = 0.5):
        self.id = id
        self.radius = radius
        self.pos = startPos.get()     # position
        self.vel = velocity.get()     # velocity
        self.acc = acceleration.get() # acceleration
        self.mass = mass        # mass
        self.dir = self.pos.normalize()
        self.force = self.mass * self.acc
        self.turnRate = turnRate
        self.color = color
    

    def display(self):
        stroke(0);
        strokeWeight(2);
        fill(self.color[0], self.color[1], self.color[2]);
        ellipse(self.pos.x, self.pos.y, self.radius, self.radius)
        # print(self.id, self.vel)
        
        
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
