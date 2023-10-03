import load_images
import pygame

info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h

class Button():
    def __init__(self, x, y, image, scale):
        s_width = image.get_width()
        s_height = image.get_height()
        self.image = pygame.transform.scale(image, (int(s_width * scale), int(s_height * scale)))
        self.rect =self.image.get_rect ()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.select = False
    
    def drawbutton(self, win):
        action = False
        pos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and self.clicked == False:
                self.clicked = True
                self.select = True
                action = True
            
        
        if pygame.mouse.get_pressed()[0]== 0:
            self.clicked = False                
                     
        win.blit(self.image, (self.rect.x, self.rect.y))
        
         
        return action



board = pygame.image.load("../THE LAND OF OZ/wooden-gold-buttons-ui-game/wooden_board.png")
Rogue = pygame.image.load("../THE LAND OF OZ/heroes/PNG/Rogue/rogue.png")
Knight =pygame.image.load("../THE LAND OF OZ/heroes/PNG/Knight/knight.png")
Mage= pygame.image.load("../THE LAND OF OZ/heroes/PNG/Mage/mage.png")
bg = [pygame.image.load("../THE LAND OF OZ/forest background/PNG/Cartoon_Forest_BG_02/bg2.png")]
bg_scaled = [pygame.transform.scale(img, (screen_width, screen_height)) for img in bg]

select = 0

Rogue = pygame.image.load("../THE LAND OF OZ/heroes/PNG/Rogue/rogue.png")
Knight =pygame.image.load("../THE LAND OF OZ/heroes/PNG/Knight/knight.png")
Mage= pygame.image.load("../THE LAND OF OZ/heroes/PNG/Mage/mage.png")

char1 = Button(400, 350, Rogue, 2.4)
char2 = Button(620, 350, Knight,2.4)
char3 = Button(850, 350, Mage, 2.4)
