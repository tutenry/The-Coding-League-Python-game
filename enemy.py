import pygame
from constants import *
import random

class Enemy():

    def __init__(self):
        self.radius = 25

        num = random.randint(0,1)
        if num == 0:
            self.x = 0 - self.radius
        else:
            self.x = SCREEN_WIDTH

        self.y = random.randint(0, SCREEN_HEIGHT - self.radius)
        self.xvel = 0
        self.yvel = 0
        self.rect = pygame.Rect(self.x, self.y, self.radius, self.radius)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def update(self, screen, player):
        self.draw(screen)
        self.follow(player)
        self.rect = pygame.Rect(self.x-self.radius/2, self.y-self.radius/2, self.radius, self.radius)
        self.check_collision(player)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def follow(self, player):
        if player.x > self.x:
            self.xvel += .1
        elif player.x < self.x:
            self.xvel -= .1
        if player.y > self.y:
            self.yvel += .1
        elif player.y < self.y:
            self.yvel -= .1

        if self.xvel < -1:
            self.xvel = -1
        elif self.xvel > 1:
            self.xvel = 1
        if self.yvel < -1:
            self.yvel = -1
        elif self.yvel > 1:
            self.yvel = 1
        
        self.x += self.xvel
        self.y += self.yvel
    
    def check_collision(self, player):
        if self.rect.colliderect(player.rect):
            player.destroy()

