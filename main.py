import threading

import pygame

import collideImplementation
from domain import game as gm

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

game = gm.Game(500, 1000, 25, collideImplementation.CollideImplementation())


def repeat_each_second():
    game.move(down=True)
    threading.Timer(1.0, repeat_each_second).start()


repeat_each_second()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("quit")
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.move(left=True)
            if event.key == pygame.K_RIGHT:
                game.move(right=True)
            if event.key == pygame.K_DOWN:
                game.move(down=True)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    squares = game.getSquares()

    for square in squares:
        rect = pygame.Rect(square.x, square.y, square.width, square.width)
        pygame.draw.rect(screen, "red", rect)

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
