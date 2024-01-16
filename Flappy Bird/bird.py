# bird.py
import pygame
from settings import GRAVITY, SCREEN_HEIGHT


class Bird:
    def __init__(self):
        self.images = {
            "midflap": pygame.image.load("assets/sprites/yellowbird-midflap.png").convert_alpha(),
            "upflap": pygame.image.load("assets/sprites/yellowbird-upflap.png").convert_alpha(),
            "downflap": pygame.image.load("assets/sprites/yellowbird-downflap.png").convert_alpha()
        }
        self.current_image = self.images["midflap"]
        self.flap_state = 0  # To keep track of flap cycle
        self.rect = self.current_image.get_rect(center=(100, SCREEN_HEIGHT // 2))
        self.movement = 0

    def update_flap(self):
        flap_sequence = ["midflap", "upflap", "downflap"]
        self.flap_state = (self.flap_state + 1) % 3
        self.current_image = self.images[flap_sequence[self.flap_state]]

    def update(self):
        self.movement += GRAVITY
        self.rect.centery += self.movement
        self.update_flap()

    def jump(self):
        self.movement = 0
        self.movement -= 7

    def draw(self, screen):
        screen.blit(self.current_image, self.rect)

    def initiate(self):
        self.rect = self.current_image.get_rect(center=(100, SCREEN_HEIGHT // 2))