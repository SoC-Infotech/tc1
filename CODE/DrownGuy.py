# Imports two library to our game
import pygame
import random

#Initialize the pygame (;oop, game screen)
pygame.init()

#Declares some variables
winHeight = 480
winWidth = 700
GREEN = (0, 255, 0)

#Create window game
win = pygame.display.set_mode((winWidth,winHeight))
pygame.display.set_caption("Drown Guy")

#main program
#   create game loop to keep the window
inPlay = True
while inPlay:
    win.fill(GREEN) #Make background colour green
    pygame.display.update
    pygame.time.delay(10)
    




#quit the pygame
pygame.quit()
