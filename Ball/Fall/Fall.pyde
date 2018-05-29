# Main

import Ball
"""
   ISSUES: despite that all the balls had different initial values for velocity and position
           they are spawned in the same position with the same velocity
"""

# Environment Setup
balls = []
N = 4
def setup():
  size(800, 800)
  
  # Balls Setup
  global N  # Nr of balls
  global balls
  for i in range(N):
    balls += [Ball.Ball(id = i,startPos = PVector(random(200, width), random(200,height)) ,radius = random(15, 50), turnRate = random(1,2))]
    print(balls[i].turnRate)
    
    force = PVector(random(-30,30), random(-30,30))
    force.normalize()
    force.mult(i * ((-1)**i))
    balls[i].acc = force
    balls[i].move()
    print(balls[i].vel)
   
 
def draw():   
  global balls
  clear()
  background(255)
  drawWorld()
      

  for i in range(N):
    balls[i].move() # Update the position
  
  collision()
  
  for ball in balls:
    ball.display()

def mouseMoved():
    mouse = PVector(mouseX, mouseY)
    for ball in balls:
      
      dir = PVector.sub(mouse, ball.pos)
      dir.normalize()
      dir.mult(ball.turnRate)
      ball.applyForce(dir)

def drawWorld():
    pass
    
def collision():
    global balls

    for ball in balls:
        if(ball.pos.x > width):
            ball.pos.x = 0
            
        elif(ball.pos.x < 0):
            ball.pos.x = width
            
        elif(ball.pos.y > height):
            ball.pos.y = 0
            
        if(ball.pos.y < 0):
            ball.pos.y = height
            
    
