import random
import pgzrun
WIDTH = 600
HEIGHT = 600
TITLE = "balls"
GRAVITY = 2000

class Ball:
    def __init__(self, x, y , radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.vx = 100
        self.vy = 0
        R = random.randint(0,255)
        G = random.randint(0,255)
        B = random.randint(0,255)
        self.clr = (R, G, B)
    
    def show(self):
        pos = (self.x , self.y)
        screen.draw.filled_circle(pos, self.radius, self.clr)
    

ball = Ball(32 , 20, 30)

def draw():
    screen.clear()
    ball.show()

def update(dt):
    # Apply constant acceleration formulae    
    uy = ball.vy # uy = current vertical velocity of ball
    ball.vy += GRAVITY * dt #(v=u+at) ball's vertical velocity increases due to the acc. of gravity 
    ball.y += (uy + ball.vy) * 0.5 * dt #(s = ut + 1/2 at^2)  - calculate avg. velocity over the time interval dt
    # detect and handle bounce
    if ball.y > HEIGHT - ball.radius:  # we've bounced!
        ball.y = HEIGHT - ball.radius  # fix the position
        ball.vy = -ball.vy * 0.9  # inelastic collision
    # X component doesn't have acceleration
    ball.x += ball.vx * dt
    if ball.x > WIDTH - ball.radius or ball.x < ball.radius:
        ball.vx = -ball.vx

def on_key_down(key):
    if key == keys.SPACE:
        ball.vy = -300
    

pgzrun.go()
