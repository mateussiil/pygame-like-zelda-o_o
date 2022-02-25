import pygame, sys
import pygame.freetype  # Import the freetype module.

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode()
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
            self.screen.fill('black')
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()