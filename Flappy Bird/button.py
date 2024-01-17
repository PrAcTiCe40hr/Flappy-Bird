import pygame


class Button:
    def __init__(self, image, x, y, action=None):
        """
        Initializes a new button.
        :param image: The image to be displayed on the button.
        :param x: The x-coordinate of the top-left corner of the button.
        :param y: The y-coordinate of the top-left corner of the button.
        :param action: The action to be performed when the button is clicked.
        """
        self.image = pygame.transform.rotozoom(image, 0, 2)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.action = action

    def draw(self, screen):
        """
        Draws the button on the specified screen.
        :param screen: The screen on which to draw the button.
        """
        screen.blit(self.image, self.rect)

    def is_clicked(self, event):
        """
        Checks if the button is clicked.
        :param event: The event to check.
        :return: True if the button is clicked, False otherwise.
        """
        if event.type == pygame.MOUSEBUTTONDOWN and (
                self.rect.collidepoint(event.pos)):
            return True
        return False
