import unittest
from bird import Bird  # Adjust the import path based on your project structure
import pygame

class TestBird(unittest.TestCase):
    def setUp(self):
        pygame.init()
        pygame.display.set_mode((50, 50))  # Set a small dummy display
        self.bird = Bird()


    def test_init(self):
        # Test the __init__ method
        self.assertIsNotNone(self.bird.images, "Bird images should not be None after initialization")
        self.assertIn("midflap", self.bird.images, "Bird images should include 'midflap' state")

    def test_update_flap(self):
        # Test the update_flap method
        initial_flap_state = self.bird.flap_state
        self.bird.update_flap()
        self.assertNotEqual(initial_flap_state, self.bird.flap_state, "Flap state should change after update_flap")

    def test_jump(self):
        # Test the jump methodxw
        initial_velocity = self.bird.movement
        self.bird.jump()
        self.assertNotEqual(initial_velocity, self.bird.movement, "Bird's velocity should change after jump")

    def test_draw(self):
        # Test the draw method - Requires a Pygame screen object
        screen = pygame.display.set_mode((800, 600))  # Dummy screen for testing
        self.bird.draw(screen)
        # Note: This is a basic test to ensure the method runs; more detailed tests may require visual confirmation

    def test_initiate(self):
        # Test the initiate method
        self.bird.jump()  # Alter the bird's state
        self.bird.initiate()
        self.assertEqual(self.bird.movement, -7, "Bird's velocity should be reset to 0 after initiate")

    def tearDown(self):
        # Clean up after each test
        pygame.quit()

if __name__ == '__main__':
    unittest.main()
