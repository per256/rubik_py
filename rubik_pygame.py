import pygame
from pygame.locals import QUIT
from pygame.locals import *
import random

colorlist_side_1=["white","green","yellow","blue"]
colorlist_side_2=["white","green","yellow","blue"]
colorlist_side_3=["white","green","yellow","blue"]
colorlist_side_4=["white","green","yellow","blue"]
colorlist_side_5=["white","green","yellow","blue"]
colorlist_side_6=["white","green","yellow","blue"]
colorlist_side_7=["white","green","yellow","blue"]
colorlist_side_8=["white","green","yellow","blue"]
colorlist_side_9=["white","green","yellow","blue"]

colorlist_over_1=["white","red","yellow","orange"]
colorlist_over_2=["white","red","yellow","orange"]
colorlist_over_3=["white","red","yellow","orange"]
colorlist_over_4=["white","red","yellow","orange"]
colorlist_over_5=["white","red","yellow","orange"]
colorlist_over_6=["white","red","yellow","orange"]
colorlist_over_7=["white","red","yellow","orange"]
colorlist_over_8=["white","red","yellow","orange"]
colorlist_over_9=["white","red","yellow","orange"]

pygame.init()
screen = pygame.display.set_mode((1700,1100), FULLSCREEN)

pygame.display.set_caption("rubik") 

font = pygame.font.SysFont(None, 21)
text_up=font.render("UP", True, (0,0,0))
text_down=font.render("DOWN", True, (0,0,0))
text_right=font.render("RIGHT",True,(0,0,0))
text_left=font.render("LEFT",True,(0,0,0))
text_shuffle=font.render("SHUFFLE",True,(0,0,0))
text_reset=font.render("RESET",True,(0,0,0))
text_colorset=font.render("WHITE",True,(0,0,0))

switch_x=650
switch_y=50

center_x = 650
center_y = 360

right_x=center_x+240
right_y=center_y

left_x=center_x-240
left_y=center_y

high_x=center_x
high_y=center_y-240

low_x=center_x
low_y=center_y+240

back_x=center_x+300
back_y=center_y+300

def Rup():
    save1=colorlist_side_1[1]
    save2=colorlist_side_2[1]
    save3=colorlist_side_6[1]
    save4=colorlist_side_3[1]
    colorlist_side_1[1]=colorlist_side_7[1]
    colorlist_side_2[1]=colorlist_side_4[1]
    colorlist_side_3[1]=save1
    colorlist_side_4[1]=colorlist_side_8[1]
    colorlist_side_6[1]=save2
    colorlist_side_7[1]=colorlist_side_9[1]
    colorlist_side_8[1]=save3
    colorlist_side_9[1]=save4
    
    save=colorlist_over_3[3]
    colorlist_over_3[3]=colorlist_over_3[2]
    colorlist_over_3[2]=colorlist_side_3[2]=colorlist_over_3[1]
    colorlist_over_3[1]=colorlist_over_3[0]
    colorlist_over_3[0]=colorlist_side_3[0]=save
    
    save=colorlist_over_6[3]
    colorlist_over_6[3]=colorlist_over_6[2]
    colorlist_over_6[2]=colorlist_side_6[2]=colorlist_over_6[1]
    colorlist_over_6[1]=colorlist_over_6[0]
    colorlist_over_6[0]=colorlist_side_6[0]=save
        
    save=colorlist_over_9[3]
    colorlist_over_9[3]=colorlist_over_9[2]
    colorlist_over_9[2]=colorlist_side_9[2]=colorlist_over_9[1]
    colorlist_over_9[1]=colorlist_over_9[0]
    colorlist_over_9[0]=colorlist_side_9[0]=save
        
def Rdown():
    save1=colorlist_side_2[1]
    save2=colorlist_side_1[1]
    save3=colorlist_side_4[1]
    save4=colorlist_side_7[1]
    colorlist_side_1[1]=colorlist_side_3[1]
    colorlist_side_2[1]=colorlist_side_6[1]
    colorlist_side_3[1]=colorlist_side_9[1]
    colorlist_side_4[1]=save1
    colorlist_side_6[1]=colorlist_side_8[1]
    colorlist_side_7[1]=save2
    colorlist_side_8[1]=save3
    colorlist_side_9[1]=save4
   
    save=colorlist_over_3[0]
    colorlist_over_3[0]=colorlist_side_3[0]=colorlist_over_3[1]
    colorlist_over_3[1]=colorlist_over_3[2]
    colorlist_over_3[2]=colorlist_side_3[2]=colorlist_over_3[3]
    colorlist_over_3[3]=save
   
    save=colorlist_over_6[0]
    colorlist_over_6[0]=colorlist_side_6[0]=colorlist_over_6[1]
    colorlist_over_6[1]=colorlist_over_6[2]
    colorlist_over_6[2]=colorlist_side_6[2]=colorlist_over_6[3]
    colorlist_over_6[3]=save
   
    save=colorlist_over_9[0]
    colorlist_over_9[0]=colorlist_side_9[0]=colorlist_over_9[1]
    colorlist_over_9[1]=colorlist_over_9[2]
    colorlist_over_9[2]=colorlist_side_9[2]=colorlist_over_9[3]
    colorlist_over_9[3]=save
    
def Mup():
    save= colorlist_over_2[3]
    colorlist_over_2[3]=colorlist_over_2[2]
    colorlist_over_2[2]=colorlist_side_2[2]=colorlist_over_2[1]
    colorlist_over_2[1]=colorlist_over_2[0]
    colorlist_over_2[0]=colorlist_side_2[0]=save
   
    save= colorlist_over_5[3]
    colorlist_over_5[3]=colorlist_over_5[2]
    colorlist_over_5[2]=colorlist_side_5[2]=colorlist_over_5[1]
    colorlist_over_5[1]=colorlist_over_5[0]
    colorlist_over_5[0]=colorlist_side_5[0]=save
   
    save= colorlist_over_8[3]
    colorlist_over_8[3]=colorlist_over_8[2]
    colorlist_over_8[2]=colorlist_side_8[2]=colorlist_over_8[1]
    colorlist_over_8[1]=colorlist_over_8[0]
    colorlist_over_8[0]=colorlist_side_8[0]=save
    
    
def Mdown():
    save=colorlist_over_2[0]
    colorlist_over_2[0]=colorlist_side_2[0]=colorlist_over_2[1]
    colorlist_over_2[1]=colorlist_over_2[2]
    colorlist_over_2[2]=colorlist_side_2[2]=colorlist_over_2[3]
    colorlist_over_2[3]=save
   
    save=colorlist_over_5[0]
    colorlist_over_5[0]=colorlist_side_5[0]=colorlist_over_5[1]
    colorlist_over_5[1]=colorlist_over_5[2]
    colorlist_over_5[2]=colorlist_side_5[2]=colorlist_over_5[3]
    colorlist_over_5[3]=save
   
    save=colorlist_over_8[0]
    colorlist_over_8[0]=colorlist_side_8[0]=colorlist_over_8[1]
    colorlist_over_8[1]=colorlist_over_8[2]
    colorlist_over_8[2]=colorlist_side_8[2]=colorlist_over_8[3]
    colorlist_over_8[3]=save
    
def Lup():
    save1=colorlist_side_2[3]
    save2=colorlist_side_1[3]
    save3=colorlist_side_4[3]
    save4=colorlist_side_7[3]
    colorlist_side_1[3]=colorlist_side_3[3]
    colorlist_side_2[3]=colorlist_side_6[3]
    colorlist_side_3[3]=colorlist_side_9[3]
    colorlist_side_4[3]=save1
    colorlist_side_6[3]=colorlist_side_8[3]
    colorlist_side_7[3]=save2
    colorlist_side_8[3]=save3
    colorlist_side_9[3]=save4
    
    save= colorlist_over_1[3]
    colorlist_over_1[3]=colorlist_over_1[2]
    colorlist_over_1[2]=colorlist_side_1[2]=colorlist_over_1[1]
    colorlist_over_1[1]=colorlist_over_1[0]
    colorlist_over_1[0]=colorlist_side_1[0]=save
   
    save=colorlist_over_4[3]
    colorlist_over_4[3]=colorlist_over_4[2]
    colorlist_over_4[2]=colorlist_side_4[2]=colorlist_over_4[1]
    colorlist_over_4[1]=colorlist_over_4[0]
    colorlist_over_4[0]=colorlist_side_4[0]=save
   
    save=colorlist_over_7[3]
    colorlist_over_7[3]=colorlist_over_7[2]
    colorlist_over_7[2]=colorlist_side_7[2]=colorlist_over_7[1]
    colorlist_over_7[1]=colorlist_over_7[0]
    colorlist_over_7[0]=colorlist_side_7[0]=save
   
def Ldown():
    save1=colorlist_side_1[3]
    save2=colorlist_side_2[3]
    save3=colorlist_side_6[3]
    save4=colorlist_side_3[3]
    colorlist_side_1[3]=colorlist_side_7[3]
    colorlist_side_2[3]=colorlist_side_4[3]
    colorlist_side_3[3]=save1
    colorlist_side_4[3]=colorlist_side_8[3]
    colorlist_side_6[3]=save2
    colorlist_side_7[3]=colorlist_side_9[3]
    colorlist_side_8[3]=save3
    colorlist_side_9[3]=save4
   
    save=colorlist_over_1[0]
    colorlist_over_1[0]=colorlist_side_1[0]=colorlist_over_1[1]
    colorlist_over_1[1]=colorlist_over_1[2]
    colorlist_over_1[2]=colorlist_side_1[2]=colorlist_over_1[3]
    colorlist_over_1[3]=save
   
    save=colorlist_over_4[0]
    colorlist_over_4[0]=colorlist_side_4[0]=colorlist_over_4[1]
    colorlist_over_4[1]=colorlist_over_4[2]
    colorlist_over_4[2]=colorlist_side_4[2]=colorlist_over_4[3]
    colorlist_over_4[3]=save
   
    save=colorlist_over_7[0]
    colorlist_over_7[0]=colorlist_side_7[0]=colorlist_over_7[1]
    colorlist_over_7[1]=colorlist_over_7[2]
    colorlist_over_7[2]=colorlist_side_7[2]=colorlist_over_7[3]
    colorlist_over_7[3]=save

def Hup():
    save1=colorlist_over_2[1]
    save2=colorlist_over_1[1]
    save3=colorlist_over_4[1]
    save4=colorlist_over_7[1]
    colorlist_over_1[1]=colorlist_over_3[1]
    colorlist_over_2[1]=colorlist_over_6[1]
    colorlist_over_3[1]=colorlist_over_9[1]
    colorlist_over_4[1]=save1
    colorlist_over_6[1]=colorlist_over_8[1]
    colorlist_over_7[1]=save2
    colorlist_over_8[1]=save3
    colorlist_over_9[1]=save4
   
    save=colorlist_side_1[3]
    colorlist_side_1[3]=colorlist_side_9[2]
    colorlist_side_9[2]=colorlist_over_9[2]=colorlist_side_1[1]
    colorlist_side_1[1]=colorlist_side_1[0]
    colorlist_side_1[0]=colorlist_over_1[0]=save
   
    save=colorlist_side_2[3]
    colorlist_side_2[3]=colorlist_side_8[2]
    colorlist_side_8[2]=colorlist_over_8[2]=colorlist_side_2[1]
    colorlist_side_2[1]=colorlist_side_2[0]
    colorlist_side_2[0]=colorlist_over_2[0]=save
   
    save=colorlist_side_3[3]
    colorlist_side_3[3]=colorlist_side_7[2]
    colorlist_side_7[2]=colorlist_over_7[2]=colorlist_side_3[1]
    colorlist_side_3[1]=colorlist_side_3[0]
    colorlist_side_3[0]=colorlist_over_3[0]=save
   
def Hdown():
    save1=colorlist_over_1[1]
    save2=colorlist_over_2[1]
    save3=colorlist_over_6[1]
    save4=colorlist_over_3[1]
    colorlist_over_1[1]=colorlist_over_7[1]
    colorlist_over_2[1]=colorlist_over_4[1]
    colorlist_over_3[1]=save1
    colorlist_over_4[1]=colorlist_over_8[1]
    colorlist_over_6[1]=save2
    colorlist_over_7[1]=colorlist_over_9[1]
    colorlist_over_8[1]=save3
    colorlist_over_9[1]=save4
   
    save=colorlist_side_1[0]
    colorlist_side_1[0]=colorlist_over_1[0]=colorlist_side_1[1]
    colorlist_side_1[1]=colorlist_side_9[2]
    colorlist_side_9[2]=colorlist_over_9[2]=colorlist_side_1[3]
    colorlist_side_1[3]=save
   
    save=colorlist_side_2[0]
    colorlist_side_2[0]=colorlist_over_2[0]=colorlist_side_2[1]
    colorlist_side_2[1]=colorlist_side_8[2]
    colorlist_side_8[2]=colorlist_over_8[2]=colorlist_side_2[3]
    colorlist_side_2[3]=save
   
    save=colorlist_side_3[0]
    colorlist_side_3[0]=colorlist_over_3[0]=colorlist_side_3[1]
    colorlist_side_3[1]=colorlist_side_7[2]
    colorlist_side_7[2]=colorlist_over_7[2]=colorlist_side_3[3]
    colorlist_side_3[3]=save
   
def Cup():
    save=colorlist_side_4[3]
    colorlist_side_4[3]=colorlist_side_6[2]
    colorlist_side_6[2]=colorlist_over_6[2]=colorlist_side_4[1]
    colorlist_side_4[1]=colorlist_side_4[0]
    colorlist_side_4[0]=colorlist_over_4[0]=save
    
    save=colorlist_side_5[3]
    colorlist_side_5[3]=colorlist_side_5[2]
    colorlist_side_5[2]=colorlist_over_5[2]=colorlist_side_5[1]
    colorlist_side_5[1]=colorlist_side_5[0]
    colorlist_side_5[0]=colorlist_over_5[0]=save
    
    save=colorlist_side_6[3]
    colorlist_side_6[3]=colorlist_side_4[2]
    colorlist_side_4[2]=colorlist_over_4[2]=colorlist_side_6[1]
    colorlist_side_6[1]=colorlist_side_6[0]
    colorlist_side_6[0]=colorlist_over_6[0]=save
   
def Cdown():
    save=colorlist_side_4[0]
    colorlist_side_4[0]=colorlist_over_4[0]=colorlist_side_4[1]
    colorlist_side_4[1]=colorlist_side_6[2]
    colorlist_side_6[2]=colorlist_over_6[2]=colorlist_side_4[3]
    colorlist_side_4[3]=save
    
    save=colorlist_side_5[0]
    colorlist_side_5[0]=colorlist_over_5[0]=colorlist_side_5[1]
    colorlist_side_5[1]=colorlist_side_5[2]
    colorlist_side_5[2]=colorlist_over_5[2]=colorlist_side_5[3]
    colorlist_side_5[3]=save
    
    save=colorlist_side_6[0]
    colorlist_side_6[0]=colorlist_over_6[0]=colorlist_side_6[1]
    colorlist_side_6[1]=colorlist_side_4[2]
    colorlist_side_4[2]=colorlist_over_4[2]=colorlist_side_6[3]
    colorlist_side_6[3]=save

def Wup():
    save1=colorlist_over_2[3]
    save2=colorlist_over_1[3]
    save3=colorlist_over_4[3]
    save4=colorlist_over_7[3]
    colorlist_over_1[3]=colorlist_over_3[3]
    colorlist_over_2[3]=colorlist_over_6[3]
    colorlist_over_3[3]=colorlist_over_9[3]
    colorlist_over_4[3]=save1
    colorlist_over_6[3]=colorlist_over_8[3]
    colorlist_over_7[3]=save2
    colorlist_over_8[3]=save3
    colorlist_over_9[3]=save4
    
    save=colorlist_side_7[3]
    colorlist_side_7[3]=colorlist_side_3[2]
    colorlist_side_3[2]=colorlist_over_3[2]=colorlist_side_7[1]
    colorlist_side_7[1]=colorlist_side_7[0]
    colorlist_side_7[0]=colorlist_over_7[0]=save
    
    save=colorlist_side_8[3]
    colorlist_side_8[3]=colorlist_side_2[2]
    colorlist_side_2[2]=colorlist_over_2[2]=colorlist_side_8[1]
    colorlist_side_8[1]=colorlist_side_8[0]
    colorlist_side_8[0]=colorlist_over_8[0]=save
    
    save=colorlist_side_9[3]
    colorlist_side_9[3]=colorlist_side_1[2]
    colorlist_side_1[2]=colorlist_over_1[2]=colorlist_side_9[1]
    colorlist_side_9[1]=colorlist_side_9[0]
    colorlist_side_9[0]=colorlist_over_9[0]=save
    
   
def Wdown():
    save1=colorlist_over_1[3]
    save2=colorlist_over_2[3]
    save3=colorlist_over_6[3]
    save4=colorlist_over_3[3]
    colorlist_over_1[3]=colorlist_over_7[3]
    colorlist_over_2[3]=colorlist_over_4[3]
    colorlist_over_3[3]=save1
    colorlist_over_4[3]=colorlist_over_8[3]
    colorlist_over_6[3]=save2
    colorlist_over_7[3]=colorlist_over_9[3]
    colorlist_over_8[3]=save3
    colorlist_over_9[3]=save4
    
    save=colorlist_side_7[0]
    colorlist_side_7[0]=colorlist_over_7[0]=colorlist_side_7[1]
    colorlist_side_7[1]=colorlist_side_3[2]
    colorlist_side_3[2]=colorlist_over_3[2]=colorlist_side_7[3]
    colorlist_side_7[3]=save
    
    save=colorlist_side_8[0]
    colorlist_side_8[0]=colorlist_over_8[0]=colorlist_side_8[1]
    colorlist_side_8[1]=colorlist_side_2[2]
    colorlist_side_2[2]=colorlist_over_2[2]=colorlist_side_8[3]
    colorlist_side_8[3]=save
    
    save=colorlist_side_9[0]
    colorlist_side_9[0]=colorlist_over_9[0]=colorlist_side_9[1]
    colorlist_side_9[1]=colorlist_side_1[2]
    colorlist_side_1[2]=colorlist_over_1[2]=colorlist_side_9[3]
    colorlist_side_9[3]=save
    
def shuffle():
    functions = [Rup, Rdown, Mup, Mdown, Lup, Ldown, Hup, Hdown, Cup, Cdown, Wup, Wdown]

    selected_functions = random.sample(functions, 3)
    for func in selected_functions:
        func()
def reset():
    colorlist_over_1[0]=colorlist_over_2[0]=colorlist_over_3[0]=colorlist_over_4[0]=colorlist_over_5[0]=colorlist_over_6[0]=colorlist_over_7[0]=colorlist_over_8[0]=colorlist_over_9[0]=colorlist_side_1[0]=colorlist_side_2[0]=colorlist_side_3[0]=colorlist_side_4[0]=colorlist_side_5[0]=colorlist_side_6[0]=colorlist_side_7[0]=colorlist_side_8[0]=colorlist_side_9[0]="white"
    colorlist_over_1[1]=colorlist_over_2[1]=colorlist_over_3[1]=colorlist_over_4[1]=colorlist_over_5[1]=colorlist_over_6[1]=colorlist_over_7[1]=colorlist_over_8[1]=colorlist_over_9[1]="red"
    colorlist_over_1[2]=colorlist_over_2[2]=colorlist_over_3[2]=colorlist_over_4[2]=colorlist_over_5[2]=colorlist_over_6[2]=colorlist_over_7[2]=colorlist_over_8[2]=colorlist_over_9[2]=colorlist_side_1[2]=colorlist_side_2[2]=colorlist_side_3[2]=colorlist_side_4[2]=colorlist_side_5[2]=colorlist_side_6[2]=colorlist_side_7[2]=colorlist_side_8[2]=colorlist_side_9[2]="yellow"
    colorlist_over_1[3]=colorlist_over_2[3]=colorlist_over_3[3]=colorlist_over_4[3]=colorlist_over_5[3]=colorlist_over_6[3]=colorlist_over_7[3]=colorlist_over_8[3]=colorlist_over_9[3]="orange"
    colorlist_side_1[1]=colorlist_side_2[1]=colorlist_side_3[1]=colorlist_side_4[1]=colorlist_side_5[1]=colorlist_side_6[1]=colorlist_side_7[1]=colorlist_side_8[1]=colorlist_side_9[1]="green"
    colorlist_side_1[3]=colorlist_side_2[3]=colorlist_side_3[3]=colorlist_side_4[3]=colorlist_side_5[3]=colorlist_side_6[3]=colorlist_side_7[3]=colorlist_side_8[3]=colorlist_side_9[3]="blue"
    
def colorset():
    colorlist_over_1[0]=colorlist_over_2[0]=colorlist_over_3[0]=colorlist_over_4[0]=colorlist_over_5[0]=colorlist_over_6[0]=colorlist_over_7[0]=colorlist_over_8[0]=colorlist_over_9[0]=colorlist_side_1[0]=colorlist_side_2[0]=colorlist_side_3[0]=colorlist_side_4[0]=colorlist_side_5[0]=colorlist_side_6[0]=colorlist_side_7[0]=colorlist_side_8[0]=colorlist_side_9[0]=(255,255,255)
    colorlist_over_1[1]=colorlist_over_2[1]=colorlist_over_3[1]=colorlist_over_4[1]=colorlist_over_5[1]=colorlist_over_6[1]=colorlist_over_7[1]=colorlist_over_8[1]=colorlist_over_9[1]=(255,255,250)
    colorlist_over_1[2]=colorlist_over_2[2]=colorlist_over_3[2]=colorlist_over_4[2]=colorlist_over_5[2]=colorlist_over_6[2]=colorlist_over_7[2]=colorlist_over_8[2]=colorlist_over_9[2]=colorlist_side_1[2]=colorlist_side_2[2]=colorlist_side_3[2]=colorlist_side_4[2]=colorlist_side_5[2]=colorlist_side_6[2]=colorlist_side_7[2]=colorlist_side_8[2]=colorlist_side_9[2]=(255,250,255)
    colorlist_over_1[3]=colorlist_over_2[3]=colorlist_over_3[3]=colorlist_over_4[3]=colorlist_over_5[3]=colorlist_over_6[3]=colorlist_over_7[3]=colorlist_over_8[3]=colorlist_over_9[3]=(250,255,255)
    colorlist_side_1[1]=colorlist_side_2[1]=colorlist_side_3[1]=colorlist_side_4[1]=colorlist_side_5[1]=colorlist_side_6[1]=colorlist_side_7[1]=colorlist_side_8[1]=colorlist_side_9[1]=(250,250,255)
    colorlist_side_1[3]=colorlist_side_2[3]=colorlist_side_3[3]=colorlist_side_4[3]=colorlist_side_5[3]=colorlist_side_6[3]=colorlist_side_7[3]=colorlist_side_8[3]=colorlist_side_9[3]=(255,250,250)
def main():
    
    button_Rup= pygame.Rect(switch_x+170,switch_y, 65, 45)
    button_Rdown = pygame.Rect(switch_x+170, switch_y+800, 65, 45)
    button_Mup= pygame.Rect(switch_x+85, switch_y, 65, 45)
    button_Mdown= pygame.Rect(switch_x+85, switch_y+800, 65, 45)
    button_Lup= pygame.Rect(switch_x+0,switch_y, 65, 45)
    button_Ldown= pygame.Rect(switch_x+0, switch_y+800, 65, 45)
    button_Hup= pygame.Rect(switch_x+500, switch_y+320, 65, 45)
    button_Hdown= pygame.Rect(switch_x-320, switch_y+320, 65, 45)
    button_Cup= pygame.Rect(switch_x+500, switch_y+405, 65, 45)
    button_Cdown= pygame.Rect(switch_x-320, switch_y+405, 65, 45)
    button_Wup= pygame.Rect(switch_x+500, switch_y+500, 65, 45)
    button_Wdown= pygame.Rect(switch_x-320,switch_y+500, 65, 45)
    button_random=pygame.Rect(switch_x+600,switch_y+500, 65, 45)
    button_reset=pygame.Rect(switch_x+700,switch_y+500, 65, 45)
    button_colorset=pygame.Rect(switch_x+800,switch_y+500,65,45)
    
    screen.fill((255,255,255)) 
  
    running = True
    while running:
    
        pygame.draw.rect(screen, (128,128,128), button_Rup)
        pygame.draw.rect(screen, (128,128,128), button_Rdown)
        pygame.draw.rect(screen, (128,128,128), button_Mup)
        pygame.draw.rect(screen, (128,128,128), button_Mdown)
        pygame.draw.rect(screen, (128,128,128), button_Lup)
        pygame.draw.rect(screen, (128,128,128), button_Ldown)
        pygame.draw.rect(screen, (128,128,128), button_Hup)
        pygame.draw.rect(screen, (128,128,128), button_Hdown)
        pygame.draw.rect(screen, (128,128,128), button_Cup)
        pygame.draw.rect(screen, (128,128,128), button_Cdown)
        pygame.draw.rect(screen, (128,128,128), button_Wup)
        pygame.draw.rect(screen, (128,128,128), button_Wdown)
        pygame.draw.rect(screen, (128,128,128), button_random)
        pygame.draw.rect(screen, (128,128,128), button_reset)
        pygame.draw.rect(screen, (128,128,128), button_colorset)
        #センター
        pygame.draw.rect(screen, colorlist_side_1[0], (center_x,center_y,80,80))
        pygame.draw.rect(screen, colorlist_side_2[0], (center_x+80,center_y,80,80))
        pygame.draw.rect(screen, colorlist_side_3[0], (center_x+160,center_y,80,80))
        pygame.draw.rect(screen, colorlist_side_4[0], (center_x,center_y+80,80,80))
        pygame.draw.rect(screen, colorlist_side_5[0], (center_x+80,center_y+80,80,80))
        pygame.draw.rect(screen, colorlist_side_6[0], (center_x+160,center_y+80,80,80))
        pygame.draw.rect(screen, colorlist_side_7[0], (center_x,center_y+160,80,80))
        pygame.draw.rect(screen, colorlist_side_8[0], (center_x+80,center_y+160,80,80))
        pygame.draw.rect(screen, colorlist_side_9[0], (center_x+160,center_y+160,80,80))
        
        pygame.draw.rect(screen, (0,0,0), (center_x,center_y,80,80),width=1)
        pygame.draw.rect(screen, (0,0,0), (center_x+80,center_y,80,80),width=1)
        pygame.draw.rect(screen, (0,0,0), (center_x+160,center_y,80,80),width=1)
        pygame.draw.rect(screen, (0,0,0), (center_x,center_y+80,80,80),width=1)
        pygame.draw.rect(screen, (0,0,0), (center_x+80,center_y+80,80,80),width=1)
        pygame.draw.rect(screen, (0,0,0), (center_x+160,center_y+80,80,80),width=1)
        pygame.draw.rect(screen, (0,0,0), (center_x,center_y+160,80,80),width=1)
        pygame.draw.rect(screen, (0,0,0), (center_x+80,center_y+160,80,80),width=1)
        pygame.draw.rect(screen, (0,0,0), (center_x+160,center_y+160,80,80),width=1)
        
        #右側
        pygame.draw.rect(screen, colorlist_side_1[1], (right_x,right_y,80,80))
        pygame.draw.rect(screen, colorlist_side_2[1], (right_x+80,right_y,80,80))
        pygame.draw.rect(screen, colorlist_side_3[1], (right_x+160,right_y,80,80))
        pygame.draw.rect(screen, colorlist_side_4[1], (right_x,right_y+80,80,80))
        pygame.draw.rect(screen, colorlist_side_5[1], (right_x+80,right_y+80,80,80))
        pygame.draw.rect(screen, colorlist_side_6[1], (right_x+160,right_y+80,80,80))
        pygame.draw.rect(screen, colorlist_side_7[1], (right_x,right_y+160,80,80))
        pygame.draw.rect(screen, colorlist_side_8[1], (right_x+80,right_y+160,80,80))
        pygame.draw.rect(screen, colorlist_side_9[1], (right_x+160,right_y+160,80,80))
        
        pygame.draw.rect(screen, (0,0,0), (right_x,right_y,80,80),width=1)
        pygame.draw.rect(screen, (0,0,0), (right_x+80,right_y,80,80),width=1)
        pygame.draw.rect(screen, (0,0,0), (right_x+160,right_y,80,80),width=1)
        pygame.draw.rect(screen, (0,0,0), (right_x,right_y+80,80,80),width=1)
        pygame.draw.rect(screen, (0,0,0), (right_x+80,right_y+80,80,80),width=1)
        pygame.draw.rect(screen, (0,0,0), (right_x+160,right_y+80,80,80),width=1)
        pygame.draw.rect(screen, (0,0,0), (right_x,right_y+160,80,80),width=1)
        pygame.draw.rect(screen, (0,0,0), (right_x+80,right_y+160,80,80),width=1)
        pygame.draw.rect(screen, (0,0,0), (right_x+160,right_y+160,80,80),width=1)
        
        #左側
        pygame.draw.rect(screen, colorlist_side_1[3], (left_x,left_y,80,80))
        pygame.draw.rect(screen, colorlist_side_2[3], (left_x+80,left_y,80,80))
        pygame.draw.rect(screen, colorlist_side_3[3], (left_x+160,left_y,80,80))
        pygame.draw.rect(screen, colorlist_side_4[3], (left_x,left_y+80,80,80))
        pygame.draw.rect(screen, colorlist_side_5[3], (left_x+80,left_y+80,80,80))
        pygame.draw.rect(screen, colorlist_side_6[3], (left_x+160,left_y+80,80,80))
        pygame.draw.rect(screen, colorlist_side_7[3], (left_x,left_y+160,80,80))
        pygame.draw.rect(screen, colorlist_side_8[3], (left_x+80,left_y+160,80,80))
        pygame.draw.rect(screen, colorlist_side_9[3], (left_x+160,left_y+160,80,80))
        
        pygame.draw.rect(screen, (0,0,0), (left_x,left_y,80,80),width=1)
        pygame.draw.rect(screen, (0,0,0), (left_x+80,left_y,80,80),width=1)
        pygame.draw.rect(screen, (0,0,0), (left_x+160,left_y,80,80),width=1)
        pygame.draw.rect(screen, (0,0,0), (left_x,left_y+80,80,80),width=1)
        pygame.draw.rect(screen, (0,0,0), (left_x+80,left_y+80,80,80),width=1)
        pygame.draw.rect(screen, (0,0,0), (left_x+160,left_y+80,80,80),width=1)
        pygame.draw.rect(screen, (0,0,0), (left_x,left_y+160,80,80),width=1)
        pygame.draw.rect(screen, (0,0,0), (left_x+80,left_y+160,80,80),width=1)
        pygame.draw.rect(screen, (0,0,0), (left_x+160,left_y+160,80,80),width=1)
        
        #上
        pygame.draw.rect(screen, colorlist_over_1[1], (high_x,high_y,80,80))
        pygame.draw.rect(screen, colorlist_over_2[1], (high_x+80,high_y,80,80))
        pygame.draw.rect(screen, colorlist_over_3[1], (high_x+160,high_y,80,80))
        pygame.draw.rect(screen, colorlist_over_4[1], (high_x,high_y+80,80,80))
        pygame.draw.rect(screen, colorlist_over_5[1], (high_x+80,high_y+80,80,80))
        pygame.draw.rect(screen, colorlist_over_6[1], (high_x+160,high_y+80,80,80))
        pygame.draw.rect(screen, colorlist_over_7[1], (high_x,high_y+160,80,80))
        pygame.draw.rect(screen, colorlist_over_8[1], (high_x+80,high_y+160,80,80))
        pygame.draw.rect(screen, colorlist_over_9[1], (high_x+160,high_y+160,80,80))
        
        pygame.draw.rect(screen, (0,0,0), (high_x,high_y,80,80),width=1)
        pygame.draw.rect(screen, (0,0,0), (high_x+80,high_y,80,80),width=1)
        pygame.draw.rect(screen, (0,0,0), (high_x+160,high_y,80,80),width=1)
        pygame.draw.rect(screen, (0,0,0), (high_x,high_y+80,80,80),width=1)
        pygame.draw.rect(screen, (0,0,0), (high_x+80,high_y+80,80,80),width=1)
        pygame.draw.rect(screen, (0,0,0), (high_x+160,high_y+80,80,80),width=1)
        pygame.draw.rect(screen, (0,0,0), (high_x,high_y+160,80,80),width=1)
        pygame.draw.rect(screen, (0,0,0), (high_x+80,high_y+160,80,80),width=1)
        pygame.draw.rect(screen, (0,0,0), (high_x+160,high_y+160,80,80),width=1)
        
        #下
        pygame.draw.rect(screen, colorlist_over_1[3], (low_x,low_y,80,80))
        pygame.draw.rect(screen, colorlist_over_2[3], (low_x+80,low_y,80,80))
        pygame.draw.rect(screen, colorlist_over_3[3], (low_x+160,low_y,80,80))
        pygame.draw.rect(screen, colorlist_over_4[3], (low_x,low_y+80,80,80))
        pygame.draw.rect(screen, colorlist_over_5[3], (low_x+80,low_y+80,80,80))
        pygame.draw.rect(screen, colorlist_over_6[3], (low_x+160,low_y+80,80,80))
        pygame.draw.rect(screen, colorlist_over_7[3], (low_x,low_y+160,80,80))
        pygame.draw.rect(screen, colorlist_over_8[3], (low_x+80,low_y+160,80,80))
        pygame.draw.rect(screen, colorlist_over_9[3], (low_x+160,low_y+160,80,80))
        
        pygame.draw.rect(screen, (0,0,0), (low_x,low_y,80,80),width=1)
        pygame.draw.rect(screen, (0,0,0), (low_x+80,low_y,80,80),width=1)
        pygame.draw.rect(screen, (0,0,0), (low_x+160,low_y,80,80),width=1)
        pygame.draw.rect(screen, (0,0,0), (low_x,low_y+80,80,80),width=1)
        pygame.draw.rect(screen, (0,0,0), (low_x+80,low_y+80,80,80),width=1)
        pygame.draw.rect(screen, (0,0,0), (low_x+160,low_y+80,80,80),width=1)
        pygame.draw.rect(screen, (0,0,0), (low_x,low_y+160,80,80),width=1)
        pygame.draw.rect(screen, (0,0,0), (low_x+80,low_y+160,80,80),width=1)
        pygame.draw.rect(screen, (0,0,0), (low_x+160,low_y+160,80,80),width=1)
        
        #後ろ
        pygame.draw.rect(screen, colorlist_side_7[2], (back_x,back_y,80,80))
        pygame.draw.rect(screen, colorlist_side_8[2], (back_x+80,back_y,80,80))
        pygame.draw.rect(screen, colorlist_side_9[2], (back_x+160,back_y,80,80))
        pygame.draw.rect(screen, colorlist_side_4[2], (back_x,back_y+80,80,80))
        pygame.draw.rect(screen, colorlist_side_5[2], (back_x+80,back_y+80,80,80))
        pygame.draw.rect(screen, colorlist_side_6[2], (back_x+160,back_y+80,80,80))
        pygame.draw.rect(screen, colorlist_side_1[2], (back_x,back_y+160,80,80))
        pygame.draw.rect(screen, colorlist_side_2[2], (back_x+80,back_y+160,80,80))
        pygame.draw.rect(screen, colorlist_side_3[2], (back_x+160,back_y+160,80,80))
        
        pygame.draw.rect(screen, (0,0,0), (back_x,back_y,80,80),width=1)
        pygame.draw.rect(screen, (0,0,0), (back_x+80,back_y,80,80),width=1)
        pygame.draw.rect(screen, (0,0,0), (back_x+160,back_y,80,80),width=1)
        pygame.draw.rect(screen, (0,0,0), (back_x,back_y+80,80,80),width=1)
        pygame.draw.rect(screen, (0,0,0), (back_x+80,back_y+80,80,80),width=1)
        pygame.draw.rect(screen, (0,0,0), (back_x+160,back_y+80,80,80),width=1)
        pygame.draw.rect(screen, (0,0,0), (back_x,back_y+160,80,80),width=1)
        pygame.draw.rect(screen, (0,0,0), (back_x+80,back_y+160,80,80),width=1)
        pygame.draw.rect(screen, (0,0,0), (back_x+160,back_y+160,80,80),width=1)
        
        screen.blit(text_up, (switch_x+190,switch_y+15))
        screen.blit(text_down, (switch_x+175,switch_y+815))
        screen.blit(text_up, (switch_x+105,switch_y+15))
        screen.blit(text_down, (switch_x+90,switch_y+815))
        screen.blit(text_up, (switch_x+20,switch_y+15))
        screen.blit(text_down, (switch_x+5,switch_y+815))
        screen.blit(text_right, (switch_x+505,switch_y+335))
        screen.blit(text_left, (switch_x-310,switch_y+335))
        screen.blit(text_right, (switch_x+505,switch_y+420))
        screen.blit(text_left, (switch_x-310,switch_y+420))
        screen.blit(text_right, (switch_x+505,switch_y+515))
        screen.blit(text_left, (switch_x-310,switch_y+515))
        screen.blit(text_shuffle,(switch_x+600,+switch_y+515))
        screen.blit(text_reset,(switch_x+705,+switch_y+515))
        screen.blit(text_colorset,(switch_x+805,+switch_y+515))
        
        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_Rup.collidepoint(event.pos):
                    Rup()
                if button_Rdown.collidepoint(event.pos):
                    Rdown()
                if button_Mup.collidepoint(event.pos):
                    Mup()
                if button_Mdown.collidepoint(event.pos):
                    Mdown()
                if button_Lup.collidepoint(event.pos):
                    Lup()
                if button_Ldown.collidepoint(event.pos):
                    Ldown()
                if button_Hup.collidepoint(event.pos):
                    Hup()
                if button_Hdown.collidepoint(event.pos):
                    Hdown()
                if button_Cup.collidepoint(event.pos):
                    Cup()
                if button_Cdown.collidepoint(event.pos):
                    Cdown()
                if button_Wup.collidepoint(event.pos):
                    Wup()
                if button_Wdown.collidepoint(event.pos):
                    Wdown()
                if button_random.collidepoint(event.pos):
                    shuffle()
                if button_reset.collidepoint(event.pos):
                    reset()
                if button_colorset.collidepoint(event.pos):
                    colorset()
if __name__=="__main__":
        main()