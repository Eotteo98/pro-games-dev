import pgzrun
import time
import pygame
pygame.init()
WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("digital_cards")

img = pygame.image.load("birthday_cake.jpg")
imhg = pygame.transform.scale(img, (WIDTH,HEIGHT))
img1 = pygame.image.load("birthday_background.jpg")
imhg1 = pygame.transform.scale(img1, (WIDTH,HEIGHT))
img2 = pygame.image.load("birthday_background_2.jpg")
imhg2 = pygame.transform.scale(img2, (WIDTH,HEIGHT))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    font = pygame.font.SysFont("Calibri", 40)
    text = font.render("Happy birthday!", True, ("red"))
    screen.blit(imhg, (0, 0))
    screen.blit(text, (150, 400))
    pygame.display.update()
    time.sleep(2)


    font1 = pygame.font.SysFont("Helvetica", 40)
    text1 = font1.render("Have fun this year", True, ("red"))
    screen.blit(imhg1, (0, 0))
    screen.blit(text1, (150, 400))
    pygame.display.update()
    time.sleep(2)

    font2 = pygame.font.SysFont("Arial", 40)
    text2 = font2.render("Have a blessed year!", True, ("red"))
    screen.blit(imhg2, (0, 0))
    screen.blit(text2, (150, 400))
    pygame.display.update()
    time.sleep(2)



    pygame.quit()

