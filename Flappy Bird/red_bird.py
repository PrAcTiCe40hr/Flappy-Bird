import pygame
from bird import Bird


class RedBird(Bird):
    def __init__(self):
        """
        Initialize the RedBird object.

        This constructor initializes the RedBird by calling the constructor of
        the Bird class and then setting up the specific sprites for the 
        RedBird. It loads and assigns different sprite images for the
        RedBird's various flap states like midflap, upflap, and downflap.
        """
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
