import pygame
from sys import exit


pygame.init()

screen = pygame.display.set_mode((500,600))
clock = pygame.time.Clock()


player_surface = pygame.image.load('img/player_1.png').convert_alpha()
player_rect = player_surface.get_rect(center = (250, 500))

block1_surface = pygame.image.load('img/block.png').convert_alpha()
block1_rect = block1_surface.get_rect(center = (400, 500))

block2_surface = pygame.image.load('img/block.png').convert_alpha()
block2_rect = block2_surface.get_rect(center = (100, 500))

aceleration = 0
touch = True
right = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                right = True
                touch = False
                print('telca')
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                right = False
                touch = False
                print('telca')
        
    pygame.display.update()
    if right:
        if not touch:
                aceleration += 2
                player_rect.x += aceleration
        
        if player_rect.colliderect(block1_rect):
            player_rect.center = block1_rect.center
            touch = True
            aceleration = 0
    if not right:
        if not touch:
                aceleration -= -2
                player_rect.x -= aceleration
        
        if player_rect.colliderect(block2_rect):
            player_rect.center = block2_rect.center
            touch = True
            aceleration = 0

    screen.fill((30, 30, 30))
    screen.blit(block1_surface, block1_rect)
    screen.blit(block2_surface, block2_rect)
    screen.blit(player_surface, player_rect)
    clock.tick(60)