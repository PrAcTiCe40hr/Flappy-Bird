import random
from assets import load_assets
from settings import SCREEN_WIDTH, DIFFICULTY


class Pipe:
    def __init__(self, x_pos):
        # Load assets
        assets = load_assets()
        # Load the pipe images
        self.top_pipe_image = assets["pipe_up"]
        self.bottom_pipe_image = assets["pipe_down"]

        # Set the initial position and dimensions of the pipes
        self.x_pos = x_pos  # Start at 1/2 of the screen
        self.height = random.randint(200, 380)  # Random height for the gap between pipes
        self.gap = 175  # Gap between top and bottom pipe
        self.passed = False
        # Set the rect for collision detection
        self.top_rect = self.top_pipe_image.get_rect(midbottom=(self.x_pos, self.height - self.gap / 2))
        self.bottom_rect = self.bottom_pipe_image.get_rect(midtop=(self.x_pos, self.height + self.gap / 2))

        self.movement_speed = DIFFICULTY  # Speed at which the pipes move

    def update(self):
        # Move the pipes
        self.x_pos -= self.movement_speed
        self.top_rect.x = self.x_pos
        self.bottom_rect.x = self.x_pos

    def draw(self, screen):
        # Draw the pipes on the screen
        screen.blit(self.top_pipe_image, self.top_rect)
        screen.blit(self.bottom_pipe_image, self.bottom_rect)

    def collide(self, bird_rect):
        # Check for collision with the bird
        if (self.top_rect.colliderect(bird_rect) or self.bottom_rect.colliderect(bird_rect)):
            return True
        return False

    def check_off_screen(self):
        if(self.x_pos <= -50):
            return True
        return False
