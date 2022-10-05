from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import LARGE_CACTUS
from dino_runner.components.obstacles.cloud import Nube
from dino_runner.utils.constants import CLOUD

class ObstacleManager():
    def __init__(self):
        self.obstacles = []
        self.obstacles_1 = []

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

        for obstacle1 in self.obstacles_1:
            obstacle1.draw(screen)



    def update(self):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(LARGE_CACTUS[1]))

        if len(self.obstacles_1) == 0:
            self.obstacles_1.append(Nube(CLOUD))

        for obstacle in self.obstacles:
            obstacle.update()
            if obstacle.image_rect.x < -obstacle.image_rect.width:
                self.obstacles.pop()

        for obstacle1 in self.obstacles_1:
            obstacle1.update()
            if obstacle1.image_rect.x < -obstacle1.image_rect.width:
                self.obstacles_1.pop()

    