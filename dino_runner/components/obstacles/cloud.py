from dino_runner.components.obstacles.obstacle import Obstacle
from random import randint



class Nube(Obstacle):
    def __init__ (self, image):
        super().__init__(image)
        self.image_rect.y = randint (50, 150)

    def update(self):
        self.image_rect.x -= 5
        

