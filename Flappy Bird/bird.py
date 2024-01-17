import pygame
from settings import GRAVITY, SCREEN_HEIGHT


class Bird:
    """
    A class representing the bird character in the game.

    This class is responsible for initializing and managing the state
    and behavior of the bird character.
    It loads different sprites for the bird's various flap states
    (midflap, upflap, downflap) and includes methods for
    handling the bird's movement and interaction with the game environment.

    Attributes:
        images (dict): A dictionary containing the loaded images for each
        flap state of the bird.
    """

    def __init__(self):
        """
        Initialize the Bird object.

        Loads and stores the bird's sprite images for different flap states
        using the Pygame library.
        """
        self.images = {
            "midflap": pygame.image.load(
                "assets/sprites/yellowbird-midflap.png"
            ).convert_alpha(),
            "upflap": pygame.image.load(
                "assets/sprites/yellowbird-upflap.png"
            ).convert_alpha(),
            "downflap": pygame.image.load(
                "assets/sprites/yellowbird-downflap.png"
            ).convert_alpha()
        }
        self.current_image = self.images["midflap"]
        self.flap_state = 0  # To keep track of flap cycle
        self.rect = self.current_image.get_rect(center=(100,
                                                        SCREEN_HEIGHT // 2))
        self.movement = 0

    def update_flap(self):
        """
        Update the bird's flap state.

        This method changes the bird's sprite to simulate flapping.
        It should be called periodically to create a flapping animation.
        """
        flap_sequence = ["midflap", "upflap", "downflap"]
        self.flap_state = (self.flap_state + 1) % 3
        self.current_image = self.images[flap_sequence[self.flap_state]]

    def update(self):
        """
        Update the bird's state.

        This method updates the bird's position and state,
        typically called on each frame of the game to handle movements
        and game physics.
        """
        self.movement += GRAVITY
        self.rect.centery += self.movement
        self.update_flap()

    def jump(self):
        """
        Make the bird jump.

        This method alters the bird's vertical position or velocity to
        simulate a jump, typically triggered by player input.
        """
        self.movement = 0
        self.movement -= 7

    def draw(self, screen):
        """
        Draw the bird on the screen.

        Args:
            screen: The Pygame screen object where the bird will be drawn.

        This method renders the bird's current sprite on the provided screen.
        """
        screen.blit(self.current_image, self.rect)

    def initiate(self):
        """
        Initiate the bird's settings.

        This method is used to set or reset the bird's attributes to their
        initial values, often used at the start of the game or after a game
        over.
        """
        self.rect = self.current_image.get_rect(center=(100,
                                                        SCREEN_HEIGHT // 2))
