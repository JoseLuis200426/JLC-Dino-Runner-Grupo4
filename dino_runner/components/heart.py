from pygame.sprite import Sprite

from dino_runner.utils.constants import HEART

X_POS = 1070
Y_POS = 0

class Heart (Sprite):
    def __init__(self):
        self.image = HEART
        self.cloud_rect = self.image.get_rect()
        self.cloud_rect.x = X_POS
        self.cloud_rect.y = Y_POS
    
    def draw(self, screem):
        screem.blit(self.image, (self.cloud_rect.x, self.cloud_rect.y))