import pygame
class Bar:
    def __init__(self,x,y,image):
        self.image = image
        self.pipe_up = self.image.subsurface(83,324,28,161)
        #self.rect = pygame.Rect(self.x,self.y,20,200)
        self.rect = self.pipe_up.get_rect()
        self.rect.x = x
        self.rect.y = y

    def moveBar(self):
        #print(self.rect.x)
        self.rect.x -=1
        #self.x -= 1
    def drawBar(self,screen):
        #pygame.draw.rect(screen,(0,0,255),self.rect,0)
        screen.blit(self.pipe_up,(self.rect.x,self.rect.y))