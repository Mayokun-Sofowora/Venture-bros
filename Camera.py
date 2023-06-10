import pygame as pg

from Const import *


class Camera(object):
    """

    Camera class.

    """
    def __init__(self, width, height):
        self.rect = pg.Rect(0, 0, width, height)
        self.main_camera(self.rect)

    def main_camera(self, target_rect):
        """
        This method calculates the position and size of the camera based on a target rectangle.
        It centers the camera on the target and ensures that it doesn't go beyond the game window's boundaries
        """
        x, y = target_rect.x, target_rect.y
        width, height = self.rect.width, self.rect.height
        x, y = (-x + WINDOW_W / 2 - target_rect.width / 2), (-y + WINDOW_H / 2 - target_rect.height)

        x = min(0, x)
        x = max(-(self.rect.width - WINDOW_W), x)
        y = WINDOW_H - self.rect.h

        return pg.Rect(x, y, width, height)

    def apply(self, target):
        return target.rect.x + self.rect.x, target.rect.y

    def update(self, target):
        self.rect = self.main_camera(target)

    def reset(self):
        self.rect = pg.Rect(0, 0, self.rect.w, self.rect.h)
