# Main

import Ball


# Environment Setup

ball = Ball.Ball()

gravity = PVector(0, 0.1) * ball.mass
dragCoef = 0.02
# Floor
floorV = PVector(0,-1) # direction * magnitude
floorP = []

def setup():
  size(800, 800)
  
  # Ball Setup
  pos  = PVector(width/2, height * 0.1)
  ball.pos = pos
  ball.radius = 20
  
  # Floor Setup
  floorP.append(PVector(0, height * 0.9))
  floorP.append(PVector(width, height * 0.9))

def draw():   
  clear()
  background(255)
  drawWorld()

  ball.applyForce(gravity)
  ball.applyForce(getFriction())

  ball.move() # Update the position
  
  # Check collision with the floor
  if(ball.pos.y + ball.radius/2 > floorP[0].y):
      ball.vel.y *= -1
      ball.pos.y = floorP[0].y - ball.radius/2
  
  ball.display()

def drawWorld():
    line(floorP[0].x,floorP[0].y,floorP[1].x,floorP[1].y);  # Draw floor 

def getFriction():
    drag = ball.vel.get()
    drag.mult(-1)
    drag.normalize()
    normal = 1
    
    drag.mult(dragCoef * normal)
    
    return drag
  
