import sys
import pygame
import settings
from ball import BALL
from paddle import PADDLE
from pygame.math import Vector2

class GAME:
    def __init__(self, screen) -> None:
        self.ball = BALL()
        self.player = PADDLE('right')
        self.opponent = PADDLE('left')
        self.screen = screen
        self.font = pygame.font.SysFont(settings.font_face, settings.font_size)
        self.paused = True

    def update(self):
        if not self.paused:
            self.collision_check()
            self.check_for_win()
            self.ball.update()
            self.player.update()
            self.opponent.process_ai(self.ball.pos.y)
            self.opponent.update()

    def draw(self):
        self.draw_net()
        self.draw_score()
        self.ball.draw(self.screen)
        self.player.draw(self.screen)
        self.opponent.draw(self.screen)
        if self.paused:
            pause_text = self.font.render("Press Space to Continue", True, settings.white)
            pt_rect = pause_text.get_rect(center = (settings.screen_width / 2, settings.screen_height - settings.font_size))
            self.screen.blit(pause_text, pt_rect)

    def collision_check(self):
        if self.ball.rect.top <= 0 or self.ball.rect.bottom >= settings.screen_height:
            self.ball.speed.y *= -1
        if self.ball.rect.left <= 0:
            self.player.score += 1
            self.ball.respawn()
        if self.ball.rect.right >= settings.screen_width:
            self.opponent.score += 1
            self.ball.respawn()
        if self.ball.rect.colliderect(self.player.rect) or self.ball.rect.colliderect(self.opponent.rect):
            self.ball.speed.x *= -1

    def draw_net(self):
        pygame.draw.aaline(self.screen, settings.blue, (settings.screen_width / 2, 0), (settings.screen_width / 2, settings.screen_height))

    def handle_keydown(self, key):
        # if key == pygame.K_w:
        #     self.opponent.speed -= 7
        # if key == pygame.K_s:
        #     self.opponent.speed += 7
        if key == pygame.K_UP:
            self.player.speed -= 10
        if key == pygame.K_DOWN:
            self.player.speed += 10
        if key == pygame.K_SPACE:
            self.paused = not self.paused

    def handle_keyup(self, key):
        # if key == pygame.K_w:
        #     self.opponent.speed += 7
        # if key == pygame.K_s:
        #     self.opponent.speed -= 7
        if key == pygame.K_UP:
            self.player.speed += 10
        if key == pygame.K_DOWN:
            self.player.speed -= 10

    def draw_score(self):
        player_score = self.font.render(str(self.player.score), True, settings.white)
        ps_rect = player_score.get_rect(center = (settings.screen_width * 0.75, settings.font_size))
        opponent_score = self.font.render(str(self.opponent.score), True, settings.white)
        os_rect = opponent_score.get_rect(center = (settings.screen_width * 0.25, settings.font_size))
        self.screen.blit(player_score, ps_rect)
        self.screen.blit(opponent_score, os_rect)

    def check_for_win(self):
        if self.player.score == 5 or self.opponent.score == 5:
            self.paused = True
            self.player.respawn()
            self.opponent.respawn()
            self.ball.respawn()
