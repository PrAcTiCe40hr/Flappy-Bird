# game_functions.py
from settings import SCREEN_HEIGHT


def check_collision(bird):
    if bird.rect.bottom >= SCREEN_HEIGHT - 312 or bird.rect.top <= 0:
        return True
    return False
