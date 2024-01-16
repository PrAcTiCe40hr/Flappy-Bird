# bird.py
import pygame
from settings import GRAVITY, SCREEN_HEIGHT

class Bird:
    def __init__(self):
        self.image = pygame.image.load('Flappy Bird/assets/sprites/yellowbird-midflap.png').convert_alpha()
        self.rect = self.image.get_rect(center=(100, SCREEN_HEIGHT // 2))
        self.movement = 0

    def update(self):
        self.movement += GRAVITY
        self.rect.centery += self.movement

    def jump(self):
        self.movement = 0
        self.movement -= 7

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def initiate(self):
        self.rect = self.image.get_rect(center=(100, SCREEN_HEIGHT // 2))