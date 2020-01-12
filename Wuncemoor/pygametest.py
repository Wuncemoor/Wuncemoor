import pygame
import sys
import os


'''
Objects
'''

class Player(pygame.sprite.Sprite):
    '''
    Make Player
    '''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0 
        self.movey = 0
        self.frame = 0 #count frames
        self.images = []
        for i in range(1,7):
            img = pygame.image.load(os.path.join(r'C:\Users\penic\Desktop\Python\Projects\Wuncemoor\images\Knight\Walk','walk' + str(i) + '.png'))
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect() 
            
    def control(self,x,y):
        '''
        Player Movement
        '''
        self.movex += x
        self.movex += y
    def update(self):
        '''
        Update sprite position
        '''
        
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey
        
        #move left
        if self.movex < 0 :
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = self.images[self.frame//ani]
            
        #move right
        if self.movex > 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = self.images[self.frame//ani]

class Enemy(pygame.sprite.Sprite):
    '''
    Spawn enemy
    '''
    
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for i in range(1,7):
            img = pygame.image.load(os.path.join(r'C:\Users\penic\Desktop\Python\Projects\Wuncemoor\images\Mage\Walk','walk' + str(i) + '.png'))
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
            self.image.convert_alpha()
            self.rect.x = x
            self.rect.y = y
'''
Setup
'''
screen_size = (800,600)
fps = 60
ani = 4
clock = pygame.time.Clock()
pygame.init()
world = pygame.display.set_mode(screen_size)
backdrop = pygame.image.load(os.path.join(r'C:\Users\penic\Desktop\Python\Projects\Wuncemoor\images','stage.png'))
backdropbox = world.get_rect()
main = True

player = Player() #spawn player
player.rect.x = 0
player.rect.y = 0
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 10 #how many pixels to move

enemy = Enemy(20,200)
enemy_list = pygame.sprite.Group()
enemy_list.add(enemy)


'''
Main Loop
'''

while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            main = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(-steps,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(steps,0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                print('jump')
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(steps,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(-steps,0)
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False
        
       
    world.blit(backdrop, backdropbox)
    player.update()
    player_list.draw(world) #Draw player
    enemy_list.draw(world)
    pygame.display.flip()
    clock.tick(fps)
	
