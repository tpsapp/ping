import pygame
import settings
from pygame.math import Vector2


class PADDLE:
    def __init__(self, side) -> None:
        self.width = 10
        self.height = 140
        self.side = side
        self.respawn()

    def draw(self, screen):
        pygame.draw.rect(screen, settings.white, self.rect)

    def update(self):
        self.pos.y += self.speed
        self.rect = pygame.rect.Rect(
            self.pos.x, self.pos.y, self.width, self.height)
        if self.rect.top <= 0:
            self.pos.y = 0
            self.rect = pygame.rect.Rect(
                self.pos.x, self.pos.y, self.width, self.height)
        if self.rect.bottom >= settings.screen_height:
            self.pos.y = settings.screen_height - self.height
            self.rect = pygame.rect.Rect(
                self.pos.x, self.pos.y, self.width, self.height)

    def respawn(self):
        if self.side == 'left':
            self.pos = Vector2(0 + (self.width / 2) + 10,
                               (settings.screen_height / 2) - (self.height / 2))
        else:
            self.pos = Vector2(settings.screen_width - (self.width / 2) -
                               20, (settings.screen_height / 2) - (self.height / 2))
        self.rect = pygame.rect.Rect(
            self.pos.x, self.pos.y, self.width, self.height)
        self.speed = 0
        self.score = 0

    def process_ai(self, ball_y):
        if self.rect.top < ball_y:
            self.speed += 3
        if self.rect.bottom > ball_y:
            self.speed -= 3
