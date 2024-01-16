# assets.py
import pygame

def load_assets():
    assets = {}
    assets["bg_surface"] = pygame.image.load('Flappy Bird/assets/sprites/background-day.png').convert()
    assets["floor_surface"] = pygame.image.load('Flappy Bird/assets/sprites/base.png').convert()
    assets["message"] = pygame.image.load('Flappy Bird/assets/sprites/message.png').convert_alpha()
    assets["game_over"] = pygame.image.load('Flappy Bird/assets/sprites/gameover.png').convert_alpha()
    assets["pipe_up"] = pygame.image.load('Flappy Bird/assets/sprites/pipe-green-up.png').convert_alpha()
    assets["pipe_down"] = pygame.image.load('Flappy Bird/assets/sprites/pipe-green-down.png').convert_alpha()
    return assets
