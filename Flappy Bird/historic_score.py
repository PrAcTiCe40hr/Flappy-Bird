import os
import pygame
from settings import SCREEN_WIDTH


class HistoryScore:
    def __init__(self, asset_path="assets/sprites/{}.png",
                 position=(SCREEN_WIDTH // 2, 750),
                 file_path='highest_score.txt'):
        """
        Initialize the HistoryScore object.

        Args:
            asset_path (str): The path to the assets used for displaying 
            scores.
            position (tuple): The position on the screen where the score will 
            be displayed.
            file_path (str): The file path for storing and retrieving the 
            highest score.

        This method sets up the necessary attributes for managing and
        displaying historic scores.
        """
        self.file_path = file_path
        self.highest_score = self.load_highest_score()
        self.scores = []
        self.position = position
        self.digit_images = [pygame.image.load(asset_path.format(i))
                             for i in range(10)]

    def add_score(self, score):
        """
        Add a new score to the history.

        Args:
            score (int): The score to be added to the history.

        This method updates the score history with the new score and 
        checks if it's a new highest score.
        """
        if score > self.highest_score:
            self.highest_score = score
            self.save_highest_score()

    def get_highest_score(self):
        """
        Retrieve the highest score.

        Returns:
            int: The highest score recorded in the history.

        This method returns the highest score from the stored score history.
        """
        return self.highest_score

    def save_highest_score(self):
        """
        Save the highest score to a file.

        This method writes the current highest score to a file for persistent
        storage.
        """
        with open(self.file_path, 'w') as file:
            file.write(str(self.highest_score))

    def load_highest_score(self):
        """
        Load the highest score from a file.

        Returns:
            int: The highest score loaded from the file.

        This method reads the highest score from a file and updates the
        history accordingly.
        """
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                return int(file.read())
        return 0

    def draw_highest_score(self, screen):
        """
        Draw the highest score on the screen.

        Args:
            screen: The Pygame screen object where the highest score will 
            be displayed.

        This method renders the highest score on the provided screen, using
        the preloaded digit images.
        """
        highest_score = self.get_highest_score()
        score_str = str(highest_score)
        total_width = sum(self.digit_images[int(digit)].get_width()
                          for digit in score_str)
        start_x = self.position[0] - total_width // 2

        x_offset = start_x
        for digit in score_str:
            digit_image = self.digit_images[int(digit)]
            screen.blit(digit_image, (x_offset, self.position[1]))
            x_offset += digit_image.get_width()
