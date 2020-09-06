import pygame#check check
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((640,480))
location="C:\\Users\\Naveen Renold\\Desktop\\pygame\\"
player=pygame.image.load(location+"Walk\\base_base_man.png").convert()
player_walk5=pygame.image.load(location+"Walk\\walking5.png").convert()
player_walk4=pygame.image.load(location+"Walk\\walking4.png").convert()
player_walk3=pygame.image.load(location+"Walk\\walking3.png").convert()
player_walk2=pygame.image.load(location+"Walk\\walking1.png").convert()
player_walk1=pygame.image.load(location+"Walk\\base_walk.png").convert()
walk=[]
walk.append(player_walk1)
walk.append(player_walk2)
walk.append(player_walk5)
walk.append(player_walk3)
walk.append(player_walk4)

player_walk5_reverse=pygame.image.load(location+"Walk\\walking5_reverse.png").convert()
player_walk4_reverse=pygame.image.load(location+"Walk\\walking4_reverse.png").convert()
player_walk3_reverse=pygame.image.load(location+"Walk\\walking3_reverse.png").convert()
player_walk2_reverse=pygame.image.load(location+"Walk\\walking1_reverse.png").convert()
player_walk1_reverse=pygame.image.load(location+"Walk\\base_walk_reverse.png").convert()
walk.append(player_walk1_reverse)
walk.append(player_walk2_reverse)
walk.append(player_walk5_reverse)
walk.append(player_walk3_reverse)
walk.append(player_walk4_reverse)

background=pygame.image.load(location+"ground2.png").convert()
sun=pygame.image.load(location+"sun.png").convert()

sound1=pygame.mixer.Sound(location+"gameclose.wav")
font1=pygame.font.Font(None,30)
font2=pygame.font.Font(None,16)
clock=pygame.time.Clock()
#pygame.key.set_repeat(1,50)
class GameObject:
    def __init__(self,image,speed,position,paste=True):
        colorkey=image.get_at((0,0))
        self.speed=speed
        self.image=image
        self.x=position[0]
        self.y=position[1]
        self.image.set_colorkey(colorkey,RLEACCEL)
        self.rect=image.get_rect()
        self.rect=self.rect.move(self.x,self.y)
        if(paste):
            screen.blit(background,self.rect,self.rect)
            screen.blit(self.image,self.rect)
        #self.rect=self.rect.move(position)
    def show(self):
        screen.blit(self.image,self.rect)
    def hide(self):
        screen.blit(background,self.rect,self.rect)
class PlayerObject(GameObject):
    def __init__(self,image,speed,position,walk_animations,paste=True):
        super().__init__(image,speed,position,paste)
        self.walk_animations=walk_animations
        self.i=0
        self.temp_image=None
        for j in range(len(self.walk_animations)):
            colorkey=self.walk_animations[j].get_at((0,0))
            self.walk_animations[j].set_colorkey(colorkey,RLEACCEL)
        #print(self.i)        
    def move(self,speed=5,direction=1):
        direction_factor=0
        if(direction==-1):
                speed=speed*direction
                direction_factor=len(self.walk_animations)//2
        self.x=self.x+speed
        if(self.x<0):
            self.x=0
        elif(self.x>620):
            self.x=620
        else:
            if(self.i==len(self.walk_animations)//2):
                self.i=0
            #print(((self.i)//2)+direction_factor)
            self.temp_image=self.walk_animations[((self.i))+direction_factor]
            self.i=self.i+1
            screen.blit(background,self.rect,self.rect)
            self.rect=self.rect.move((speed,0))
            screen.blit(self.temp_image,self.rect)
class FightMode(GameObject):
    def __init__(self,image,speed,position,crouches,bullet,paste=True,direction=1):
        super().__init__(image,speed,position,paste)
        colorkey=crouches.get_at((0,0))
        crouches.set_colorkey(colorkey,RLEACCEL)
        self.crouches=crouches
        self.stand=image
        self.hp=100
        self.bullet=bullet
        colorkey2=self.bullet.get_at((0,0))
        self.position=position
        self.bullet.set_colorkey(colorkey2,RLEACCEL)
        self.bullet_x=position[0]+90
        self.bullet_y=position[1]+20
        self.bullet_rect=self.bullet.get_rect()
        self.bullet_rect=self.bullet_rect.move(self.bullet_x,self.bullet_y)
        self.bullet_speed=5
        self.bullet_direction=1
    def stands(self):
        self.image=self.crouches
        super().hide()
        self.image=self.stand
        super().show()
    def crouch(self):
        self.image=self.stand
        super().hide()
        self.image=self.crouches
        super().show()
    def shoot(self):
        #temp=self.image
        #self.image=self.bullet   
        if(self.bullet_x>=620):
            screen.blit(background,self.bullet_rect,self.bullet_rect)
            print("if 2:",self.bullet_x)
            self.bullet_x=self.position[0]+90
            self.bullet_y=self.position[1]+20
            self.bullet_rect=self.bullet.get_rect()
            self.bullet_rect=self.bullet_rect.move(self.bullet_x,self.bullet_y)
            return False
        if(self.bullet_x<620):#saved
            screen.blit(background,self.bullet_rect,self.bullet_rect)
            #pygame.display.update()
            self.bullet_x=self.bullet_x+40
            print("if 1:",self.bullet_x)
            self.bullet_rect=self.bullet_rect.move(40,0)
            screen.blit(self.bullet,self.bullet_rect)
            #self.image=stand
        return True
    def bullet_show(self):
        screen.blit(self.bullet,self.bullet_rect)
  #  def hide(self):
 #   def show(self):

#Level 1
screen.blit(background,(0,0))
arrow=pygame.image.load(location+"orange_green_arrow.png").convert()
npc=pygame.image.load(location+"man.png").convert()
text=font1.render("Use arrow keys to move",False,(255,255,0))
text21=font2.render("There is a lot of crowd up ahead.",False,(255,0,0))
text22=font2.render("Wonder what happened",False,(255,0,0))
text4=font1.render("Press up arrow to talk",False,(255,255,0))
text1=GameObject(text,0,(150,430))
text31=GameObject(text21,0,(410,250))
text32=GameObject(text22,0,(410,264))
text5=GameObject(text4,0,(150,430))
arrow1=GameObject(arrow,0,(530,275))
p1=PlayerObject(player,5,(70,290),walk)
sun_pic=GameObject(sun,0,(400,70))
npc1=GameObject(npc,5,(400,290))

text5.hide()
text1.show()
text31.hide()
text32.hide()
talked=0
pygame.display.update()

run=True
while(run):
    for event in pygame.event.get():
        if event.type is QUIT:
            pygame.quit()
    keys=pygame.key.get_pressed()
    if keys[K_RIGHT]:
        p1.move(5)
    elif keys[K_LEFT]:
        p1.move(5,-1)
    elif keys[K_UP] and (p1.x>350) and (p1.x<450):
        text31.show()
        text32.show()
        talked=1
        pygame.display.update()
        pygame.time.wait(2000)
        text31.hide()
        text32.hide()
    else:
        p1.hide()
        p1.show()
    arrow1.show()
    sun_pic.show()
    npc1.show()
    text1.hide()
    text5.hide()
    if(p1.x<250):
        text1.show()
    if(p1.x>300 and talked!=1):
        text5.show()
    if(p1.x>600 and talked==1):
        run=False
    pygame.display.update()
    clock.tick(27)
    #print(clock.get_fps())
        
#Level 2
background=pygame.image.load(location+"level2background.png").convert()
light_on=pygame.image.load(location+"light_on.png").convert()
light_off=pygame.image.load(location+"light_off.png").convert()
p1=PlayerObject(player,5,(0,290),walk)
lamp_on=GameObject(light_on,0,(516,218))
lamp_off=GameObject(light_off,0,((516,218)))
screen.blit(background,(0,0))
lamp_is_on=True
pressed=False
run=True
while(run):
    for event in pygame.event.get():
        if event.type is QUIT:
            pygame.quit()
    keys=pygame.key.get_pressed()
    if(not keys[K_UP]):
        pressed=False
    if keys[K_RIGHT]:
        p1.move(5)
    elif keys[K_LEFT]:
        p1.move(5,-1)
    elif(keys[K_UP]):
        if(p1.x>450 and p1.x<600 and not pressed):
            if(lamp_is_on):
                lamp_on.hide()
                lamp_off.show()
            else:
                lamp_on.show()
                lamp_off.hide()
            pressed=True
            #print(pressed)
            lamp_is_on=not lamp_is_on
        if(p1.x>30 and p1.x<100):
            run=False
    else:
        p1.hide()
        p1.show()
    #p1.show()
    pygame.display.update()
    clock.tick(27)

#Level3
background=pygame.image.load(location+"background3.png").convert()
screen.blit(background,(0,0))
p2=PlayerObject(player,5,(0,290),walk)
round1=False
run=True
crouches=pygame.image.load(location+"crouch-4.png").convert()
standing=pygame.image.load(location+"stand2.png").convert()
bullet1=pygame.image.load(location+"bullet1.png").convert()
#Enemy
enemies1=pygame.image.load(location+"enemy6.png").convert()
enemies1_crouch=pygame.image.load(location+"enemy_crouch2.png").convert()
#empty_list=[]
player_fight=FightMode(standing,0,(50,260),crouches,bullet1,paste=False)
#Enemy
enemy1=FightMode(enemies1,0,(520,240),enemies1_crouch,bullet1,paste=False)

#enemy1=GameObject(enemies1,0,(520,240))
#enemy1_crouch=GameObject(enemies1_crouch,0,(500,240))

#crouch.hide()
#enemy1_crouch.show()
enemy1.crouch()
pygame.display.update()
#clock1=pygame.time.Clock()
while(run):
    for event in pygame.event.get():
        if event.type is QUIT:
            pygame.quit()
    keys=pygame.key.get_pressed()
    if(p2.x>40):
        run=False
        round1=True
    if keys[K_RIGHT]:
        p2.move(5)
    elif keys[K_LEFT]:
        p2.move(5,-1)
    else:
        p2.hide()
        p2.show()
    #p1.show()
    pygame.display.update()
    clock.tick(27)
player_fight.crouch()
p2.x=50
shooting=False
while(round1):
    for event in pygame.event.get():
        if event.type is QUIT:
            pygame.quit()
    keys=pygame.key.get_pressed()
    if(keys[K_UP]):
        player_fight.stands()
        if(keys[K_SPACE] or shooting==True):
            if(shooting==False):
                shooting=True
            else:
                shooting=player_fight.shoot()
                player_fight.bullet_show()
  #      if(keys[K_SPACE]) and not shooting):
  #          shooting=player_fight.shoot()
  #          player_fight.bullet_show()
            #pygame.time.delay(5000)
        #enemy1_crouch.hide()
        #enemy1.show()
        enemy1.stands()
    else:
        player_fight.crouch()
        #enemy1.hide()
        #enemy1_crouch.show()
        enemy1.crouch()
        #clock.tick(27)
    pygame.display.update()
    clock.tick(27)



