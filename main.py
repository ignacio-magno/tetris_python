import threading

import pygame

from domain import game as gm

# pygame setup
pygame.init()
screen = pygame.display.set_mode((500, 750))
clock = pygame.time.Clock()
running = True

game = gm.Game(500, 750, 50)


def repeat_each_second():
    game.move(down=True)
    threading.Timer(1.0, repeat_each_second).start()


repeat_each_second()

while running:
    screen.fill("black")

    # draw limit line
    pygame.draw.line(screen, "white", (0, 0), (0, 750), 5)
    pygame.draw.line(screen, "white", (500, 0), (500, 750), 5)
    pygame.draw.line(screen, "white", (0, 750), (500, 750), 5)

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

    figures = game.getSquares()

    for fig in figures:
        for sqr in fig.squares:
            print(sqr.x, sqr.y, sqr.side)
            # TODO: Fix this. (sqr.y -sqr.side) is not the correct way to draw the square
            rect = pygame.Rect(sqr.x, sqr.y - sqr.side, sqr.side, sqr.side)
            pygame.draw.rect(screen, "red", rect)

    # RENDER YOUR GAME HERE
    if game.gameOver():

        font = pygame.font.Font(None, 75)
        game_over_text = font.render("Game Over", True, (255, 0, 0))  #

        screen.blit(game_over_text, (100, 300))
    else:
        pass

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
