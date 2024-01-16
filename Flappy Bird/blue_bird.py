
# blue_bird.py
import pygame
from bird import Bird

class BlueBird(Bird):
    def __init__(self):
        super().__init__()
        self.images = {
            "midflap": pygame.image.load("assets/sprites/bluebird-midflap.png").convert_alpha(),
            "upflap": pygame.image.load("assets/sprites/bluebird-upflap.png").convert_alpha(),
            "downflap": pygame.image.load("assets/sprites/bluebird-downflap.png").convert_alpha()
        }
        self.current_image = self.images["midflap"]
