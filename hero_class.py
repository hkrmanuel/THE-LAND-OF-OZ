import pygame
import load_images
import os
import enemy_class

FPS = 17
scroll = 0

width = 400 
height = 400
e_width = 310
e_height = 310

idlemove = 0

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()


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
                    
                    if self.walkcount // 3 >= len(load_images.walkleft):
                        self.walkcount = 0
                    win.blit(load_images.walkleft_scaled[self.walkcount // 3], (self.x, self.y))
                    self.walkcount += 1
                    
                
                elif self.left and self.run == 1 and self.jump_on == False :
                    
                    if self.walkcount // 2 >= len(load_images.runleft):
                        self.walkcount = 0
                    win.blit(load_images.runleft_scaled[self.walkcount // 2], (self.x, self.y))
                    self.walkcount += 1
                    
                elif self.right and self.jump_on == False and self.run == 0:
                
                    if self.walkcount // 2 >= len(load_images.walkright):
                        self.walkcount = 0
                    win.blit(load_images.walkright_scaled[self.walkcount // 2], (self.x, self.y))
                    self.walkcount += 1
                 
                elif self.right and self.run == 1 and self.jump_on == False :
                    if self.walkcount // 2 >= len(load_images.runright):
                        self.walkcount = 0
                    win.blit(load_images.runright_scaled[self.walkcount // 2], (self.x, self.y))
                    self.walkcount += 1
                else:
                    self.standing = True
                    
                if self.jump_on:
                    if self.right and self.run == 0 or self.attack:
                        self.standing = False
                        self.left = False
                        if jumpmove >= len(load_images.jumpright_scaled):
                            jumpmove = 0
                        win.blit(load_images.jumpright_scaled[jumpmove], (self.x, self.y))
                        jumpmove += 1
                    elif self.left and self.run ==0 or self.attackl:
                        self.standing = False
                        self.right = False
                        if jumpmove >= len(load_images.jumpleft_scaled):
                            jumpmove = 0
                        win.blit(load_images.jumpleft_scaled[jumpmove], (self.x, self.y))
                        jumpmove += 1
                
                else:
                    self.standing = True
                
                if self.jump_on and self.run == 1: 
          
                    if self.right and self.run == 1:
                        self.standing = False
                        self.left = False
                        if jumpmove >= len(load_images.highjumpright_scaled):
                            jumpmove = 0
                        win.blit(load_images.highjumpright_scaled[jumpmove], (self.x, self.y))
                        jumpmove += 1
                    elif self.left and self.run == 1:
                        self.standing = False
                        self.right = False
                        if jumpmove >= len(load_images.highjumpleft_scaled):
                            jumpmove = 0
                        win.blit(load_images.highjumpleft_scaled[jumpmove], (self.x, self.y))
                        jumpmove += 1
                    else:
                        self.standing = True
                        
                if self.attack and not(self.jump_on) and not(self.left) and not(self.right) and self.run == 0:
                    if attackmove >= len(load_images.attackwalk):
                        attackmove = 0
                    win.blit(load_images.attackwalk_scaled[attackmove], (self.x, self.y))
                    attackmove += 1
                if self.attackl and not(self.jump_on) and not(self.left) and not(self.right) and self.run ==0:
                    if attackmove >= len(load_images.attackload_images.walkleft):
                        attackmove = 0
                    win.blit(load_images.attackwalkleft_scaled[attackmove], (self.x, self.y))
                    attackmove += 1
                    
                    #Running Attack
                if self.attack and not(self.jump_on) and not(self.left) and not(self.right) and self.run == 1:
                    if attackmove >= len(load_images.attackrun):
                        attackmove = 0
                    win.blit(load_images.attackrun_scaled[attackmove], (self.x, self.y))
                    attackmove += 1
                if self.attackl and not(self.jump_on) and not(self.left) and not(self.right) and self.run == 1:
                    if attackmove >= len(load_images.attackrunleft):
                        attackmove = 0
                    win.blit(load_images.attackrunleft_scaled[attackmove], (self.x, self.y))
                    attackmove += 1
                if self.atk and not(self.jump_on) and not(self.left) and not(self.right):
                    if attackmove >= len(load_images.attack):
                        attackmove = 0
                    win.blit(load_images.attack_scaled[attackmove], (self.x, self.y))
                    attackmove += 1
              

            else:
                if self.right == False and self.left == False and self.standing ==True:
                    if idlemove >= len(load_images.idle):
                        idlemove = 0
                    win.blit(load_images.idle_scaled[idlemove], (self.x, self.y))
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
        if self.visible and enemy_class.Golem.visible:
            if self.atkdec[0] < enemy_class.Golem.hitbox[0] + enemy_class.Golem.hitbox[2] and self.atkdec[0] + self.atkdec[2] > enemy_class.Golem.hitbox[0]:
                if self.atkdec[1] + self.atkdec[3] > enemy_class.Golem.hitbox[1] and self.atkdec[1] < enemy_class.Golem.hitbox[1] + enemy_class.Golem.hitbox[3]:
                    enemy_class.Golem.hit = True
                    enemy_class.Golem.enemie_movel = False
                    enemy_class.Golem.attack = False
                    enemy_class.Golem.taunted = False
                    
                    
                    
    def logic(self, win):
        self.controls(win)
        self.drawchar(win)
        self.hero_attack(win)