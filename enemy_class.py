import pygame
import hero_class
import load_images
import main

pygame.init()
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()


FPS = 17
scroll = 0

width = 400 
height = 400
e_width = 310
e_height = 310

         
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
                if self.eidlemove >= len(load_images.Golem_idle):
                    self.eidlemove = 0
                win.blit(load_images.Golem_idle_scaled[self.eidlemove], (self.x - scroll, self.y))
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
        if self.visible and main.heroes.visible:
            if self.taunt_detect1[0] < main.heroes.hitbox[0] + main.heroes.hitbox[2] and self.taunt_detect1[0] + self.taunt_detect1[2] > main.heroes.hitbox[0]:
                if self.taunt_detect1[1] + self.taunt_detect1[3] > main.heroes.hitbox[1] and self.taunt_detect1[1] < main.heroes.hitbox[1] + main.heroes.hitbox[3]:
                    self.taunted = True
                    self.left = True
                    self.right = False
        
            elif self.taunt_detect2[0] < main.heroes.hitbox[0] + main.heroes.hitbox[2] and self.taunt_detect2[0] + self.taunt_detect2[2] > main.heroes.hitbox[0]:
                if self.taunt_detect2[1] + self.taunt_detect2[3] > main.heroes.hitbox[1] and self.taunt_detect2[1] < main.heroes.hitbox[1] + main.heroes.hitbox[3]:
                    self.taunted = True
                    self.right = True
                    self.left = False
            else:
                self.taunted = False
                self.left = False
                self.right = False
        
        if self.visible and main.heroes.visible:
            if self.walk_detect[0] < main.heroes.hitbox[0] + main.heroes.hitbox[2] and self.walk_detect[0] + self.walk_detect[2] > main.heroes.hitbox[0]:
                if self.walk_detect[1] + self.walk_detect[3] > main.heroes.hitbox[1] and self.walk_detect[1] < main.heroes.hitbox[1] + main.heroes.hitbox[3]:
                    self.enemie_movel = True
                    self.taunted = False
                    self.attack = False
                    self.left = True
                    self.right = False
        
            elif self.walk_detect2[0] < main.heroes.hitbox[0] + main.heroes.hitbox[2] and self.walk_detect2[0] + self.walk_detect2[2] > main.heroes.hitbox[0]:
                if self.walk_detect2[1] + self.walk_detect2[3] > main.heroes.hitbox[1] and self.walk_detect2[1] < main.heroes.hitbox[1] + main.heroes.hitbox[3]:
                    self.enemie_mover = True
                    self.taunted = False
                    self.attack = False
                    self.right = True
                    self.left = False
            else:
                self.taunted = True
                self.enemie_movel = False
                self.enemie_mover = False
                
        if self.visible and main.heroes.visible:
            if self.atk_detect[0] < main.heroes.hitbox[0] + main.heroes.hitbox[2] and self.atk_detect[0] + self.atk_detect[2] > main.heroes.hitbox[0]:
                if self.atk_detect[1] + self.atk_detect[3] > main.heroes.hitbox[1] and self.atk_detect[1] < main.heroes.hitbox[1] + main.heroes.hitbox[3]:
                    self.enemie_movel = False
                    self.attack = True
                    self.taunted = False
                    self.left = False
                    self.right = True
        
            elif self.atk_detect2[0] < main.heroes.hitbox[0] + main.heroes.hitbox[2] and self.atk_detect2[0] + self.atk_detect2[2] > main.heroes.hitbox[0]:
                if self.atk_detect2[1] + self.atk_detect2[3] > main.heroes.hitbox[1] and self.atk_detect2[1] < main.heroes.hitbox[1] + main.heroes.hitbox[3]:
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
            if self.taunting >= len(load_images.Golem_taunt):
                    self.taunting = 0
            win.blit(load_images.Golem_taunt_scaled[self.taunting], (self.x - scroll, self.y))
            self.taunting += 1
            self.hit = False
            
        elif self.left == True and self.enemie_movel == False and self.taunted:
            if self.taunting >= len(load_images.Golem_tauntleft):
                    self.taunting = 0
            win.blit(load_images.Golem_tauntleft_scaled[self.taunting], (self.x - scroll, self.y))
            self.taunting += 1
            
    def walk(self, win):
        if self.right == True and self.enemie_mover and not(self.attack):
            if self.ewalkcount + 1 >= len(load_images.Golem_walking):
                self.ewalkcount = 0
            if self.x + self.vel > 0:
                self.x += self.vel
            
            win.blit(load_images.Golem_walking_scaled[self.ewalkcount], (self.x - scroll, self.y))
            self.ewalkcount += 1
        elif self.left == True and self.enemie_movel and not(self.attack):
           if self.ewalkcount + 1 >= len(load_images.Golem_walkingleft):
                self.ewalkcount = 0
           if self.x - self.vel > 0:
                self.x -= self.vel
           win.blit(load_images.Golem_walkingleft_scaled[self.ewalkcount], (self.x - scroll, self.y))
           self.ewalkcount += 1
           
    def attackhero(self, win):
        if self.right and self.attack:
            if self.attackcount >= len(load_images.Golem_Attack):
                    self.attackcount = 0
            win.blit(load_images.Golem_Attack_scaled[self.attackcount], (self.x - scroll, self.y))
            self.attackcount += 1
        elif self.left and self.attack:
            if self.attackcount >= len(load_images.Golem_Attackleft):
                    self.attackcount = 0
            win.blit(load_images.Golem_Attackleft_scaled[self.attackcount], (self.x - scroll, self.y))
            self.attackcount += 1
    
    def attacked(self, win):
        if self.right and self.hit and main.heroes.attack or main.heroes.atk or main.heroes.attackl :
            if self.hitcount >= len(load_images.Golem_hurt):
                    self.hitcount = 0
            win.blit(load_images.Golem_hurt_scaled[self.hitcount], (self.x - scroll, self.y))
            self.hitcount += 1
            
        elif self.left and self.hit and main.heroes.attack or main.heroes.atk or main.heroes.attackl :
            if self.hitcount >= len(load_images.Golem_hurt):
                    self.hitcount = 0
            win.blit(load_images.Golem_hurtleft_scaled[self.hitcount], (self.x - scroll, self.y))
            self.hitcount += 1 
    
    def ai(self, win):
        self.drawenemie(win)
        self.enemy_attack(win)
        self.taunt(win)
        self.walk(win)
        self.attackhero(win)
        self.attacked(win)
         