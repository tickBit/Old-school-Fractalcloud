"""
This program is based on my old Amiga assembly program,
that was somekind of fractal cloud generator.

As youngster I read theory about it in early 90's.
In 2022, I tried to remember something about the theory
and understand my old Amiga assembly program.

This Python experiment is the result of that.
"""

import pygame
import random

pygame.init()
screen = pygame.display.set_mode((513,513))
pygame.display.set_caption("Fractal cloud")

J = 256

x = 0
y = 0

B1 = 0
B2 = 0
B3 = 0
B4 = 0


while J > 1:
    y = 0
    while 512 - J / 2 >= y + J / 2:
        x = 0
        while 512 - J / 2>= x + J / 2:
        
            
            B1 = screen.get_at((int(x), int(y)))[0]
            if B1 == 0: B1 = random.randint(20,255)
            
            
            B2 = screen.get_at((int(x+J),int(y)))[0]
            if B2 == 0: B2 = random.randint(20,255)            

           
            B3 = screen.get_at((int(x),int(y+J)))[0]
            if B3 == 0: B3 = random.randint(20,255)

       
            B4 = screen.get_at((int(x+J),int(y+J)))[0]
            if B4 == 0: B4 = random.randint(20,255)
            

            #if screen.get_at((int(x+J/2),int(y+J/2)))[0] == 0 or screen.get_at((int(x+J/2),int(y+J/2)))[1] == 0 or screen.get_at((int(x+J/2),int(y+J/2)))[2] == 0:
            # center
              
            screen.set_at((int(x+J/2),int(y+J/2)), (int(B1+B2+B3+B4)/4,int(B1+B2+B3+B4)/4,255))
        
                

            # north
            if screen.get_at((int(x+J/2),int(y)))[0] == 0:
                
                screen.set_at((int(x+J/2),int(y)), (int(B1+B2)/2,int(B1+B2)/2,255))
            else:
                # mean of north and center
                screen.set_at((int(x+J/2),int(y)), (int(B1+B2+B3+B4)/4,int(B1+B2+B3+B4)/4,255))
                

            # south
            if screen.get_at((int(x+J/2),int(y+J)))[0] == 0:
               
                screen.set_at((int(x+J/2),int(y+J)), (int(B3+B4)/2,int(B3+B4)/2,255))
            else:
                # mean of south and center
                screen.set_at((int(x+J/2),int(y+J)), (int(B1+B2+B3+B4)/4,int(B1+B2+B3+B4)/4,255))

            # west
            if screen.get_at((int(x),int(y+J/2)))[0] == 0:
               
                screen.set_at((int(x),int(y+J/2)), (int((B1+B3))/2,int((B1+B3))/2,255))
            else:
                # mean of west and center
                screen.set_at((int(x),int(y+J/2)), (int((B1+B2+B3+B4))/4,int(B1+B2+B3+B4)/4,255))


            # east
            if screen.get_at((int(x+J),int(y+J/2)))[0] == 0:
              
                screen.set_at((int(x+J),int(y+J/2)), (int(B2+B4)/2,int(B2+B4)/2,255))
            else:
                # mean of east and center
                 screen.set_at((int(x+J),int(y+J/2)), (int(B1+B2+B3+B4)/4,int(B1+B2+B3+B4)/4,255))

            x = x + J
        y = y + J
    J = J / 2

pygame.display.flip()


# wait for user to close window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


