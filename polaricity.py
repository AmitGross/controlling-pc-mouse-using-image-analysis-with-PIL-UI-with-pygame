import pyautogui
from PIL import ImageGrab, ImageOps, Image
import pygame
from numpy import *
import keyboard
screena = pygame.display.set_mode((600, 800))
import math
running = False





def roots_of_complex_number(radius):
    #seems a good proportion..
    n=int(radius*1/5)
    ##will contaion n values...
    list_of_radians=[]
    for i in range(0,n):
        root= (2*math.pi*i)/n
        list_of_radians.append(root)
    #print(list_of_radians)
    list_of_positions=[]
    for radian in list_of_radians:
        list_of_positions.append(turn_rad_to_position(radian,radius))
    #print(list_of_positions)
    return list_of_positions
def turn_rad_to_position(rad,radius):
    return (int(math.cos(rad)*radius),int(math.sin(rad)*radius))





def draw_circle_of_roots(radius):
    to_draw = roots_of_complex_number(radius)
    for i in to_draw:
        pygame.draw.circle(screena, (255, 0, 0), (i[0] + 200, i[1] + 200), 2, 2)





v=5
while running:
    draw_circle_of_roots(v)
    #screena.fill([0,0,0])
    for event in pygame.event.get():

        if keyboard.is_pressed('p'):
            pass

    pygame.display.flip()
    pygame.time.delay(1000)

    v+=15




