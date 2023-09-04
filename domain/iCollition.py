from abc import ABC, abstractmethod


class ICollition(ABC):
    @abstractmethod
    def collide(self, figure_a, figure_b):
        pass
