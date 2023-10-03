import pygame
pygame.init()
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
import main



os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

# Set Window Size
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h

win = pygame.display.set_mode((screen_width - 10, screen_height - 30), pygame.RESIZABLE)



#background image and settings
bg_images = []
for i in range(1, 6):
    bg_image = pygame.image.load(f"../THE LAND OF OZ/forest background/PNG/Cartoon_Forest_BG_01/Layers/plx{i}.png").convert_alpha()
    bg_images.append(bg_image)
    
bgimages_scaled = [pygame.transform.scale(img, (screen_width, screen_height)) for img in bg_images]
bg_width = bgimages_scaled[0].get_width()


info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h

win = pygame.display.set_mode((screen_width - 10, screen_height - 30), pygame.RESIZABLE)



width = 400 
height = 400
e_width = 310
e_height = 310

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