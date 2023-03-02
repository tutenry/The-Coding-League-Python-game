import pygame
from constants import *
import square
import random
import enemy

pygame.init()



screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running = True

clock = pygame.time.Clock()
player = square.Square()
enemies = []

while running:
    clock.tick(FPS)
    screen.fill((255, 255, 255))

    if random.randint(0, 100) == 0 and len(enemies) < 10:
        enemies.append(enemy.Enemy())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    for obs in enemies:
        obs.update(screen, player)

    keys = pygame.key.get_pressed()
    
    player.update(screen, keys)
    
    
    pygame.display.update()