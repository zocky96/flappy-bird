import random

import pygame
from bar import Bar
from player import Player
class Game:
    def __init__(self):
        pygame.display.set_caption("zoe games")
        self.screen = pygame.display.set_mode((700,500))
        self.rect_screen = pygame.Rect(0,0,700,500)
        self.listPipe = []
        self.score = 0
        self.itsOver = False
        self.x = 150
        self.y = 150
        self.image = pygame.image.load("images/images.png")
        self.game_over = self.image.subsurface(392,57,101,26)
        self.game_over = pygame.transform.scale(self.game_over,(250,180))
        self.playButton = self.image.subsurface(351,117,58,32)
        self.playButton = pygame.transform.scale(self.playButton,(150,80))
        self.player = Player(self.x,self.y,self.image)
        self.random_x = 900
        self.random_y = random.randrange(690,700)
        bar = Bar(self.random_x,self.random_y,self.image)
        self.listPipe.append(bar)
        self.velocity = 0
        self.index = 0
        self.background = self.image.subsurface(2,2,114,255)
        self.image_width = 700
        self.background = pygame.transform.scale(self.background,(self.image_width,500))
        self.fps=pygame.time.Clock()
        self.running = True
    def gameOver(self):
        ob_text = pygame.font.SysFont("arial", 50, True, False)
        text = ob_text.render("GAME OVER", False, (255, 0, 0),)
        self.screen.blit(self.game_over, [200, 190])

        ob_text = pygame.font.SysFont("arial", 30, True, False)
        text = ob_text.render("[SPACE] pour continue", False, (255, 0, 0), )
        self.screen.blit(self.playButton, [250, 380])

    def drawScore(self):
        ob_text = pygame.font.SysFont("arial", 20, True, False)
        text = ob_text.render(f"Score : {self.score}", False, (255, 0, 0),)
        self.screen.blit(text, [590, 0])

    def new_game(self):
        self.itsOver = False
        self.random_y = random.randrange(600, 700)
        bar = Bar(self.random_x, self.random_y, self.image)
        self.listPipe.append(bar)
    def main_screen(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    if self.itsOver:
                        if event.pos[0] in range(260,390) and event.pos[1] in range(383,454):
                            if event.buttons[0] == 1:
                                self.new_game()
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.velocity = -5
                    if event.key == pygame.K_SPACE:
                        self.new_game()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.velocity = 0
            self.screen.fill((255,255,255))
            for bar in self.listPipe:
                if self.player.rect.colliderect(bar.rect):
                    self.gameOver()
                    self.score = 0
                    self.player.rect.x -= 5
                    self.itsOver = True
                    self.listPipe.clear()
            for bar in self.listPipe:
                if self.player.rect.x == bar.rect.x:
                    self.random_x = random.randrange(300, 600)
                    self.random_y = random.randrange(0, 300)
                    self.score += 1
                    bar = Bar(self.random_x,self.random_y,self.image)
                    self.listPipe.append(bar)

                    pipe.drawBar(self.screen)

            self.screen.blit(self.background,[self.index,0])
            self.screen.blit(self.background,(self.image_width + self.index, 0))
            self.player.drawPlayer(self.screen)
            self.player.movePlayer(self.velocity)
            for pipe in self.listPipe:
                pipe.drawBar(self.screen)
            self.index -= 1
            if self.index == -self.image_width:
                self.index = 0
                self.screen.blit(self.background,(self.image_width + self.index,0))
            if not self.itsOver:
                for pipe in self.listPipe:
                    pipe.moveBar()
                self.player.gravity()
            self.fps.tick(60)
            self.drawScore()
            if self.itsOver:
                self.gameOver()
            pygame.draw.rect(self.screen,(255,0,0),self.rect_screen,1)
            self.player.rect.clamp_ip(self.rect_screen)
            pygame.display.flip()
if __name__ == '__main__':
    pygame.init()
    Game().main_screen()
