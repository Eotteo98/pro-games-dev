import pygame
import random

pygame.init()
WIDTH = 600
HEIGHT = 600
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("my first py game class")

class Cubes():
    #properties
    def __init__(self, dimensions):
        self.surface = display
        r = random.randint(0, 225)
        g = random.randint(0, 225)
        b = random.randint(0, 225)
        self.color = (r,g,b)
        self.dimensions = dimensions


    #functions
    def draw(self):
        self.cube = pygame.draw.rect(self.surface, self.color, self.dimensions)
        
#objects
red_cube = Cubes( (20, 20, 300,300))
green_cube = Cubes( (20, 20, 200,600))

#main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    red_cube.draw()
    green_cube.draw()
    pygame.display.update()

pygame.quit()



