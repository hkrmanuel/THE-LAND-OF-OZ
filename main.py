import pygame
import os
import pygame
from pyvidplayer import Video
import csv
import load_images
import hero_class
import enemy_class
import uidisplay



os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

# Set Window Size
info = pygame.display.Info()

screen_width, screen_height = info.current_w, info.current_h
win = pygame.display.set_mode((screen_width - 10, screen_height - 30), pygame.RESIZABLE)

pygame.display.set_caption("Land Of Oz")
clock = pygame.time.Clock()


#Choosing Player Function


FPS = 17
scroll = 0

width = 400 
height = 400
e_width = 310
e_height = 310

idlemove =0
jumpmove =0
attackmove = 0
         
#Function for all the stuff displayed on the window
def redrawwindow():
 
    # Scrolling function when player moves
    for x in range(5):
        speed = 1
        for bg_image in load_images.bgimages_scaled:
            offset = (x * load_images.bg_width - scroll * speed)
            if offset < -load_images.bg_width:
                offset += load_images.bg_width
            win.blit(bg_image, (offset, 0))
            speed += 0.2
        
    Golem.ai(win)    
    heroes.logic(win)
    
    
    pygame.display.update()

heroes = hero_class.hero(300, 460, 128,128)
Golem = enemy_class.Enemy(2000, 510, 300, 300)

#Button Variables

run = True

#Text On Window Functions

"This is a list of fonts used"
adventure = pygame.font .SysFont("Adventure", 60)

def txt(text, font, txt_color, x, y ):
    word = font.render(text, True, txt_color)
    win.blit(word, (x,y))


def intro():

    vid = Video("C:/Users/hkrma/OneDrive/Documents/PROGRAMMING/python/THE LAND OF OZ/land_of_oz_intro.mov")
    vid.set_size((900, 900))
    scr = pygame.display.set_mode((700, 500))
    
    intro_timer = 0
 
        
    while True:
        
        
        vid.draw(scr, (-110, -205))
        
        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                vid.close()
            if event.type == pygame.MOUSEBUTTONDOWN:
                vid.close()
                scr =  pygame.display.set_mode((screen_width - 10, screen_height - 30), pygame.RESIZABLE)
                select_player()
            
                       
    pygame.quit()

def select_player():
    global run
    global select

    
   
    
    while run:
        
        for event in pygame.event.get():  # quit option
                if event.type == pygame.QUIT:
                    run = False
        win.blit(uidisplay.bg_scaled[0], (0,0))
        win.blit(pygame.transform.scale(uidisplay.board, (1500, 1500)),(0,-220))
        txt("SELECT PLAYER", adventure, (255, 225, 0), 550, 300)
        if uidisplay.char1.drawbutton(win):
            play()
            
         
        if uidisplay.char2.drawbutton(win):
            play()
        
            
        if uidisplay.char3.drawbutton(win):
            play()
                        
        pygame.display.update()
        
         
                
                
        
def play():
    global run
         
    while run:
        clock.tick(FPS)  # frames per second

        for event in pygame.event.get():  # quit option
            if event.type == pygame.QUIT:
                run = False
        

        redrawwindow()

    pygame.quit()
    
intro()

