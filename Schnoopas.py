import pygame as pg

from Entity import Entity
from Const import *
from Filesystem import Filesystem


class Schnoopas(Entity):
    def __init__(self, x_pos, y_pos, move_direction):
        super().__init__()
        # Add additional attributes specific to your character
        self.rect = pg.Rect(x_pos, y_pos, 32, 25)

        self.shell_activated = False

        if move_direction:
            self.x_vel = 1
        else:
            self.x_vel = -1

        self.current_image = 0
        self.image_tick = 0
        # Load and assign images
        self.images = [
            Filesystem.load_image('assets/images/schnoopa_shell_0.png'),
            Filesystem.load_image('assets/images/schnoopa_shell_1.png'),
            Filesystem.load_image('assets/images/schnoopa_shell.png')
            # TODO: combine sprite and separate to just shell and no shell
        ]
        self.images.append(pg.transform.flip(self.images[0], 180, 0))
        self.images.append(pg.transform.flip(self.images[1], 180, 0))
        self.images.append(pg.transform.flip(self.images[2], 0, 180))

    """
    States: 
    0 - Just walking around
    1 - no shell  
    2 - shell 
    -1 - Dead
    """

    def update(self, core):
        if self.state == 0:
            self.update_image()

            if not self.on_ground:
                self.y_vel += GRAVITY

            blocks = core.get_map().get_blocks_for_collision(self.rect.x // 32, (self.rect.y - 14) // 32)
            self.update_x_pos(blocks)
            self.update_y_pos(blocks)

            self.check_map_borders(core)

        elif self.state == 1:
            blocks = core.get_map().get_blocks_for_collision(self.rect.x // 32, self.rect.y // 32)
            self.update_x_pos(blocks)
            self.update_y_pos(blocks)

            self.check_map_borders(core)

        elif self.state == 2:
            if not self.on_ground:
                self.y_vel += GRAVITY

            blocks = core.get_map().get_blocks_for_collision(self.rect.x // 32, self.rect.y // 32)
            self.update_x_pos(blocks)
            self.update_y_pos(blocks)

            self.check_map_borders(core)
            self.check_collision_with_player(core)

        elif self.state == -1:
            self.rect.y += self.y_vel
            self.y_vel += GRAVITY

            self.check_map_borders(core)

    def update_image(self):
        self.image_tick += 1

        """if self.image_tick == 10:
            self.current_image = 1

        elif self.image_tick == 20:
            self.current_image = 2

        elif self.image_tick == 30:
            self.current_image = 1

        elif self.image_tick == 40:
            self.current_image = 0

        elif self.image_tick == 50:
            self.current_image = 1

        elif self.image_tick == 60:
            self.current_image = 2

        elif self.image_tick == 70:
            if self.move_direction:
                self.current_image = 3
            else:
                self.current_image = 0
            self.image_tick = 0 """

        if self.x_vel > 0:
            self.move_direction = True
        else:
            self.move_direction = False

        if self.image_tick == 35:
            if self.move_direction:
                self.current_image = 4
            else:
                self.current_image = 1
        elif self.image_tick == 70:
            if self.move_direction:
                self.current_image = 3
            else:
                self.current_image = 0
            self.image_tick = 0

    def check_collision_with_player(self, core):
        if self.collision:
            if self.rect.colliderect(core.get_map().get_player().rect):
                if self.state != -1:
                    if core.get_map().get_player().y_vel > 0:
                        self.change_state(core)
                        core.get_sound().play('kill_mob', 0, 0.5)
                        core.get_map().get_player().reset_jump()
                        core.get_map().get_player().jump_on_mob()
                    else:
                        if not core.get_map().get_player().unkillable:
                            core.get_map().get_player().set_powerlvl(0, core)

                if self.state == 2 and not core.get_map().get_player().jump_on_mob():
                    core.get_map().get_player().add_score(50)
                    core.get_map().spawn_score_text(self.rect.x + 16, self.rect.y, score=50)

    def change_state(self, core):
        self.state += 1
        self.current_image = 2  # TODO:  take out

        # 0 to 1 state
        if self.rect.h == 46:
            self.x_vel = 0
            self.rect.h = 25
            self.rect.y += 14
            core.get_map().get_player().add_score(500)
            core.get_map().spawn_score_text(self.rect.x + 16, self.rect.y, score=500)

        # 1 to 2
        elif self.state == 2:
            core.get_map().get_player().add_score(500)
            core.get_map().spawn_score_text(self.rect.x + 16, self.rect.y, score=500)

            if core.get_map().get_player().rect.x - self.rect.x <= 0:
                self.x_vel = 1
            else:
                self.x_vel = -1

        # TODO: maybe take out
        # 2 to 3
        elif self.state == 3:
            self.die(core, instantly=False, crushed=False)

    def die(self, core, instantly, crushed):
        if not instantly:
            core.get_map().get_player().add_score(core.get_map().score_for_killing_mob)
            core.get_map().spawn_score_text(self.rect.x + 16, self.rect.y)
            if crushed:
                self.crushed = True
                self.image_tick = 0
                self.current_image = 5
                self.state = -1
                core.get_sound().play('kill_mob', 0, 0.5)
                self.collision = False
            else:
                self.y_vel = -2
                self.current_image = 3
                core.get_sound().play('shot', 0, 0.5)
                self.state = -1
                self.collision = False
        else:
            core.get_map().get_mobs().remove(self)

    # TODO: maybe change render method
    # def render(self, core):
    #    core.screen.blit(self.images[self.current_image], core.get_map().get_camera().apply(self))

    def render(self, core):
        if self.state == 2 and self.shell_activated:
            # Render the shell image instead of the character image
            shell_image = self.images[2]  # TODO: make [1] if shell or no she;;
            core.screen.blit(shell_image, core.get_map().get_camera().apply(self))
        else:
            character_image = self.images[self.current_image]
            core.screen.blit(character_image, core.get_map().get_camera().apply(self))

    def activate_shell(self):
        if self.state == 2:
            self.shell_activated = True

    def deactivate_shell(self):
        if self.state == 2:
            self.shell_activated = False
