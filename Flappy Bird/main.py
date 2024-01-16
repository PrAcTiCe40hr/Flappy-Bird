# main.py
import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from bird import Bird
from assets import load_assets
from game_functions import check_collision
from pipe import Pipe
from score_counter import ScoreCounter

def run_game():
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
    bird = Bird()
    pipes = [Pipe()]

    game_active = False
    game_end = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not game_active:
                    game_active = True  # Start the game when space key is pressed
                    game_end = False
                    pipes = []
                    score_counter.reset()
                    bird.initiate()
            if event.type == pygame.KEYDOWN and game_active and not game_end:
                if event.key == pygame.K_SPACE:
                    bird.jump()
                    
        # Load start screen and end screen depends on the status of the game
        screen.blit(assets["bg_surface"], (bg_x_pos, 0))
        screen.blit(assets["bg_surface"], (bg_x_pos_2, 0))
        screen.blit(assets["bg_surface"], (bg_x_pos_3, 0))
        screen.blit(assets["floor_surface"], (base_x_pos, SCREEN_HEIGHT - 300))
        screen.blit(assets["floor_surface"], (base_x_pos_2, SCREEN_HEIGHT - 300))
        screen.blit(assets["floor_surface"], (base_x_pos_3, SCREEN_HEIGHT - 300))
        bird.draw(screen)
        if(not game_active):
            screen.blit(assets["message"], (200, 150))
        
        if game_active:
            bird.update()
            game_end = check_collision(bird)
            if(game_end):  # Check if game ends
                game_active = False
                game_end = True
                screen.blit(assets["game_over"], (200, 150))
                screen.blit(assets["message"], (200, 150))
                
            # Scrolling both sets of background and base
            screen.blit(assets["bg_surface"], (bg_x_pos, 0))
            screen.blit(assets["bg_surface"], (bg_x_pos_2, 0))
            screen.blit(assets["bg_surface"], (bg_x_pos_3, 0))
            bg_x_pos -= 1
            bg_x_pos_2 -= 1
            bg_x_pos_3 -= 1
            
            # Pipe Creation
            if not pipes or pipes[-1].x_pos < (SCREEN_WIDTH * 1 / 2) - 150:
                pipes.append(Pipe())  # Add a new pipe to the list

            # Update and Draw Pipes
            for pipe in pipes:
                pipe.update()  # Update each pipe's position
                pipe.draw(screen)  # Draw each pipe to the screen
                if(pipe.x_pos < 100):
                    score_counter.increment()

            # Collision Detection
            for pipe in pipes:
                if pipe.collide(bird.rect):
                    game_active = False
                    game_end = True
                    screen.blit(assets["game_over"], (200, 150))
                    screen.blit(assets["message"], (200, 150))
                    
            pipes = [pipe for pipe in pipes if not pipe.check_off_screen()]
            
                   
            screen.blit(assets["floor_surface"], (base_x_pos, SCREEN_HEIGHT - 300))
            screen.blit(assets["floor_surface"], (base_x_pos_2, SCREEN_HEIGHT - 300))
            screen.blit(assets["floor_surface"], (base_x_pos_3, SCREEN_HEIGHT - 300))
            base_x_pos -= 1
            base_x_pos_2 -= 1
            base_x_pos_3 -= 1
            
            height_of_elements_above = 600
            rectangle_height = SCREEN_HEIGHT - height_of_elements_above
            # Draw the white rectangle
            pygame.draw.rect(screen, (0,0,0), (0, height_of_elements_above, SCREEN_WIDTH, rectangle_height))
            
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
                base_x_pos_3 = base_x_pos_2  + 336
            # Render the bird
            bird.draw(screen)
            # Render the score counter
            score_counter.draw(screen)


        pygame.display.update()
        from settings import FPS
        clock.tick(FPS)

if __name__ == '__main__':
    run_game()
