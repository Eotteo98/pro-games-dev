import pygame
WIDTH = 600
HEIGHT = 600


display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("sizes")

pygame.display.update()

class Circle():
    def __init__(self, clr, pos, radius, width):
        self.clr = clr
        self.pos = pos
        self.radius = radius
        self.width = width
        self.surface = display
    
    def draw(self):
        pygame.draw.circle(self.surface, self.clr, self.pos, self.radius, self.width)
    
    def grow(self, r): ##
        self.radius = self.radius + r
        pygame.draw.circle(self.surface, self.clr, self.pos, self.radius, self.width)

circle = Circle('red', (4,4), 20, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type ==pygame.MOUSEBUTTONDOWN:
            circle.draw()
            pygame.display.update()
        
        if event.type == pygame.MOUSEBUTTONUP:
            circle.grow(3)
            pygame.display.update()


     

