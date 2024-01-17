import pygame
from settings import SCREEN_HEIGHT
from button import Button


def create_buttons():
    buttons = []
    bird_images = {
        'red': pygame.image.load(
            'assets/sprites/redbird-midflap.png'
        ).convert_alpha(),
        'blue': pygame.image.load(
            'assets/sprites/bluebird-midflap.png'
        ).convert_alpha(),
        'yellow': pygame.image.load(
            'assets/sprites/yellowbird-midflap.png'
        ).convert_alpha()
    }
    x, y = 160, SCREEN_HEIGHT - 125  # Adjust position as needed
    for color, img in bird_images.items():
        button = Button(img, x, y, action=color)
        buttons.append(button)
        x += 100  # Adjust spacing as needed
    return buttons
