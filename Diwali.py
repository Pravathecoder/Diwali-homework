import pygame
import time

pygame.init() #initialize

WIDTH = 600
HEIGHT = 600
pygame.display.set_caption('Happy Diwali')
screen = pygame.display.set_mode((WIDTH,HEIGHT))

img1 = pygame.image.load('images/diwalibg1.png') #loding the image
image1 = pygame.transform.scale(img1,(WIDTH,HEIGHT)) #Changing witdh and height

while True:
     #font loading
     font = pygame.font.SysFont('Arial',72)

     #text loading
     text1 = font.render('Happy',True,(0,0,0))
     text2 = font.render('Diwali',True,(0,0,0))

     #showing on screen 
     screen.fill((255,255,255))
     screen.blit(image1,(0,0)) #show image on screen

      #show text on screen 
     screen.blit(text1,(210,120))
     screen.blit(text2,(225,265))

     pygame.display.update()
     time.sleep(2)

     

