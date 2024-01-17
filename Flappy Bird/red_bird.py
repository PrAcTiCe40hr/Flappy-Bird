import pygame
from bird import Bird


class RedBird(Bird):
    def __init__(self):
        super().__init__()
        self.images = {
            "midflap": pygame.image.load(
                "assets/sprites/redbird-midflap.png"
            ).convert_alpha(),
            "upflap": pygame.image.load(
                "assets/sprites/redbird-upflap.png"
            ).convert_alpha(),
            "downflap": pygame.image.load(
                "assets/sprites/redbird-downflap.png"
            ).convert_alpha()
        }
        self.current_image = self.images["midflap"]
