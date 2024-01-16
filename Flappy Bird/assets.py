# assets.py
import pygame


def load_assets():
    assets = {}
    assets["bg_surface"] = pygame.image.load('assets/sprites/background-day.png').convert()
    assets["floor_surface"] = pygame.image.load('assets/sprites/base.png').convert()
    assets["message"] = pygame.image.load('assets/sprites/message.png').convert_alpha()
    assets["game_over"] = pygame.image.load('assets/sprites/gameover.png').convert_alpha()
    assets["pipe_up"] = pygame.image.load('assets/sprites/pipe-green-up.png').convert_alpha()
    assets["pipe_down"] = pygame.image.load('assets/sprites/pipe-green-down.png').convert_alpha()
    return assets
