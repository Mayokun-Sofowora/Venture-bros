from os import environ
import pygame as pg
import re
from pygame.locals import *

from Const import *
from Map import Map
from MenuManager import MenuManager
from Sound import Sound


class Core(object):
    """

    Main class.

    """

    def __init__(self):
        environ['SDL_VIDEO_CENTERED'] = '1'
        pg.mixer.pre_init(44100, -16, 2, 1024)
        pg.init()
        self.screen = pg.display.set_mode((WINDOW_W, WINDOW_H))

        self.clock = pg.time.Clock()
        self.pause_time = False
        self.paused_ticks = 0
        self.player_name_active = True

        self.oWorld = Map('1-1')
        self.oSound = Sound()
        self.oMM = MenuManager(self)

        self.run = True
        self.keyR = False
        self.keyL = False
        self.keyU = False
        self.keyD = False
        self.keyShift = False
        self.score = str(self.get_map().get_player().score)

    def main_loop(self):
        while self.run:
            self.input()
            if not self.pause_time:
                self.update()
                self.render()
            self.clock.tick(FPS)

    def input(self):
        if self.get_mm().currentGameState == 'Game':
            self.input_player()
        elif self.get_mm().currentGameState == 'Leaderboard':
            self.input_leaderboard()
        else:
            self.input_menu()

    def input_leaderboard(self):
        for e in pg.event.get():
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_BACKSPACE:
                    self.oMM.oLeaderboardMenu.player_name = self.oMM.oLeaderboardMenu.player_name[:-1]
                elif e.key == pg.K_RETURN:
                    if self.oMM.oLeaderboardMenu.player_name.strip() != "":
                        # Only add the name if it is not empty
                        self.get_mm().oLeaderboardMenu.add_score(self.score, self.oMM.oLeaderboardMenu.player_name)
                        self.oMM.oLeaderboardMenu.player_name = ""
                        print(self.oMM.oLeaderboardMenu.player_name)
                        if re.match(self.oMM.oLeaderboardMenu.regex_pattern, self.oMM.oLeaderboardMenu.player_name):
                            print("Valid name:", self.oMM.oLeaderboardMenu.player_name)
                            self.get_mm().oLeaderboardMenu.add_score(self.score, self.oMM.oLeaderboardMenu.player_name)
                            self.oMM.oLeaderboardMenu.player_name = ""
                            self.get_mm().oLeaderboardMenu.save_scores('assets/scores/scores.txt')
                        else:
                            print("Invalid name:", str(self.oMM.oLeaderboardMenu.player_name))
                            # Reset the player name and deactivate input box
                            self.oMM.oLeaderboardMenu.player_name = ""
                            self.oMM.oLeaderboardMenu.player_name_active = False
                    else:
                        self.oMM.currentGameState = 'MainMenu'  # Go back to the main menu
                else:
                    # Append the pressed key to the player name if it's a valid character
                    if e.unicode.isalnum():
                        self.oMM.oLeaderboardMenu.player_name += e.unicode
            elif e.type == pg.KEYUP:
                if e.key == pg.K_ESCAPE:
                    self.oMM.oLeaderboardMenu.player_name = ""
                    self.oMM.currentGameState = 'MainMenu'  # Go back to the main menu

    def input_player(self):
        for e in pg.event.get():

            if e.type == pg.QUIT:
                self.run = False

            elif e.type == KEYDOWN:
                if e.key == K_RIGHT or e.key == K_d:
                    self.keyR = True
                elif e.key == K_LEFT or e.key == K_a:
                    self.keyL = True
                elif e.key == K_DOWN or e.key == K_s:
                    self.keyD = True
                elif e.key == K_UP or e.key == K_w:
                    self.keyU = True
                elif e.key == K_LSHIFT or e.key == K_RSHIFT:
                    self.keyShift = True

            elif e.type == KEYUP:
                if e.key == K_RIGHT or e.key == K_d:
                    self.keyR = False
                elif e.key == K_LEFT or e.key == K_a:
                    self.keyL = False
                elif e.key == K_DOWN or e.key == K_s:
                    self.keyD = False
                elif e.key == K_UP or e.key == K_w:
                    self.keyU = False
                elif e.key == K_LSHIFT or e.key == K_RSHIFT:
                    self.keyShift = False

    def input_menu(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.run = False
            elif e.type == KEYDOWN:
                if e.key == K_l:
                    self.get_mm().show_leaderboard()
                elif e.key == K_RETURN:
                    self.get_mm().start_loading()

    def update(self):
        if self.pause_time:
            self.paused_ticks += 1  # Keep track of paused ticks
        else:
            self.get_mm().update(self)

    def pause_game_time(self):
        self.pause_time = True
        self.paused_ticks = 0

    def resume_game_time(self):
        self.pause_time = False
        self.paused_ticks = 0

    def render(self):
        self.get_mm().render(self)
        self.ups = str(int(self.clock.get_fps()))
        caption = 'Venture Bros | FPS: ' + self.ups
        pg.display.set_caption(caption)

    def get_map(self):
        return self.oWorld

    def get_mm(self):
        return self.oMM

    def get_sound(self):
        return self.oSound

    def get_score_from_game(self):
        return self.oWorld.get_player().score
