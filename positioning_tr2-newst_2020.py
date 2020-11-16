import pyautogui
from PIL import ImageGrab, ImageOps, Image
import pygame
from numpy import *
import keyboard



import time
from pygame import Surface
from polaricity import roots_of_complex_number
screena = pygame.display.set_mode((600, 800))
class application:
    def __init__(self):
        #savfed as rect (xpos start, ypos start, x positipon end, yposition end)
        self.range_of_image=None
        self.center_of_image_x=0
        self.center_of_image_y=0
        self.center_of_monitor_x=50
        self.center_of_monitor_y=50
        self.running_image=None
        self.x_dif=0
        self.y_dif=0
        self.rmin_move=0
        self.rmax_move=0
        self.gmin_move=0
        self.gmax_move=0
        self.bmin_move=0
        self.bmax_move=0

        self.rmin_click=0
        self.rmax_click=0
        self.gmin_click=0
        self.gmax_click=0
        self.bmin_click=0
        self.bmax_click=0

        self.lastpos_x=0
        self.lastpos_y=0
        self.looking=False
        self.wrong_times=0


#sets where to gram image from
    def set_range_of_image(self):
        # grabs center by position of mouse
        x, y = pyautogui.position()
        self.range_of_image = (x - 100, y - 100, x + 100, y + 100)
        self.center_of_image_x=x
        self.center_of_image_y=y
        self.lastpos_x=x
        self.lastpos_y=y


#shows the image we analyze on monitor
    def show_running_image(self,screen):
        im = ImageGrab.grab(self.range_of_image)
        im.save("im.jpg")
        self.running_image=pygame.image.load("im.jpg")
        screen.blit(self.running_image,(50,50))

    def standartize_to_monitor(self):
        self.x_dif=self.center_of_image_x-self.center_of_monitor_x
        self.y_dif = self.center_of_image_y - self.center_of_monitor_y

#show central circle on monitor
    def show_circle_on_monitor(self,screena):
        x, y = pyautogui.position()
        pygame.draw.circle(screena,(255,0,0),(x-self.x_dif,y-self.y_dif),5,5)
#set color to move mouse
    def set_color(self):
        image = ImageGrab.grab((self.center_of_image_x-5, self.center_of_image_y-5, self.center_of_image_x+5, self.center_of_image_y+5))
        pygame.draw.circle(screena, (255, 255, 0),(self.center_of_monitor_y,self.center_of_monitor_y),10,2)
        array_of_colors = array(image.getcolors())

        rmax_move=0
        rmin_move=256
        gmax_move=0
        gmin_move=256
        bmax_move=0
        bmin_move=256
        for item in array_of_colors:
            #item[0]=number of times
            #item[1]=array
            #item[1][0]=r value
            if item[1][0]>rmax_move:
                rmax_move=item[1][0]
            if item[1][0]<rmin_move:
                rmin_move=item[1][0]
            if item[1][1]>gmax_move:
                gmax_move=item[1][1]
            if item[1][1]<gmin_move:
                gmin_move=item[1][1]
            if item[1][2]>bmax_move:
                bmax_move=item[1][2]
            if item[1][2]<bmin_move:
                bmin_move=item[1][2]
        self.rmax_move=rmax_move+50
        self.rmin_move=rmin_move-50
        self.gmax_move=gmax_move+25
        self.gmin_move=gmin_move-25
        self.bmax_move=bmax_move+25
        self.bmin_move=bmin_move-25

#set color to click on mouse
    def set_click(self):
        image = ImageGrab.grab((self.center_of_image_x-5, self.center_of_image_y-5, self.center_of_image_x+5, self.center_of_image_y+5))
        pygame.draw.circle(screena, (255, 0, 255),(self.center_of_monitor_y,self.center_of_monitor_y),10,2)
        array_of_colors = array(image.getcolors())

        rmax_click=0
        rmin_click=256
        gmax_click=0
        gmin_click=256
        bmax_click=0
        bmin_click=256
        for item in array_of_colors:
            #item[0]=number of times
            #item[1]=array
            #item[1][0]=r value
            if item[1][0]>rmax_click:
                rmax_click=item[1][0]
            if item[1][0]<rmin_click:
                rmin_click=item[1][0]
            if item[1][1]>gmax_click:
                gmax_click=item[1][1]
            if item[1][1]<gmin_click:
                gmin_click=item[1][1]
            if item[1][2]>bmax_click:
                bmax_click=item[1][2]
            if item[1][2]<bmin_click:
                bmin_click=item[1][2]
        self.rmax_click=rmax_click+10
        self.rmin_click=rmin_click-10
        self.gmax_click=gmax_click+10
        self.gmin_click=gmin_click-10
        self.bmax_click=bmax_click+10
        self.bmin_click=bmin_click-10

#instructions to make, depending on keyboard pressed
    def set_monitor(self, keyboard_pressed):
            if keyboard_pressed('a'):
                self.center_of_monitor_x -= 5
            if keyboard_pressed('d'):
                self.center_of_monitor_x += 5
            if keyboard_pressed('w'):
                self.center_of_monitor_y -= 5
            if keyboard_pressed('x'):
                self.center_of_monitor_y += 5
            if keyboard.is_pressed('t'):
                self.set_color()
            if keyboard.is_pressed('s'):
                self.standartize_to_monitor()
                print("x center position of image is " + str(self.center_of_image_x))
                print("y center position of image is " + str(self.center_of_image_x))

                print("x center position of monitor is " + str(self.center_of_monitor_x))
                print("y center position of monitor is " + str(self.center_of_monitor_y))
                print("x dif is" + str(self.x_dif))
                print("y dif is" + str(self.y_dif))
            if keyboard.is_pressed('l'):
                info.set_click()

            if keyboard.is_pressed('g'):
                self.show_circle_on_monitor(screena)
            if keyboard.is_pressed('n'):
                image_to_analyze(self.range_of_image[0],self.range_of_image[1],self.range_of_image[2],self.range_of_image[3],self.x_dif,self.y_dif)
                #print(str(self.range_of_image)+"----------------")

info=application()


def image_225_pix(x_to_start, y_to_start, x_diff, y_diff):

    image = ImageGrab.grab((x_to_start, y_to_start, x_to_start + 10, y_to_start + 7))

    # needs t o ttandartize
    pygame.draw.circle(screena, (255, 0, 0), (x_to_start + 7 - x_diff, y_to_start + 10 - y_diff), 7,
                       1)  # add difference to x and y

    array_of_colors = array(image.getcolors())

    # array_of_colors= [ [ number of items that -, (tuple of colors) ] .... ]
    for item in array_of_colors:
        print(item)
        print(str(info.rmax_move)+"rmax")
        print(str(info.rmin_move)+"rmin")
        print(str(info.gmax_move)+"gmax")
        print(str(info.gmin_move)+"gmin")
        print(str(info.bmax_move)+"bmax")
        print(str(info.bmin_move)+"bmin")



        #print(item)
        if  info.rmin_move<item[1][0]<info.rmax_move and info.gmin_move<item[1][1]<info.gmax_move and info.bmin_move<item[1][2]<info.bmax_move:
            pygame.draw.circle(screena, (0, 0, 255), (x_to_start + 7 - x_diff, y_to_start + 7 - y_diff), 7, 1)

            x, y = pyautogui.position()
            move_on_x = (x_to_start - info.center_of_image_x)
            move_on_y = (y_to_start - info.center_of_image_y)
            pyautogui.moveTo(move_on_x + x, move_on_y + y)
            info.lastpos_x=x_to_start
            info.lastpos_y=y_to_start

            return True
        if info.rmin_click < item[1][0] < info.rmax_click and info.gmin_click < item[1][
            1] < info.gmax_click and info.bmin_click < item[1][2] < info.bmax_click:
            pygame.draw.circle(screena, (0, 0, 255), (x_to_start + 7 - x_diff, y_to_start + 7 - y_diff), 7, 1)
            pyautogui.click()

            return True






            # else:
            # print("not red")
            # else:
            # print("not red")


def image_to_analyze(left, top, right, bottom, x_diff, y_diff):
    pygame.display.flip()
    image_size_x = right - left
    image_size_y = bottom - top
##algorithm to place a new
    still_looking=True


    radius=5
    while still_looking:
        #need to standartize to zero pos
        list_of_positions=roots_of_complex_number(radius)
        for position in list_of_positions:
            a=image_225_pix(position[0]+info.lastpos_x, position[1]+info.lastpos_y, x_diff, y_diff)


            pygame.display.flip()

            if a:
                pygame.time.wait(100)
                still_looking=False
                return

        if info.wrong_times>3:
            info.lastpos_y=info.center_of_image_y
            info.lastpos_x=info.center_of_image_x
            info.wrong_times=0
        else:
            info.wrong_times+=1




        radius+=20
        if radius>=80:
            still_looking=False


running = True
show_circle=True
while running:
    screena.fill([0,0,0])
    info.show_running_image(screena)
    if keyboard.is_pressed('m'):
        info.looking = True
    if keyboard.is_pressed('o'):
        info.looking = False

    if info.looking:
        image_to_analyze(info.range_of_image[0], info.range_of_image[1], info.range_of_image[2], info.range_of_image[3],
                         info.x_dif, info.y_dif)

    for event in pygame.event.get():
        if keyboard.is_pressed('y'):
            running=False
        if keyboard.is_pressed('p'):
            info.set_range_of_image()


        #set up monitor with keyboard
        if keyboard.is_pressed('a'):
            info.set_monitor(keyboard.is_pressed)
        if keyboard.is_pressed('w'):
            info.set_monitor(keyboard.is_pressed)
        if keyboard.is_pressed('d'):
            info.set_monitor(keyboard.is_pressed)
        if keyboard.is_pressed('x'):
            info.set_monitor(keyboard.is_pressed)
        if keyboard.is_pressed('s'):
            info.set_monitor(keyboard.is_pressed)
        if keyboard.is_pressed('g'):
            info.set_monitor(keyboard.is_pressed)
        if keyboard.is_pressed('n'):
            info.set_monitor(keyboard.is_pressed)
        if keyboard.is_pressed('t'):
            info.set_monitor(keyboard.is_pressed)
        if keyboard.is_pressed('l'):
            info.set_monitor(keyboard.is_pressed)




        if keyboard.is_pressed('z'):
            if show_circle==True:
                show_circle=False
            else:
                show_circle=True

    if show_circle:
        pygame.draw.circle(screena,(255,0,0),(info.center_of_monitor_x,info.center_of_monitor_y),10,10)
        pygame.draw.circle(screena,(255,0,0),(info.center_of_monitor_x,info.center_of_monitor_y),30,2)

    pygame.display.flip()


"""
  if event.type == pygame.KEYDOWN:
            info.set_monitor(keyboard.is_pressed)

"""


