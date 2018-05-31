import math

minLenght = 5
proportion = 0.5
branch_color = [0, 0, 0]
startBranch = 0
angle = 0.785

def Tree(x, y, l = 300, _angle = PI/4, _minLenght = 5, _proportion = 0.6, _color = [200, 150, 50], _startBranch = 0): # (start x, start y, initial lenght, the minimum lenght of branch,the proportion of each subsequent branch,color of the branch, from what branch we need to begin to color )
    global minLenght, proportion, branch_color, startBranch, angle
    minLenght = _minLenght
    proportion = _proportion
    branch_color = _color
    startBranch =  _startBranch
    angle = _angle
    
    """
    Formula:
        x(0) = l                   |
                                   | => x(n) = proportion^(n) * l
        x(n+1) = proporion * x(n)  |
        Stop condition:
            x(n) < limit => proportion^(n) * l < limit => n < log(limit/l) with base 'proportion' and then we ceil the result (we can not have 5 branch and half)
    """
    print("The maximum number of branches that can be generated with the current settings is", math.ceil(math.log(minLenght * 1.0/l, proportion)) + 1) # (additional branches) + base branch
    
    translate(x, y)
    branch(l, 0)
    

def branch(l, level): # length of the branch
    
    # Color settings
    _red = branch_color[0]
    _green = branch_color[1] + max(150 ,255 - l)
    _blue = branch_color[2]
    
    stroke(_red, _green, _blue)
    
    line(0, 0, 0, -l)
    translate(0, -l) # go to the top of the brach
    
    if( l > minLenght):
        # Go to right
        pushMatrix() # save the initial coordinates
        rotate(angle) # rotate
        branch(l * proportion, level + 1)
        popMatrix() # return to inital coordinates
        # Go to left
        pushMatrix() # save the initial coordinates
        rotate(-angle) # rotate
        branch(l * proportion, level + 1)
        popMatrix() # return to inital coordinates
        
