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
kill_count = 0
can_kill = False

while running:
    clock.tick(FPS)
    screen.fill((255, 255, 255))

    x, y = pygame.mouse.get_pos()

    if random.randint(0, SPAWN_RATE) == 0 and len(enemies) < SPAWN_CAP:
        enemies.append(enemy.Enemy())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    

    
    for obs in enemies:
       
        if x >= obs.rect.x and x <= obs.rect.x + obs.radius and y >= obs.rect.y and y <= obs.rect.y + obs.radius:
            if can_kill == True and pygame.mouse.get_pressed() == (1, 0, 0):
                obs.dead = True
                enemies.remove(obs)
                kill_count+=1
                can_kill = False
            if pygame.mouse.get_pressed() == (0, 0, 0):
                can_kill = True
        obs.update(screen, player)
        

        

    keys = pygame.key.get_pressed()
    
    player.update(screen, keys)
    
    
    pygame.display.update()
    