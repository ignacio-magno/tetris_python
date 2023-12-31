import threading

import pygame

from domain import game as gm

# pygame setup
pygame.init()
screen = pygame.display.set_mode((700, 750))
clock = pygame.time.Clock()
running = True

game = gm.Game(500, 750, 50)

sound = pygame.mixer.Sound("sound.mp3")


sound.play(loops=-1)


def repeat_each_second():
    game.move(down=True)
    threading.Timer(1.0, repeat_each_second).start()


def draw_figure(fig):
    for sqr in fig:
        # TODO: Fix this. (sqr.y -sqr.side) is not the correct way to draw the square
        rect = pygame.Rect(sqr.x, sqr.y - sqr.side, sqr.side, sqr.side)

        color = sqr.color
        pygame.draw.rect(screen, color, rect)

        darkColor = pygame.Color("dark" + color)

        pygame.draw.rect(screen, darkColor, rect.inflate(-4, -4))


repeat_each_second()

while running:
    screen.fill("black")

    # draw limit line
    pygame.draw.line(screen, "white", (0, 0), (0, 750), 5)
    pygame.draw.line(screen, "white", (500, 0), (500, 750), 5)
    pygame.draw.line(screen, "white", (0, 750), (500, 750), 5)

    # draw score
    font = pygame.font.Font(None, 40)
    score_text = font.render("Score: " + str(game.score), True, (255, 0, 0))
    screen.blit(score_text, (530, 50))

    next_figure_text = font.render("Next Figure", True, (255, 0, 0))
    screen.blit(next_figure_text, (530, 150))
    # draw next figure
    next_figure = game.next_figure
    draw_figure(next_figure.generate_new_clone(530, 350).squares)

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

            if event.key == pygame.K_SPACE:
                game.move(torque=True)

            # pause
            if event.key == pygame.K_p:
                sound.stop()
                pygame.mixer.music.pause()

    # fill the screen with a color to wipe away anything from last frame
    draw_figure(game.getSquares())

    # RENDER YOUR GAME HERE
    if game.gameOver():

        font = pygame.font.Font(None, 75)
        game_over_text = font.render("Game Over", True, (255, 0, 0))  #

        screen.blit(game_over_text, (100, 300))
    else:
        game.check_lines()
        pass

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
