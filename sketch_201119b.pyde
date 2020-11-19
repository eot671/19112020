#size(1000, 1000)
#background(255, 0, 0)
#n=50
#m=10
#step_x = width // n
#step_y = height // m
#for i in range(n):
    #offset_x = step_x*i
    #ellipse(30+offset_x, 30, 40, 40)
    #delay(100)
    #fill(255, 0, 0)
    #stroke(255, 0, 0)
    #delay(100)
    #fill(255, 255, 255)
    #stroke(0, 0, 0)
#size(1000, 1000)
#background(255, 0, 0)
#n=50
#m=10
#step_x = width // n
#step_y = height // m
x = 0
y = 0
d = 10
def setup():
    size (400, 400)
    noStroke()
    
def draw():
    global x, y
    background(255)
    
    x = x + 1
    if x > width + d:
        x = -d
    translate (x, d)
    fill(0)
    ellipse(-d/2, -d/2, d, d)

 
