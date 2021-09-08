import pygame
from src.constants import SCREEN_W, SCREEN_H, FPS
from pygame import QUIT
from src.game import Game

def main():

    pygame.init()

    display = pygame.display.set_mode((SCREEN_W, SCREEN_H), 0, 32)
    font = pygame.font.SysFont("Arial", 24)

    # basic skeleton of game loop
    running = True
    game = Game()
    # calculate Delta
    gameClock = pygame.time.Clock()
    while running:
        # tick is function to calculate delta
        # FPS is optional argument for framerate
        delta = gameClock.tick(FPS)

        events = pygame.event.get()
        # process input
        game.handleInput(events)
        # update game world
        game.update(delta)
        # render game world
        game.render(display, font)

        # makes sure what is being rendered is being updated
        pygame.display.update()

        for e in events:
            if e.type == QUIT:
                running = False
        # somehow quit. If they press a button, and == quit, then running = false



if __name__ == "__main__":
    main()