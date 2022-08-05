import pygame
import sys
import settings
from game import GAME

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode(
    (settings.screen_width, settings.screen_height))
pygame.display.set_caption(settings.screen_caption)
game = GAME(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            game.handle_keydown(event.key)
        if event.type == pygame.KEYUP:
            game.handle_keyup(event.key)

    game.update()
    screen.fill(settings.black)
    game.draw()
    pygame.display.flip()
    clock.tick(settings.framerate)
