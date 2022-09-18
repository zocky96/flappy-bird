import pygame
class Player():
    def __init__(self,x,y,image):
        super().__init__()
        self.image = image
        self.image = self.image.subsurface(113,431,21,17)
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def drawPlayer(self,screen):
        #pygame.draw.rect(screen, [255, 0, 0], self.rect, 0)
        screen.blit(self.image,(self.rect.x,self.rect.y))
    def movePlayer(self,velocity):
        self.rect.y += velocity
    def gravity(self):
        self.rect.y += 1
