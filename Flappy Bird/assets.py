import pygame


def load_assets():
    """
    Load game assets from the specified file paths.

    This function initializes a dictionary of assets and loads various
    game assets such as background, floor, messages, game over screen,
    and pipes using the Pygame library.
    Each asset is loaded from a specified file path and converted for
    optimal performance in Pygame.
    Some assets also use the convert_alpha() method for handling
    transparency.

    Returns:
        dict: A dictionary containing all the loaded game assets,
        each referenced by a descriptive key.
    """
    assets = {}
    assets["bg_surface"] = pygame.image.load(
        'assets/sprites/background-day.png'
    ).convert()
    assets["floor_surface"] = pygame.image.load(
        'assets/sprites/base.png'
    ).convert()
    assets["message"] = pygame.image.load(
        'assets/sprites/message.png'
    ).convert_alpha()
    assets["game_over"] = pygame.image.load(
        'assets/sprites/gameover.png').convert_alpha()
    assets["pipe_up"] = pygame.image.load(
        'assets/sprites/pipe-green-up.png'
    ).convert_alpha()
    assets["pipe_down"] = pygame.image.load(
        'assets/sprites/pipe-green-down.png'
    ).convert_alpha()
    return assets
