import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from bird import Bird
from red_bird import RedBird
from blue_bird import BlueBird
from assets import load_assets
from game_functions import check_collision
from pipe import Pipe
from score_counter import ScoreCounter
from historic_score import HistoryScore
from render_button import create_buttons


def run_game():
    """
    Run the main game loop.

    This function initializes the game environment using Pygame, sets up game
    elements like the bird, pipes, score counter, etc., and enters the main
    game loop. Within the loop, it handles events, updates game states,
    checks for collisions, and updates the display. It continues until the
    game is exited.
    """
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    bg_x_pos = 0
    base_x_pos = 0
    bg_x_pos_2 = 288
    base_x_pos_2 = 336
    bg_x_pos_3 = 288 * 2
    base_x_pos_3 = 336 * 2

    assets = load_assets()
    score_counter = ScoreCounter()
    history_score = HistoryScore()
    buttons = create_buttons()
    bird_color = 'yellow'  # Default color

    bird = Bird()
    pipes = []
    for i in range(5):
        pipe = Pipe(SCREEN_WIDTH * 2 / 3 + i * 150)
        pipes.append(pipe)

    g_a = False
    g_e = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            for button in buttons:
                if button.is_clicked(event) and not g_a:
                    # Set bird color based on button clicked
                    bird_color = button.action
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not g_e and not g_a:
                    # Start the game when space key is pressed
                    g_a = True
                    if bird_color == 'red':
                        bird = RedBird()
                    elif bird_color == 'blue':
                        bird = BlueBird()
                    else:
                        bird = Bird()  # Default yellow bird
                    pipes = []
                    score_counter.reset()
                    bird.initiate()
            if event.type == pygame.KEYDOWN and g_a and not g_e:
                if event.key == pygame.K_SPACE:
                    bird.jump()

        # Load start screen and end screen depends on the status of the game
        screen.blit(assets["bg_surface"], (bg_x_pos, 0))
        screen.blit(assets["bg_surface"], (bg_x_pos_2, 0))
        screen.blit(assets["bg_surface"], (bg_x_pos_3, 0))
        screen.blit(assets["floor_surface"], (base_x_pos,
                                              SCREEN_HEIGHT - 300))
        screen.blit(assets["floor_surface"], (base_x_pos_2,
                                              SCREEN_HEIGHT - 300))
        screen.blit(assets["floor_surface"], (base_x_pos_3,
                                              SCREEN_HEIGHT - 300))
        bird.draw(screen)

        height_of_elements_above = 600
        rectangle_height = SCREEN_HEIGHT - height_of_elements_above
        # Draw the white rectangle
        pygame.draw.rect(screen, (109, 190, 200), (0, height_of_elements_above,
                                                   SCREEN_WIDTH,
                                                   rectangle_height))

        for button in buttons:
            button.draw(screen)

        if not g_a and not g_e:
            # Display assets["message"]
            screen.blit(assets["message"], (200, 150))

        if g_a:
            bird.update()
            g_e = check_collision(bird)

            # Scrolling both sets of background and base
            screen.blit(assets["bg_surface"], (bg_x_pos, 0))
            screen.blit(assets["bg_surface"], (bg_x_pos_2, 0))
            screen.blit(assets["bg_surface"], (bg_x_pos_3, 0))
            bg_x_pos -= 1
            bg_x_pos_2 -= 1
            bg_x_pos_3 -= 1

            # Pipe Creation
            if pipes:  # Check if the pipes list is not empty
                pipes.append(Pipe(pipes[-1].x_pos + 150))
            else:
                # Code to handle the situation when there are no pipes
                pipes.append(Pipe(SCREEN_WIDTH * 2 / 3))

            # Update and Draw Pipes
            for pipe in pipes:
                pipe.update()  # Update each pipe's position
                pipe.draw(screen)  # Draw each pipe to the screen
                if 100 > pipe.x_pos and not pipe.passed:
                    score_counter.increment()
                    pipe.passed = True

            # Collision Detection
            for pipe in pipes:
                if pipe.collide(bird.rect):
                    g_e = True

            pipes = [pipe for pipe in pipes if not pipe.check_off_screen()]
            screen.blit(assets["floor_surface"], (base_x_pos,
                                                  SCREEN_HEIGHT - 300))
            screen.blit(assets["floor_surface"], (base_x_pos_2,
                                                  SCREEN_HEIGHT - 300))
            screen.blit(assets["floor_surface"], (base_x_pos_3,
                                                  SCREEN_HEIGHT - 300))
            base_x_pos -= 1
            base_x_pos_2 -= 1
            base_x_pos_3 -= 1

            height_of_elements_above = 600
            rectangle_height = SCREEN_HEIGHT - height_of_elements_above
            # Draw the white rectangle
            pygame.draw.rect(screen, (109, 190, 200), (
                0, height_of_elements_above, SCREEN_WIDTH, rectangle_height)
            )

            # Immediate reset if off-screen
            if bg_x_pos <= -288:
                bg_x_pos = bg_x_pos_3 + 288
            if bg_x_pos_2 <= -288:
                bg_x_pos_2 = bg_x_pos + 288
            if bg_x_pos_3 <= -288:
                bg_x_pos_3 = bg_x_pos_2 + 288
            # Immediate reset if off-screen
            if base_x_pos <= -336:
                base_x_pos = base_x_pos_3 + 336
            if base_x_pos_2 <= -336:
                base_x_pos_2 = base_x_pos + 336
            if base_x_pos_3 <= -336:
                base_x_pos_3 = base_x_pos_2 + 336
            # Render the bird
            bird.draw(screen)
            # Render the score counter
            score_counter.draw(screen)

        if g_e:
            history_score.add_score(score_counter.score)
            screen.blit(assets["game_over"], (200, 150))
            pygame.display.update()
            pygame.time.wait(2000)
            g_e = False
            g_a = False
            screen.blit(assets["message"], (200, 150))

        history_score.draw_highest_score(screen)

        pygame.display.update()
        from settings import FPS
        clock.tick(FPS)


if __name__ == '__main__':
    run_game()
