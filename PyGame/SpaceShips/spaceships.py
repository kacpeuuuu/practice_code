import pygame
import os
import random
pygame.init()
size = width, height = 900, 600
screen = pygame.display.set_mode((size))
clock = pygame.time.Clock()
spaceship_width, spaceship_height = 55, 40
background =  pygame.image.load(r'Git Repo\PyGame\SpaceShips\Assets\space.png')


player_spaceship_image = pygame.image.load(r'Git Repo\PyGame\SpaceShips\Assets\spaceship_yellow.png')
player_spaceship_image = pygame.transform.rotate(pygame.transform.scale(player_spaceship_image, (55, 40)), 90)


enemy_spaceship_image = pygame.image.load(r'Git Repo\PyGame\SpaceShips\Assets\spaceship_red.png')
enemy_spaceship_image = pygame.transform.rotate(pygame.transform.scale(enemy_spaceship_image, (55, 40)), 270)

def draw_screen(surface):
    surface.blit(background, (-100, 0))
    surface.blit(player_spaceship_image, (100, 300))
    surface.blit(enemy_spaceship_image, (800, 300))

    pygame.display.update()


def main():
    running = True
    clock.tick(30)
    draw_screen(screen)
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
main()

