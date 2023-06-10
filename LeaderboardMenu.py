import pygame as pg
import os
import re

from Text import Text
from Const import *
from Filesystem import Filesystem


class Leaderboard(pg.sprite.Sprite):
    def __init__(self, core):
        super().__init__()
        self.scores = []
        self.font = pg.font.Font(None, 16)
        self.input_box = pg.Rect(485, 400, 200, 32)
        self.background_image = Filesystem.load_image(r'assets\images\leaderboard_bg.png')
        self.title_text = Text('LEADERBOARD', 16, (WINDOW_W * 0.7, WINDOW_H / 6), 'Emulogic', (0, 0, 0))

        self.color_inactive = pg.Color('lightskyblue3')
        self.color_active = pg.Color('dodgerblue2')
        self.color = self.color_inactive
        self.done = False
        self.score = 0
        self.player_name = ''
        self.player_name_surface = self.font.render(self.player_name, True, (23, 23, 0))
        self.player_name_active = False
        self.regex_pattern = r'^[a-zA-Z0-9]+$'
        self.max_name_length = 10  # Maximum length of the player name

    def load_scores(self, file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    score, player_name = line.strip().split(':')  # Split score and player name
                    self.scores.append((player_name, int(score)))  # Store as a tuple

    def save_scores(self, file_path):
        with open(file_path, 'w') as file:
            for score in self.scores:
                player_name, score_value = score
                file.write(f"{player_name}:{score_value}\n")

    def add_score(self, player_name, score):
        self.scores.append((player_name, score))
        self.scores.sort(key=lambda x: x[1], reverse=True)  # Sort scores in descending order
        self.save_scores('assets/scores/scores.txt')

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if self.input_box.collidepoint(event.pos):
                    self.player_name_active = not self.player_name_active
                else:
                    self.player_name_active = False
                color = self.color_active if self.player_name_active else self.color_inactive
            elif event.type == pg.KEYDOWN and self.player_name_active:
                if event.key == pg.K_RETURN:
                    print(self.player_name)
                    # Validate and process the player name
                    if pg.key.get_mods() & pg.KMOD_SHIFT:
                        # Shift key is pressed, add score directly from the game
                        score = self.get_score_from_game()  # Replace with your own code to get the score
                        self.add_score(score)
                    else:
                        if re.match(self.regex_pattern, self.player_name):
                            print("Valid name:", self.player_name)
                            self.add_score(123)  # Replace 123 with the actual high score
                            self.add_score(self.player_name)
                            self.save_scores('assets/scores/scores.txt')
                        else:
                            print("Invalid name:", self.player_name)
                            # Reset the player name and deactivate input box
                    self.player_name = ''
                    self.player_name_active = False
                elif event.key == pg.K_BACKSPACE:
                    # Remove the last character from the player name
                    self.player_name = self.player_name[:-1]
                else:
                    # Append the pressed key to the player name
                    if event.unicode.isalnum() and len(self.player_name) < self.max_name_length:
                        if re.match(self.regex_pattern, self.player_name):
                            self.player_name += event.unicode

                self.player_name_surface = self.font.render(self.player_name, True, (23, 23, 0))
        for event in pg.event.get():
            if event.type == pg.KEYUP and event.key == pg.K_ESCAPE:
                pass
                # self.core.resume_game_time()
                #self.get_mm().currentGameState = 'MainMenu'

    def update(self):
        self.handle_events()
        width = max(200, self.player_name_surface.get_width() + 10)
        self.input_box.w = width

    def render(self, core):
        core.screen.blit(self.background_image, (0, 0))
        self.title_text.render(core)
        y_offset = 100  # Vertical offset for rendering player names
        for i, score in enumerate(self.scores):
            player_name = score[1]
            player_name_text = Text(player_name, 10, (WINDOW_W // 2, y_offset + i * 20), 'Emulogic', (120, 20, 103))
            player_name_text.render(core)

        pg.draw.rect(core.screen, (255, 255, 255), self.input_box)
        pg.draw.rect(core.screen, (0, 0, 0), self.input_box, 2)

        player_name_surface = self.font.render(self.player_name, True, (23, 23, 0))
        player_name_rect = player_name_surface.get_rect(topleft=(self.input_box.x + 5, self.input_box.y + 5))
        if player_name_rect.width > self.input_box.width - 10:
            overflow = player_name_rect.width - (self.input_box.width - 10)
            player_name_text = self.player_name[-(len(self.player_name) - int(overflow / 8)):]
            player_name_surface = self.font.render(player_name_text, True, (23, 23, 0))

        core.screen.blit(player_name_surface, player_name_rect.topleft)

    def update_time(self):
        self.iTime = pg.time.get_ticks()
        delay_complete = False

    def get_score_from_game(self):
        return self.oWorld.get_player().score

