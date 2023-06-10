from pathlib import Path # for filesystem
import pygame as pg
import re # for regex

class Filesystem:
    @staticmethod
    def load_image(filename):
        path = Path(filename)
        image_path = path.resolve()  # Resolve the absolute path

        # Load the image using pygame
        image = pg.image.load(str(image_path)).convert_alpha()

        return image
    @staticmethod
    def find_files_by_pattern(directory, pattern):
        path = Path(directory)
        absolute_path = path.resolve()

        # Use regex to match filenames
        regex_pattern = re.compile(pattern)
        matching_files = [file for file in absolute_path.glob('*') if regex_pattern.match(file.name)]

        return matching_files
