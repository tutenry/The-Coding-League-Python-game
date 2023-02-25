import pygame
from constants import *
import math

class Square():

    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT //2
        self.width = 40
        self.height = 40
        self.xvel = 0
        self.yvel = 0
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.dead = False

    def update(self, screen, keys):
        if self.dead == False:
            return
        self.draw(screen)
        self.move(keys)
        self.check_collision()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def destroy(self):
        self.dead = True
    
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))

    def move(self, keys):

        if keys[pygame.K_a]:
            self.xvel -= 1
        if keys[pygame.K_d]:
            self.xvel += 1
        if keys[pygame.K_w]:
            self.yvel -= 1
        if keys[pygame.K_s]:
            self.yvel += 1
        
        if self.xvel < -10:
            self.xvel = -10
        elif self.xvel > 10:
            self.xvel = 10
        if self.yvel < -10:
            self.yvel = -10
        elif self.yvel > 10:
            self.yvel = 10
            
        self.xvel *= 0.99
        self.yvel *= 0.99
        
        self.x += self.xvel
        self.y += self.yvel
    
    def check_collision(self):
        if self.x + self.width > SCREEN_WIDTH :
            self.x = SCREEN_WIDTH - self.width
            self.xvel *= -1
        elif self.x < 0:
            self.x = 0
            self.xvel *= -1
        if self.y + self.height > SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT - self.height
            self.yvel *= -1
        elif self.y < 0:
            self.y = 0
            self.yvel *= -1
