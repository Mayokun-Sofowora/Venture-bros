import pygame as pg
from Filesystem import Filesystem 


class Tube(pg.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.image = Filesystem.load_image('assets/images/tube.png')
        length = (12 - y_pos) * 32
        self.image = self.image.subsurface(0, 0, 64, length)
        self.rect = pg.Rect(x_pos * 32, y_pos * 32, 64, length)

    def render(self, core):
        core.screen.blit(self.image, core.get_map().get_camera().apply(self))
