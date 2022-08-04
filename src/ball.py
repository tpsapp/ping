import pygame, random
import settings
from pygame.math import Vector2

class BALL:
    def __init__(self) -> None:
        self.width = 30
        self.height = 30
        self.respawn()

    def draw(self, screen):
        pygame.draw.ellipse(screen, settings.white, self.rect)

    def update(self):
        self.pos += self.speed
        self.rect = pygame.rect.Rect(self.pos.x, self.pos.y, self.width, self.height)

    def respawn(self):
        self.pos = Vector2((settings.screen_width / 2) - (self.width / 2), (settings.screen_height / 2) - (self.height / 2))
        self.rect = pygame.rect.Rect(self.pos.x, self.pos.y, self.width, self.height)
        self.speed = Vector2(7, 7)
        self.speed.x *= random.choice((1, -1))
        self.speed.y *= random.choice((1, -1))
