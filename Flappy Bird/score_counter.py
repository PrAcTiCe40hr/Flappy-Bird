import pygame
from settings import SCREEN_WIDTH  # Assuming you have this constant defined


class ScoreCounter:
    def __init__(self, asset_path="assets/sprites/{}.png",
                 position=(SCREEN_WIDTH // 2, 50)):
        self.score = 0
        self.position = position
        self.digit_images = [pygame.image.load(asset_path.format(i))
                             for i in range(10)]

    def increment(self, value=1):
        """ Increments the score by a given value. """
        self.score += value

    def reset(self):
        """ Resets the score to zero. """
        self.score = 0

    def draw(self, screen):
        """ Draws the score on the screen using loaded assets. """
        score_str = str(self.score)
        total_width = sum(self.digit_images[int(digit)].get_width()
                          for digit in score_str)
        start_x = self.position[0] - total_width // 2

        x_offset = start_x
        for digit in score_str:
            digit_image = self.digit_images[int(digit)]
            screen.blit(digit_image, (x_offset, self.position[1]))
            x_offset += digit_image.get_width()
