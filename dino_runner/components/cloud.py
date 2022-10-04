from pygame.sprite import Sprite

from dino_runner.utils.constants import CLOUD 

X_POS = 500
Y_POS = 100

class Cloud (Sprite):
    def __init__(self):
        self.image = CLOUD
        self.cloud_rect = self.image.get_rect()
        self.cloud_rect.x = X_POS
        self.cloud_rect.y = Y_POS
    
    def draw(self, screem):
        screem.blit(self.image, (self.cloud_rect.x, self.cloud_rect.y))


