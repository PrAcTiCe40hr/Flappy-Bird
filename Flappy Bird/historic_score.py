import os
import pygame
from settings import SCREEN_WIDTH


class HistoryScore:
    def __init__(self, asset_path="assets/sprites/{}.png", position=(SCREEN_WIDTH // 2, 750), file_path='highest_score.txt'):
        self.file_path = file_path
        self.highest_score = self.load_highest_score()
        self.scores = []
        self.position = position
        self.digit_images = [pygame.image.load(asset_path.format(i)) for i in range(10)]

    def add_score(self, score):
        if score > self.highest_score:
            self.highest_score = score
            self.save_highest_score()

    def get_highest_score(self):
        return self.highest_score

    def save_highest_score(self):
        with open(self.file_path, 'w') as file:
            file.write(str(self.highest_score))

    def load_highest_score(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                return int(file.read())
        return 0

    def draw_highest_score(self, screen):
        highest_score = self.get_highest_score()      
        score_str = str(highest_score)
        total_width = sum(self.digit_images[int(digit)].get_width() for digit in score_str)
        start_x = self.position[0] - total_width // 2

        x_offset = start_x
        for digit in score_str:
            digit_image = self.digit_images[int(digit)]
            screen.blit(digit_image, (x_offset, self.position[1]))
            x_offset += digit_image.get_width()