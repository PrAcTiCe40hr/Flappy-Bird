import pygame
from bird import Bird


class BlueBird(Bird):
    """
    A subclass of the Bird class representing a specific blue bird character
    in the game.
    This class extends the functionality of the Bird class, specializing it
    for a blue bird character. It overrides the initialization method to load
    specific sprite images for the blue bird's various flap states.

    Attributes:
        images (dict): A dictionary containing the loaded images for each flap state of the blue bird.
    """

    def __init__(self):
        """
        Initialize the BlueBird object.

        Calls the superclass initializer and then loads and stores the
        blue bird's sprite images for different flap states using the
        Pygame library.
        """
        super().__init__()
        self.images = {
            "midflap": pygame.image.load(
                "assets/sprites/bluebird-midflap.png"
            ).convert_alpha(),
            "upflap": pygame.image.load(
                "assets/sprites/bluebird-upflap.png"
            ).convert_alpha(),
            "downflap": pygame.image.load(
                "assets/sprites/bluebird-downflap.png"
            ).convert_alpha()
        }
        self.current_image = self.images["midflap"]
