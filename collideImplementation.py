from domain import iCollition
import pygame


class CollideImplementation(iCollition.ICollition):
    def collide(self, square_a, square_b):
        rect1 = pygame.Rect(square_a.x, square_a.y, square_a.width, square_a.width)
        rect2 = pygame.Rect(square_b.x, square_b.y, square_b.width, square_b.width)

        return rect1.colliderect(rect2)
