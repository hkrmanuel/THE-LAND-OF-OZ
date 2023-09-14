import pygame
import os
import pygame
from pyvidplayer import Video
import csv





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


#background image and settings
bg_images = []
for i in range(1, 6):
    bg_image = pygame.image.load(f"../THE LAND OF OZ/forest background/PNG/Cartoon_Forest_BG_01/Layers/plx{i}.png").convert_alpha()
    bg_images.append(bg_image)
    
bg_images_scaled = [pygame.transform.scale(img, (screen_width, screen_height)) for img in bg_images]
bg_width = bg_images_scaled[0].get_width()

#Enemy Images and Settings



idlemove =0
jumpmove =0
attackmove = 0


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



#Character Selection Buttons 
board = pygame.image.load("../THE LAND OF OZ/wooden-gold-buttons-ui-game/wooden_board.png")
Rogue = pygame.image.load("../THE LAND OF OZ/heroes/PNG/Rogue/rogue.png")
Knight =pygame.image.load("../THE LAND OF OZ/heroes/PNG/Knight/knight.png")
Mage= pygame.image.load("../THE LAND OF OZ/heroes/PNG/Mage/mage.png")
bg = [pygame.image.load("../THE LAND OF OZ/forest background/PNG/Cartoon_Forest_BG_02/bg2.png")]
bg_scaled = [pygame.transform.scale(img, (screen_width, screen_height)) for img in bg]
select = 0

char1 = Button(400, 350, Rogue, 2.4)
char2 = Button(620, 350, Knight,2.4)
char3 = Button(850, 350, Mage, 2.4)


        
#Hero images and settings
walkright =[]
for i in range(1, 6):
        w = pygame.image.load(f"../THE LAND OF OZ/heroes/PNG/Rogue/Walk/walk{i}.png").convert_alpha()
        walkright.append(w) 

    
walkright_scaled = [pygame.transform.scale(img, (width, height)) for img in walkright]  
walkleft =[]
for i in range(1, 6):
    w = pygame.image.load(f"../THE LAND OF OZ/heroes/PNG/Rogue/Walk/walk{i}L.png").convert_alpha()
    walkleft.append(w) 

walkleft_scaled = [pygame.transform.scale(img, (width, height)) for img in walkleft]  

runright = []
for i in range(1, 9):
    run = pygame.image.load(f"../THE LAND OF OZ/heroes/PNG/Rogue/Run/run{i}.png").convert_alpha()
    runright.append(run)

runright_scaled = [pygame.transform.scale(img, (width, height)) for img in runright]  

runleft =[]
for i in range(1, 9):
    run = pygame.image.load(f"../THE LAND OF OZ/heroes/PNG/Rogue/Run/run{i}L.png").convert_alpha()
    runleft.append(run)
runleft_scaled = [pygame.transform.scale(img, (width, height)) for img in runleft]  

idle = [] 
for i in range(1, 18):
    id = pygame.image.load(f"../THE LAND OF OZ/heroes/PNG/Rogue/Idle/idle{i}.png").convert_alpha()
    idle.append(id)


idle_scaled = [pygame.transform.scale(img, (width, height)) for img in idle] 
jumpright = []

for i in range(1,8):
    jum = pygame.image.load(f"../THE LAND OF OZ/heroes/PNG/Rogue/Jump/jump{i}.png").convert_alpha()
    jumpright.append(jum) 
jumpright_scaled = [pygame.transform.scale(img, (width, height)) for img in jumpright]

jumpleft = []
for i in range(1,8):
    jum = pygame.image.load(f"../THE LAND OF OZ/heroes/PNG/Rogue/Jump/jump{i}L.png").convert_alpha()
    jumpleft.append(jum) 

jumpleft_scaled = [pygame.transform.scale(img, (width, height)) for img in jumpleft]

highjumpright =[] 
for i in range(1, 12):
    jum =pygame.image.load(f"../THE LAND OF OZ/heroes/PNG/Rogue/High_Jump/high_jump{i}.png").convert_alpha()
    highjumpright.append(jum)
highjumpright_scaled = [pygame.transform.scale(img, (width, height)) for img in highjumpright]

highjumpleft =[]
for i in range(1, 12):
    jum =pygame.image.load(f"../THE LAND OF OZ/heroes/PNG/Rogue/High_Jump/high_jump{i}L.png").convert_alpha()
    highjumpleft.append(jum)
highjumpleft_scaled = [pygame.transform.scale(img, (width, height)) for img in highjumpleft]

attack =[]
for i in range(1, 8):
    atk = pygame.image.load(f"../THE LAND OF OZ/heroes/PNG/Rogue/Attack/Attack{i}.png").convert_alpha()
    attack.append(atk)
attack_scaled = [pygame.transform.scale(img, (width, height)) for img in attack]
attackleft = []
for i in range(1, 8):
    atk = pygame.image.load(f"../THE LAND OF OZ/heroes/PNG/Rogue/Attack/Attack{i}L.png").convert_alpha()
    attackleft.append(atk)
attackleft_scaled = [pygame.transform.scale(img, (width, height)) for img in attackleft]
attackwalk=[]
for i in range(1, 7):
    atk = pygame.image.load(f"../THE LAND OF OZ/heroes/PNG/Rogue/Walk_Attack/walk_attack{i}.png").convert_alpha()
    attackwalk.append(atk)
attackwalk_scaled = [pygame.transform.scale(img, (width, height)) for img in attackwalk]
attackwalkleft =[]
for i in range(1, 7):
    atk = pygame.image.load(f"../THE LAND OF OZ/heroes/PNG/Rogue/Walk_Attack/walk_attack{i}L.png").convert_alpha()
    attackwalkleft.append(atk)
attackwalkleft_scaled = [pygame.transform.scale(img, (width, height)) for img in attackwalkleft]
attackrun =[]
for i in range(1, 8):
    atk = pygame.image.load(f"../THE LAND OF OZ/heroes/PNG/Rogue/Run_Attack/run_attack{i}.png").convert_alpha()
    attackrun.append(atk)
attackrun_scaled = [pygame.transform.scale(img, (width, height)) for img in attackrun]
attackrunleft =[]
for i in range(1, 8):
    atk = pygame.image.load(f"../THE LAND OF OZ/heroes/PNG/Rogue/Run_Attack/run_attack{i}L.png").convert_alpha()
    attackrunleft.append(atk)
attackrunleft_scaled = [pygame.transform.scale(img, (width, height)) for img in attackrunleft]

#Enemy Sprites And Animations       
#GOlem Enemy 1
Golem_idle = []
for i in range(1, 9):
    idl = pygame.image.load(f"../THE LAND OF OZ/Golem enemy/PNG/Golem_03/PNG Sequences/Idle/Golem_03_Idle_00{i}.png").convert_alpha()
    Golem_idle.append(idl)
for i in range(10, 12):
    idl = pygame.image.load(f"../THE LAND OF OZ/Golem enemy/PNG/Golem_03/PNG Sequences/Idle/Golem_03_Idle_0{i}.png").convert_alpha()
    Golem_idle.append(idl)
Golem_idle_scaled = [pygame.transform.scale(img, (e_width, e_height)) for img in Golem_idle]

Golem_Attack = []
for i in range(0, 10):
    idl = pygame.image.load(f"../THE LAND OF OZ/Golem enemy/PNG/Golem_03/PNG Sequences/Attacking/Golem_03_Attacking_00{i}.png").convert_alpha()
    Golem_Attack.append(idl)
for i in range(10, 12):
    idl = pygame.image.load(f"../THE LAND OF OZ/Golem enemy/PNG/Golem_03/PNG Sequences/Attacking/Golem_03_Attacking_0{i}.png").convert_alpha()
    Golem_Attack.append(idl)
Golem_Attack_scaled = [pygame.transform.scale(img, (e_width, e_height)) for img in Golem_Attack]

Golem_Attackleft = []
for i in range(0, 10):
    idl = pygame.image.load(f"../THE LAND OF OZ/Golem enemy/PNG/Golem_03/PNG Sequences/Attacking/Golem_03_Attacking_00{i}L.png").convert_alpha()
    Golem_Attackleft.append(idl)
for i in range(10, 12):
    idl = pygame.image.load(f"../THE LAND OF OZ/Golem enemy/PNG/Golem_03/PNG Sequences/Attacking/Golem_03_Attacking_0{i}L.png").convert_alpha()
    Golem_Attackleft.append(idl)
Golem_Attackleft_scaled = [pygame.transform.scale(img, (e_width, e_height)) for img in Golem_Attackleft]

Golem_hurt =[]
for i in range(0, 9):
    idl = pygame.image.load(f"../THE LAND OF OZ/Golem enemy/PNG/Golem_03/PNG Sequences/Hurt/Golem_03_Hurt_00{i}.png").convert_alpha()
    Golem_hurt.append(idl)
for i in range(10, 12):
    idl = pygame.image.load(f"../THE LAND OF OZ/Golem enemy/PNG/Golem_03/PNG Sequences/Hurt/Golem_03_Hurt_0{i}.png").convert_alpha()
    Golem_hurt.append(idl)
Golem_hurt_scaled = [pygame.transform.scale(img, (e_width, e_height)) for img in Golem_hurt]

Golem_hurtleft = []
for i in range(0, 9):
    idl = pygame.image.load(f"../THE LAND OF OZ/Golem enemy/PNG/Golem_03/PNG Sequences/Hurt/Golem_03_Hurt_00{i}L.png").convert_alpha()
    Golem_hurtleft.append(idl)
for i in range(10, 12):
    idl = pygame.image.load(f"../THE LAND OF OZ/Golem enemy/PNG/Golem_03/PNG Sequences/Hurt/Golem_03_Hurt_0{i}L.png").convert_alpha()
    Golem_hurtleft.append(idl)
Golem_hurtleft_scaled = [pygame.transform.scale(img, (e_width, e_height)) for img in Golem_hurtleft]

Golem_dying =[]
for i in range(0, 9):
    idl = pygame.image.load(f"../THE LAND OF OZ/Golem enemy/PNG/Golem_03/PNG Sequences/Dying/Golem_03_Dying_00{i}.png").convert_alpha()
    Golem_dying.append(idl)
for i in range(10, 15):
    idl = pygame.image.load(f"../THE LAND OF OZ/Golem enemy/PNG/Golem_03/PNG Sequences/Dying/Golem_03_Dying_0{i}.png").convert_alpha()
    Golem_dying.append(idl)
Golem_dying_scaled = [pygame.transform.scale(img, (e_width, e_height)) for img in Golem_dying]

Golem_dyingleft =[]
for i in range(0, 9):
    idl = pygame.image.load(f"../THE LAND OF OZ/Golem enemy/PNG/Golem_03/PNG Sequences/Dying/Golem_03_Dying_00{i}L.png").convert_alpha()
    Golem_dyingleft.append(idl)
for i in range(10, 15):
    idl = pygame.image.load(f"../THE LAND OF OZ/Golem enemy/PNG/Golem_03/PNG Sequences/Dying/Golem_03_Dying_0{i}L.png").convert_alpha()
    Golem_dyingleft.append(idl)
Golem_dyingleft_scaled = [pygame.transform.scale(img, (e_width, e_height)) for img in Golem_dyingleft]


Golem_walking = []
for i in range(0, 9):
    idl = pygame.image.load(f"../THE LAND OF OZ/Golem enemy/PNG/Golem_03/PNG Sequences/Walking/Golem_03_Walking_00{i}.png").convert_alpha()
    Golem_walking.append(idl)
for i in range(10, 18):
    idl = pygame.image.load(f"../THE LAND OF OZ/Golem enemy/PNG/Golem_03/PNG Sequences/Walking/Golem_03_Walking_0{i}.png").convert_alpha()
    Golem_walking.append(idl)
Golem_walking_scaled = [pygame.transform.scale(img, (e_width,e_height)) for img in Golem_walking]

Golem_walkingleft = []
for i in range(0, 9):
    idl = pygame.image.load(f"../THE LAND OF OZ/Golem enemy/PNG/Golem_03/PNG Sequences/Walking/Golem_03_Walking_00{i}L.png").convert_alpha()
    Golem_walkingleft.append(idl)
for i in range(10, 18):
    idl = pygame.image.load(f"../THE LAND OF OZ/Golem enemy/PNG/Golem_03/PNG Sequences/Walking/Golem_03_Walking_0{i}L.png").convert_alpha()
    Golem_walkingleft.append(idl)
Golem_walkingleft_scaled = [pygame.transform.scale(img, (e_width, e_width)) for img in Golem_walkingleft]

Golem_taunt = []
for i in range(0, 9):
    idl = pygame.image.load(f"../THE LAND OF OZ/Golem enemy/PNG/Golem_03/PNG Sequences/Taunt/Golem_03_Taunt_00{i}.png").convert_alpha()
    Golem_taunt.append(idl) 
for i in range(10, 17):
    idl = pygame.image.load(f"../THE LAND OF OZ/Golem enemy/PNG/Golem_03/PNG Sequences/Taunt/Golem_03_Taunt_0{i}.png").convert_alpha()
    Golem_taunt.append(idl) 
Golem_taunt_scaled = [pygame.transform.scale(img, (e_width, e_width)) for img in Golem_taunt]

Golem_tauntleft =[]
for i in range(0, 9):
    idl = pygame.image.load(f"../THE LAND OF OZ/Golem enemy/PNG/Golem_03/PNG Sequences/Taunt/Golem_03_Taunt_00{i}L.png").convert_alpha()
    Golem_tauntleft.append(idl) 
for i in range(10, 17):
    idl = pygame.image.load(f"../THE LAND OF OZ/Golem enemy/PNG/Golem_03/PNG Sequences/Taunt/Golem_03_Taunt_0{i}L.png").convert_alpha()
    Golem_tauntleft.append(idl) 
Golem_tauntleft_scaled = [pygame.transform.scale(img, (e_width, e_width)) for img in Golem_tauntleft]


class hero():
    def __init__(self, x, y, width, height):
        self.x =x
        self.y = y
        self.height = height
        self.width =width
        self.vel = 10
        self.left = False
        self.right = False
        self.walkcount = 0  
        self.jump_on = False
        self.jumpcount = 10
        self.standing = True
        self.hitbox = (self.x + 70, self.y + 200 , width - 270, height - 250)
        self.atkdec = (self.x + 70, self.y + 200 , width - 270, height - 250)
        self.visible = True
        self.run =0
        self.highjump =0
        self.attack = False
        self.attackl = False
        self.atk = False
        self.taunt = 0
        
        
        
        
        
        
    # Hero Controls For Movement
    def controls(self,win):
        global scroll
        global jumpmove
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and scroll > 0 and self.run == 0:
            scroll -= 20
            self.x -= self.vel
            self.left = True
            self.right = False
            self.standing = False
        elif keys[pygame.K_RIGHT] and scroll < 3000 and self.run == 0:
            scroll += 20
            self.x += self.vel
            self.left = False
            self.right = True
            self.standing = False
        else:
            self.standing = True
            self.left = False
            self.right = False
        
        if keys[pygame.K_LSHIFT]:
            if self.run == 0:
                self.run = 1
            else:
                self.run = 0

        if keys[pygame.K_RIGHT] and self.run== 1 and scroll < 3000:
            self.vel = 12
            scroll += 25
            self.x += self.vel
            self.left = False
            self.right = True
            self.standing = False
            
        if keys[pygame.K_LEFT] and self.run== 1 and scroll > 0:
            self.vel = 12
            scroll -= 25
            self.x -= self.vel
            self.left = True
            self.right = False
            self.standing = False

        if not self.jump_on:
            if keys[pygame.K_UP]:
                if self.highjump == 0:
                    self.highjump = 1
                else:
                    self.highjump == 0
                    
                self.jump_on = True
        else:
            if self.jumpcount >= -10:
                fall = 2
                if self.jumpcount < 0:
                    fall = -2
                self.y -= (self.jumpcount ** 2) * 0.4 * fall
                self.jumpcount -= 1
            else:
                self.jump_on = False
                self.jumpcount = 10

        
        
        
          #high jump 
                
        if not self.jump_on:
            if keys[pygame.K_UP]:
                if self.highjump == 0:
                    self.highjump = 1
                else:
                    self.highjump == 0
                    
                self.jump_on = True
        elif self.jump_on and self.run == 1:
            if self.jumpcount >= -10:
                fall = 2
                if self.jumpcount < 0:
                    fall = -2
                self.y -= (self.jumpcount ** 2) * 0.7 * fall
                self.jumpcount -= 1
            else:
                self.jump_on = False
                self.jumpcount = 10
        if keys[pygame.K_SPACE]:
            self.atk = True
            self.left = False
            self.right = False
            self.standing = False
            self.attackl = False
            self.attack = False
                
        if keys[pygame.K_RIGHT ]and keys[pygame.K_SPACE] :
                self.attack = True
                self.left = False
                self.right = False
                self.standing = False 
                self.atk = False
                self.attackl = False
                
        elif keys[pygame.K_LEFT ]and keys[pygame.K_SPACE] :
            
                self.left = False
                self.right = False
                self.standing = False
                self.attack = False
                self.attackl = True
                self.atk=False
        elif keys[pygame.K_UP] and keys[pygame.K_SPACE]:
                self.jump_on = True
                self.standing = True     
                self.attack = False
                self.attackl = False
                self.atk = False
                self.left = False
                self.right= False
       
       
              
    def drawchar(self, win):
        global idlemove
        global jumpmove
        global attackmove
        if self.visible:
            if not self.standing:
                if self.walkcount + 1 >= FPS:
                    self.walkcount = 0

                if self.left and self.jump_on == False and self.run == 0:
                    
                    if self.walkcount // 3 >= len(walkleft):
                        self.walkcount = 0
                    win.blit(walkleft_scaled[self.walkcount // 3], (self.x, self.y))
                    self.walkcount += 1
                    
                
                elif self.left and self.run == 1 and self.jump_on == False :
                    
                    if self.walkcount // 2 >= len(runleft):
                        self.walkcount = 0
                    win.blit(runleft_scaled[self.walkcount // 2], (self.x, self.y))
                    self.walkcount += 1
                    
                elif self.right and self.jump_on == False and self.run == 0:
                
                    if self.walkcount // 2 >= len(walkright):
                        self.walkcount = 0
                    win.blit(walkright_scaled[self.walkcount // 2], (self.x, self.y))
                    self.walkcount += 1
                 
                elif self.right and self.run == 1 and self.jump_on == False :
                    if self.walkcount // 2 >= len(runright):
                        self.walkcount = 0
                    win.blit(runright_scaled[self.walkcount // 2], (self.x, self.y))
                    self.walkcount += 1
                else:
                    self.standing = True
                    
                if self.jump_on:
                    if self.right and self.run == 0 or self.attack:
                        self.standing = False
                        self.left = False
                        if jumpmove >= len(jumpright_scaled):
                            jumpmove = 0
                        win.blit(jumpright_scaled[jumpmove], (self.x, self.y))
                        jumpmove += 1
                    elif self.left and self.run ==0 or self.attackl:
                        self.standing = False
                        self.right = False
                        if jumpmove >= len(jumpleft_scaled):
                            jumpmove = 0
                        win.blit(jumpleft_scaled[jumpmove], (self.x, self.y))
                        jumpmove += 1
                
                else:
                    self.standing = True
                
                if self.jump_on and self.run == 1: 
          
                    if self.right and self.run == 1:
                        self.standing = False
                        self.left = False
                        if jumpmove >= len(highjumpright_scaled):
                            jumpmove = 0
                        win.blit(highjumpright_scaled[jumpmove], (self.x, self.y))
                        jumpmove += 1
                    elif self.left and self.run == 1:
                        self.standing = False
                        self.right = False
                        if jumpmove >= len(highjumpleft_scaled):
                            jumpmove = 0
                        win.blit(highjumpleft_scaled[jumpmove], (self.x, self.y))
                        jumpmove += 1
                    else:
                        self.standing = True
                        
                if self.attack and not(self.jump_on) and not(self.left) and not(self.right) and self.run == 0:
                    if attackmove >= len(attackwalk):
                        attackmove = 0
                    win.blit(attackwalk_scaled[attackmove], (self.x, self.y))
                    attackmove += 1
                if self.attackl and not(self.jump_on) and not(self.left) and not(self.right) and self.run ==0:
                    if attackmove >= len(attackwalkleft):
                        attackmove = 0
                    win.blit(attackwalkleft_scaled[attackmove], (self.x, self.y))
                    attackmove += 1
                    
                    #Running Attack
                if self.attack and not(self.jump_on) and not(self.left) and not(self.right) and self.run == 1:
                    if attackmove >= len(attackrun):
                        attackmove = 0
                    win.blit(attackrun_scaled[attackmove], (self.x, self.y))
                    attackmove += 1
                if self.attackl and not(self.jump_on) and not(self.left) and not(self.right) and self.run == 1:
                    if attackmove >= len(attackrunleft):
                        attackmove = 0
                    win.blit(attackrunleft_scaled[attackmove], (self.x, self.y))
                    attackmove += 1
                if self.atk and not(self.jump_on) and not(self.left) and not(self.right):
                    if attackmove >= len(attack):
                        attackmove = 0
                    win.blit(attack_scaled[attackmove], (self.x, self.y))
                    attackmove += 1
              

            else:
                if self.right == False and self.left == False and self.standing ==True:
                    if idlemove >= len(idle):
                        idlemove = 0
                    win.blit(idle_scaled[idlemove], (self.x, self.y))
                    idlemove += 1
            if self.left:
                self.hitbox = (self.x + 200, self.y + 200 , width - 270, height - 250)
                self.atkdec = (self.x + 90, self.y + 290 , width - 200, height - 380)
                
            else:
                self.hitbox = (self.x + 70, self.y + 200 , width - 270, height - 250)
                self.atkdec = (self.x + 90, self.y + 290 , width - 200, height - 380)
                
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
            pygame.draw.rect(win, (255, 0, 0), self.atkdec, 2)
            
    def hero_attack(self, win):
        if self.visible and Golem.visible:
            if self.atkdec[0] < Golem.hitbox[0] + Golem.hitbox[2] and self.atkdec[0] + self.atkdec[2] > Golem.hitbox[0]:
                if self.atkdec[1] + self.atkdec[3] > Golem.hitbox[1] and self.atkdec[1] < Golem.hitbox[1] + Golem.hitbox[3]:
                    Golem.hit = True
                    Golem.enemie_movel = False
                    Golem.attack = False
                    Golem.taunted = False
                    
                    
                    
    def logic(self, win):
        self.controls(win)
        self.drawchar(win)
        self.hero_attack(win)
         
class Enemy():
    def __init__(self, x, y ,width, height ):
         self.x =x
         self.y = y
         self.height = height
         self.width =width
         self.vel = 5
         self.left = False
         self.right = False
         self.taunted = False
         self.ewalkcount = 0
         self.enemie_movel = False
         self.enemie_mover= False
         self.visible= True
         self.hitbox = pygame.Rect(self.x + 120 - scroll, self.y + 80, 90, 220)
         self.taunt_detect1 = pygame.Rect(self.x - 540  - scroll, self.y + 170, 670, 30)
         self.taunt_detect2 = pygame.Rect(self.x + 540  - scroll, self.y + 170, 670, 30) 
         self.walk_detect = pygame.Rect(self.x - 400 - scroll, self.y + 80, 520, 220)
         self.walk_detect2 =pygame.Rect(self.x + 400 - scroll, self.y + 80, 520, 220)
         self.atk_detect= pygame.Rect(self.x + 150 - scroll, self.y + 80, 230, 220)
         self.atk_detect2=pygame.Rect(self.x - 150 - scroll, self.y + 80, 230, 220)
         self.attack = False
         self.hit = 0
         self.health = 10
         self.eidlemove = 0
         self.taunting = 0
         self.attackcount = 0
         self.hit = False
         self.hitcount = 0
         
    def drawenemie(self, win):
        
            if self.right == False and self.left == False and not(self.enemie_movel) and not(self.enemie_mover):
                if self.eidlemove >= len(Golem_idle):
                    self.eidlemove = 0
                win.blit(Golem_idle_scaled[self.eidlemove], (self.x - scroll, self.y))
                self.eidlemove += 1
                
            self.hitbox = pygame.Rect(self.x + 120 - scroll, self.y + 80, 90, 220)
            self.taunt_detect1 = pygame.Rect(self.x - 540  - scroll, self.y + 170, 670, 30)
            self.taunt_detect2 = pygame.Rect(self.x + 200  - scroll, self.y + 170, 670, 30)
            self.walk_detect = pygame.Rect(self.x - 400 - scroll, self.y + 80, 520, 220)
            self.walk_detect2 = pygame.Rect(self.x + 200 - scroll, self.y + 80, 520, 220)
            self.atk_detect= pygame.Rect(self.x + 150 - scroll, self.y + 80, 230, 220)
            self.atk_detect2=pygame.Rect(self.x - 30 - scroll, self.y + 80, 230, 220)
            
            

            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
            #pygame.draw.rect(win, (255, 0, 0), self.taunt_detect1, 2)
            #pygame.draw.rect(win, (255, 0, 0), self.walk_detect, 2)
            #pygame.draw.rect(win, (255, 0, 0), self.walk_detect2, 2)
            #pygame.draw.rect(win, (255, 0, 0), self.atk_detect, 2)
            #pygame.draw.rect(win, (255, 0, 0), self.atk_detect2, 2)
            
    def enemy_attack(self, win):
        # Enemy attack collision
        if self.visible and heroes.visible:
            if self.taunt_detect1[0] < heroes.hitbox[0] + heroes.hitbox[2] and self.taunt_detect1[0] + self.taunt_detect1[2] > heroes.hitbox[0]:
                if self.taunt_detect1[1] + self.taunt_detect1[3] > heroes.hitbox[1] and self.taunt_detect1[1] < heroes.hitbox[1] + heroes.hitbox[3]:
                    self.taunted = True
                    self.left = True
                    self.right = False
        
            elif self.taunt_detect2[0] < heroes.hitbox[0] + heroes.hitbox[2] and self.taunt_detect2[0] + self.taunt_detect2[2] > heroes.hitbox[0]:
                if self.taunt_detect2[1] + self.taunt_detect2[3] > heroes.hitbox[1] and self.taunt_detect2[1] < heroes.hitbox[1] + heroes.hitbox[3]:
                    self.taunted = True
                    self.right = True
                    self.left = False
            else:
                self.taunted = False
                self.left = False
                self.right = False
        
        if self.visible and heroes.visible:
            if self.walk_detect[0] < heroes.hitbox[0] + heroes.hitbox[2] and self.walk_detect[0] + self.walk_detect[2] > heroes.hitbox[0]:
                if self.walk_detect[1] + self.walk_detect[3] > heroes.hitbox[1] and self.walk_detect[1] < heroes.hitbox[1] + heroes.hitbox[3]:
                    self.enemie_movel = True
                    self.taunted = False
                    self.attack = False
                    self.left = True
                    self.right = False
        
            elif self.walk_detect2[0] < heroes.hitbox[0] + heroes.hitbox[2] and self.walk_detect2[0] + self.walk_detect2[2] > heroes.hitbox[0]:
                if self.walk_detect2[1] + self.walk_detect2[3] > heroes.hitbox[1] and self.walk_detect2[1] < heroes.hitbox[1] + heroes.hitbox[3]:
                    self.enemie_mover = True
                    self.taunted = False
                    self.attack = False
                    self.right = True
                    self.left = False
            else:
                self.taunted = True
                self.enemie_movel = False
                self.enemie_mover = False
                
        if self.visible and heroes.visible:
            if self.atk_detect[0] < heroes.hitbox[0] + heroes.hitbox[2] and self.atk_detect[0] + self.atk_detect[2] > heroes.hitbox[0]:
                if self.atk_detect[1] + self.atk_detect[3] > heroes.hitbox[1] and self.atk_detect[1] < heroes.hitbox[1] + heroes.hitbox[3]:
                    self.enemie_movel = False
                    self.attack = True
                    self.taunted = False
                    self.left = False
                    self.right = True
        
            elif self.atk_detect2[0] < heroes.hitbox[0] + heroes.hitbox[2] and self.atk_detect2[0] + self.atk_detect2[2] > heroes.hitbox[0]:
                if self.atk_detect2[1] + self.atk_detect2[3] > heroes.hitbox[1] and self.atk_detect2[1] < heroes.hitbox[1] + heroes.hitbox[3]:
                    self.enemie_mover = False
                    self.attack = True
                    self.taunted = False
                    self.right = False
                    self.left = True
                    
            else:
                self.taunted = False
                self.attack = False
              
                if self.left:
                    self.enemie_movel = True
                    self.enemie_mover = False
                if self.right:
                    self.enemie_mover = True
                    self.enemie_movel = False
    
            
            
    def taunt(self, win):
        if self.right == True and self.enemie_mover == False and self.taunted:
            if self.taunting >= len(Golem_taunt):
                    self.taunting = 0
            win.blit(Golem_taunt_scaled[self.taunting], (self.x - scroll, self.y))
            self.taunting += 1
            self.hit = False
            
        elif self.left == True and self.enemie_movel == False and self.taunted:
            if self.taunting >= len(Golem_tauntleft):
                    self.taunting = 0
            win.blit(Golem_tauntleft_scaled[self.taunting], (self.x - scroll, self.y))
            self.taunting += 1
            
    def walk(self, win):
        if self.right == True and self.enemie_mover and not(self.attack):
            if self.ewalkcount + 1 >= len(Golem_walking):
                self.ewalkcount = 0
            if self.x + self.vel > 0:
                self.x += self.vel
            
            win.blit(Golem_walking_scaled[self.ewalkcount], (self.x - scroll, self.y))
            self.ewalkcount += 1
        elif self.left == True and self.enemie_movel and not(self.attack):
           if self.ewalkcount + 1 >= len(Golem_walkingleft):
                self.ewalkcount = 0
           if self.x - self.vel > 0:
                self.x -= self.vel
           win.blit(Golem_walkingleft_scaled[self.ewalkcount], (self.x - scroll, self.y))
           self.ewalkcount += 1
           
    def attackhero(self, win):
        if self.right and self.attack:
            if self.attackcount >= len(Golem_Attack):
                    self.attackcount = 0
            win.blit(Golem_Attack_scaled[self.attackcount], (self.x - scroll, self.y))
            self.attackcount += 1
        elif self.left and self.attack:
            if self.attackcount >= len(Golem_Attackleft):
                    self.attackcount = 0
            win.blit(Golem_Attackleft_scaled[self.attackcount], (self.x - scroll, self.y))
            self.attackcount += 1
    
    def attacked(self, win):
        if self.right and self.hit and heroes.attack or heroes.atk or heroes.attackl :
            if self.hitcount >= len(Golem_hurt):
                    self.hitcount = 0
            win.blit(Golem_hurt_scaled[self.hitcount], (self.x - scroll, self.y))
            self.hitcount += 1
            
        elif self.left and self.hit and heroes.attack or heroes.atk or heroes.attackl :
            if self.hitcount >= len(Golem_hurt):
                    self.hitcount = 0
            win.blit(Golem_hurtleft_scaled[self.hitcount], (self.x - scroll, self.y))
            self.hitcount += 1 
        
        
    def ai(self, win):
        self.drawenemie(win)
        self.enemy_attack(win)
        self.taunt(win)
        self.walk(win)
        self.attackhero(win)
        self.attacked(win)
         
        
            
      
            
                

        
        
    
#Function for all the stuff displayed on the window
def redrawwindow():
 
    # Scrolling function when player moves
    for x in range(5):
        speed = 1
        for bg_image in bg_images_scaled:
            offset = (x * bg_width - scroll * speed)
            if offset < -bg_width:
                offset += bg_width
            win.blit(bg_image, (offset, 0))
            speed += 0.2
        
    Golem.ai(win)    
    heroes.logic(win)
    
    
    pygame.display.update()

heroes = hero(300, 460, 128,128)
Golem = Enemy(2000, 510, 300, 300)

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
        win.blit(bg_scaled[0], (0,0))
        win.blit(pygame.transform.scale(board, (1500, 1500)),(0,-220))
        txt("SELECT PLAYER", adventure, (255, 225, 0), 550, 300)
        if char1.drawbutton(win):
            play()
            
         
        if char2.drawbutton(win):
            play()
        
            
        if char3.drawbutton(win):
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

