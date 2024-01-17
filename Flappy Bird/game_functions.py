from settings import SCREEN_HEIGHT


def check_collision(bird):
    """
    Check for a collision involving the bird.

    Args:
        bird: The Bird object to check for collisions.

    This function determines if the bird has collided with the ground or 
    has gone out of bounds (off the screen).
    It returns True if a collision has occurred, otherwise False.
    """
    if bird.rect.bottom >= SCREEN_HEIGHT - 312 or bird.rect.top <= 0:
        return True
    return False
