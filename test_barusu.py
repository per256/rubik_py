import pygame
from pygame.locals import *
from pygame.locals import QUIT
import sys
import random
import keyboard
import time

def main ():
    pygame.init()
    pygame.display.set_caption("バルス")
    screen = pygame.display.set_mode((1920,1200),FULLSCREEN)
    font = pygame.font.SysFont("hgpｺﾞｼｯｸm",400)
    while True:
        if keyboard.is_pressed('q'):
            pygame.QUIT
            pygame.quit()
            sys.exit()

        R = random.randint(0,255)
        G = random.randint(0,255)
        B = random.randint(0,255)
        RM = random.randint(0,255)
        GM = random.randint(0,255)
        BM = random.randint(0,255)
        txt = font.render("バルス☆",True,(RM,GM,BM))
        x = random.randint(0,100)
        y = random.randint(0,100)
        zahyoux = 150+x
        zahyouy = 250+y
        screen.fill((R,G,B))
        screen.blit(txt,(zahyoux,zahyouy))
        #time.sleep(0.02)
        pygame.display.update()
        
if __name__ == '__main__':
    main()


