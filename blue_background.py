import sys
import pygame

class BlueBackground():
    """Создание окна с синим фоном"""
    
    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode((1400,800))
        pygame.display.set_caption("Blue Background")
        
        self.bg_color = (0, 191, 255)
        
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
        
            self.screen.fill(self.bg_color)
            pygame.display.flip()
            
if __name__ == '__main__':
    bg = BlueBackground()
    bg.run_game()
