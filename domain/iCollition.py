from abc import ABC, abstractmethod


class ICollition(ABC):
    @abstractmethod
    def collide(self, square_a, square_b):
        pass
