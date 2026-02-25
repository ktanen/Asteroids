import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    ship = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT /2)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        ship.update(dt)
        screen.fill("black")
        ship.draw(screen)

        pygame.display.flip()
        milliseconds = clock.tick(60)
        dt = milliseconds / 1000
        
if __name__ == "__main__":
    main()
