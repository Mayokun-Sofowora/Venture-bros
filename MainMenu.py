import pygame as pg

from Const import *
from Text import Text
from Filesystem import Filesystem

class MainMenu(object):
    def __init__(self):
        self.mainImage = self.load_main_image()

        self.toStartText = Text('Press ENTER to start', 16, (WINDOW_W - WINDOW_W * 0.72, WINDOW_H - WINDOW_H * 0.3))
        self.leaderboardText = Text('Press L for Leaderboard', 12, (WINDOW_W - WINDOW_W * 0.72, WINDOW_H - WINDOW_H * 0.2))


    def load_main_image(self):
        directory = r'assets\images'
        pattern = r'super_mario_bros\.(png|jpg)'  # Define the regex pattern for the filename

        matching_files = Filesystem.find_files_by_pattern(directory, pattern)
        if matching_files:
            return Filesystem.load_image(str(matching_files[0]))

        # Return a default image or handle the case when no matching file is found
        return None

    def render(self, core):
        core.screen.blit(self.mainImage, (50, 50))
        self.toStartText.render(core)
        self.leaderboardText.render(core)

