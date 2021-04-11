from typing import Tuple

import pygame
import math
from enum import Enum
from loading import load, TILE_SIZE
import random
import inventory

# import loading

DASH_ACCELERATION = 40
WALKING_ACCELERATION = 2
MAX_STAMINA = 120
STAMINA_GAIN = 0.2
STAMINA_DASH_DRAIN = 50
START_HP = 100
INPUT_HANDLING_DICT = {
    pygame.K_RIGHT: (0, 1),
    pygame.K_LEFT: (0, -1),
    pygame.K_UP: (1, 0),
    pygame.K_DOWN: (-1, 0),
}
WALL_BOUNCINESS = 1
BULLET_FIRE_RATE = 1  # delay in milliseconds between shots
GAME_SIZE = [1920, 1080]
MAX_BULLETS = 50
MAX_HP = 100
pygame.font.init()
font = pygame.font.SysFont('', 24)


def blit_rotate(surf, image, topleft, angle, center):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=topleft).center)
    new_rect.center = center
    surf.blit(rotated_image, new_rect.topleft)
    # pygame.draw.rect(surf, (255, 0, 0), new_rect, 2)
    # pygame.draw.circle(surf, (255, 255, 0), new_rect.center, 20)
    return new_rect


class ObjectType(Enum):
    EMPTY = 'empty'
    GROUND = 'ground'
    BORDER = 'border'
    PLAYER = 22
    ENEMY = 33
    BULLET = 44
    CHEST = 'chest'


def find_collisions(_object, object_to_collide_with_list):
    collided_with = []
    for obj in object_to_collide_with_list:
        if obj.rect.colliderect(_object.rect):
            collided_with.append(obj)
    return collided_with


all_lod_textures = load()
textures = all_lod_textures


class Particle:
    def __init__(self, parent_obj, pos, color, randomness=2, rad=5):
        self.parent_obj = parent_obj
        self.x, self.y = pos[0], pos[1]
        self.vx, self.vy = random.randint(-randomness, randomness), random.randint(-randomness * 10,
                                                                                   randomness * 10) * .1
        self.color = color
        self.rad = rad
        self.randomness = randomness

    def draw(self, win, scroll, lod):
        pygame.draw.circle(win, self.color, ((self.x - scroll[0]) / lod, (self.y - scroll[1]) / lod),
                           self.rad / (100 * lod / TILE_SIZE))

    def update(self, dt, var2=None):
        self.x += self.vx * dt / (100 / TILE_SIZE)
        self.y += self.vy * dt / (100 / TILE_SIZE)
        if random.randint(0, self.randomness * 50) < 40:
            self.rad -= 1
        if self.rad < 0 and self.parent_obj:
            self.parent_obj.particles.remove(self)
            del self


class Element(Particle):
    dt = 1

    def __init__(self, name, parent_obj=None, pos=(0, 0), color=(255, 255, 255), abbreviation=None, image=None):
        super().__init__(parent_obj, pos, color, randomness=100)
        self.name = name
        if image:
            self.image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
        else:
            self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
            self.image.fill((0, 0, 0))
            self.image.blit(font.render(self.name, True, color), (TILE_SIZE // 2, TILE_SIZE // 2))

        self.rect = pygame.Rect((0, 0), (TILE_SIZE, TILE_SIZE))
        if abbreviation:
            self.abbreviation = abbreviation
        else:
            self.abbreviation = name[0]

    def __repr__(self):
        return self.abbreviation

    def description(self):
        return f"<{self.name}>"

    def update(self, player, var2=None):
        vector_between_player_and_object = pygame.math.Vector2(player.x - self.x, player.y - self.y)
        if vector_between_player_and_object.magnitude() < 400:
            self.vx, self.vy = vector_between_player_and_object[0] / 100, vector_between_player_and_object[1] / 100

        self.vx, self.vy = self.vx / 1.2, self.vy / 1.2
        self.x += self.vx * self.dt / (100 / TILE_SIZE)
        self.y += self.vy * self.dt / (100 / TILE_SIZE)
        self.rect.x, self.rect.y = self.x, self.y

        if self.rect.colliderect(player.rect):
            player.inventory.add_element(self)
            return True
        else:
            return False

    def draw(self, win, scroll, lod):
        win.blit(pygame.transform.scale(self.image, (TILE_SIZE // lod, TILE_SIZE // lod)),
                 ((self.x - scroll[0]) / lod, (self.y - scroll[1]) / lod))


class ParticleSystem:
    def __init__(self, pos, color=(255, 255, 255)):
        self.pos = pos
        self.particles = []
        self.color = color

    def add_particles(self, amount, x, y, randomness=2):
        for i in range(amount):
            self.particles.append(Particle(self, (x, y), self.color, randomness=randomness))

    def update(self, dt):
        [i.update(dt) for i in self.particles]

    def draw(self, win, scroll, lod):
        [i.draw(win, scroll, lod) for i in self.particles]


class StaticObject:
    def __init__(self, x, y, x_size, y_size, object_type=ObjectType.GROUND):
        self.width = x_size
        self.height = y_size
        self.type = object_type
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.x = x
        self.y = y
        if self.type == ObjectType.CHEST:
            self.texture = None
        else:
            if self.type != ObjectType.EMPTY:
                self.texture = textures["enviroment_textures"][str(self.type.value)][1]
            else:
                self.texture = textures["enviroment_textures"]['background'][1]

    def __repr__(self):
        return str(self.type.value)

    def draw(self, screen, scroll, lod):
        if 0 <= int(self.x - scroll[0]) <= GAME_SIZE[0] and 0 <= int(self.y - scroll[1]) <= GAME_SIZE[1]:
            screen.blit(self.texture, (self.rect.x - scroll[0], self.rect.y - scroll[1]))


class PlayerStatus(Enum):
    IDLE = 0
    WALKING = 1
    DASH = 2


class Gun:
    def __init__(self, fire_rate, max_bullets, parent_obj):
        self.fire_rate = fire_rate
        self.max_bullets = max_bullets
        self.bullets = []
        self.parent_obj = parent_obj
        self.dt = 1
        self.bullet_delay_timer = 0
        self.bullet_lifetime = 500

    def update(self, physics_objects):
        mouse_buttons = pygame.mouse.get_pressed(num_buttons=3)
        current_time = pygame.time.get_ticks()
        Bullet.dt = self.dt
        if mouse_buttons[0] and (current_time - self.bullet_delay_timer > self.fire_rate):
            # TODO: FIX NOT CENTRERED EMMITER
            self.bullets.append(Bullet(self.parent_obj.rect.x, self.parent_obj.rect.y + 20, TILE_SIZE, TILE_SIZE // 2,
                                       self.parent_obj.angle, self, self.bullet_lifetime))
            self.bullet_delay_timer = current_time
        # update bullets
        [bullet.update(physics_objects) for bullet in self.bullets]

        if len(self.bullets) > self.max_bullets:
            del self.bullets[0]

    def draw(self, screen, scroll, lod):
        for bullet in self.bullets:
            bullet.draw(screen, scroll, lod)


class Chest(StaticObject):
    def __init__(self, x, y, x_size, y_size, on_map_elements_list, physical_elements_list):
        super().__init__(x, y, x_size, y_size, object_type=ObjectType.CHEST)
        self.inventory = []
        for loop in range(100):
            self.inventory.append(Element(str(loop), pos=(self.x, self.y)))
        self.hp = 10
        self.on_map_elements_list = on_map_elements_list
        self.texture = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.physical_elements_list = physical_elements_list
        self.on_map_elements_list.append(self)
        self.physical_elements_list.append(self)

    def open(self):
        print('opned')
        if self in self.physical_elements_list:
            self.physical_elements_list.remove(self)
        if self in self.on_map_elements_list:
            self.on_map_elements_list.remove(self)
            self.on_map_elements_list.extend(self.inventory)
        del self

    def update(self, player):
        pass

    def draw(self, screen, scroll, lod):
        screen.blit(pygame.transform.scale(self.texture, (TILE_SIZE // lod, TILE_SIZE // lod)),
                    ((self.x - scroll[0]) / lod, (self.y - scroll[1]) / lod))


class PhysicalObject(Element):
    def __init__(self, x, y, x_size, y_size, object_type, name):
        """
        Objects that is tied with physics
        :param x: position x
        :param y: position y
        :param x_size: x_size
        :param y_size: y_size
        :param object_type: object type can be found in ObjectType Enum
        """
        super().__init__(name)
        self.width = x_size
        self.height = y_size
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.x = x
        self.y = y
        self.acceleration = pygame.math.Vector2(0, 0)
        self.speed = pygame.math.Vector2(0, 0)
        self.player_movement = [0, 0]
        self.dt = 1
        self.object_type = object_type

    def update_speed(self):
        """
        Updates the speed of the object each frame
        """
        if self.speed.length() < 0.2:
            self.speed = pygame.math.Vector2(0, 0)
        self.speed = self.speed + self.acceleration

    def apply_acceleration(self, movement):
        """
        changes the acceleration of the object
        :param movement: target acceleration
        """
        self.acceleration = movement

    def update_position(self, platforms):
        """
        Updates the position of the player accounting the collisions
        :param platforms: Physical object to account collisions with
        :return collision_data: A dict with the collisions with all the objects
        """
        movement = self.speed
        collision_data = {'top': False,
                          'bottom': False,
                          'right': False,
                          'left': False,
                          'slant_bottom': False,
                          'data': {}}
        # checking on x axis
        self.x += movement[0] * self.dt / (100 / TILE_SIZE)
        self.rect.x = int(self.x)
        block_hit_list = find_collisions(self, platforms)
        for _object in block_hit_list:
            markers = {'left': False,
                       'right': False,
                       'top': False,
                       'bottom': False}
            if movement[0] > 0:
                self.rect.right = _object.rect.left
                collision_data['right'] = True
                markers['left'] = True
            elif movement[0] < 0:
                self.rect.left = _object.rect.right
                collision_data['left'] = True
                markers['right'] = True
            collision_data['data'][_object] = markers
            self.x = self.rect.x

        # checking on y axis
        self.y += movement[1] * self.dt / (100 / TILE_SIZE)
        self.rect.y = int(self.y)
        block_hit_list = find_collisions(self, platforms)

        for _object in block_hit_list:
            try:
                collision_data['data'][_object]['top'] = False
            except KeyError:
                collision_data['data'][_object] = {'left': False,
                                                   'right': False,
                                                   'top': False,
                                                   'bottom': False}

            if movement[1] > 0:
                self.rect.bottom = _object.rect.top
                collision_data['bottom'] = True
                collision_data['data'][_object]['top'] = True
            elif movement[1] < 0:
                self.rect.top = _object.rect.bottom
                collision_data['top'] = True
                collision_data['data'][_object]['bottom'] = True
            # collision_data['data'].append([_object, markers])
            self.y = self.rect.y

        return collision_data


class Player(PhysicalObject):
    zoom = 2

    def __init__(self, x, y, x_size, y_size, manager, on_map_elements_list, start_hp=START_HP,
                 dash_acceleration=DASH_ACCELERATION,
                 walking_acceleration=WALKING_ACCELERATION, max_stamina=MAX_STAMINA, stamina_gain=STAMINA_GAIN,
                 stamina_dash_drain=STAMINA_DASH_DRAIN, max_hp=MAX_HP):
        """
        Player object
        :param x: x position of the player
        :param y: y position of the player
        :param x_size: x_size of the player
        :param y_size: y size of the player
        """
        super().__init__(x, y, x_size, y_size, ObjectType.PLAYER, 'Player')  # init the Physical object
        # Player stats
        self.max_stamina = max_stamina
        self.stamina = 0
        self.current_hp = start_hp
        self.health_capacity = max_hp
        self.dash_acceleration = dash_acceleration
        self.walking_acceleration = walking_acceleration
        self.stamina_gain = stamina_gain
        self.stamina_dash_drain = stamina_dash_drain
        self.inventory = inventory.Inventory(manager, [5, 5], 100, on_map_elements_list)

        self.angle = 0  # current player angle
        self.direction = (0, 0)  # player direction
        self.inputs = [0, 0, 0, 0, 0]  # player inputs format (left,right,up,down,shift)

        # player textures
        self.textures = {
            PlayerStatus.IDLE: textures['player']['idle'],
            PlayerStatus.WALKING: textures['player']['walking'],
            PlayerStatus.DASH: textures['player']['dash']
        }

        # player status used for animation
        self.status = None
        # player particle system
        self.particle_system = ParticleSystem((self.x, self.y))
        # player animation tick to chose the frames
        self.animation_tick = 0

        # player acceleration dict converts player inputs into pygame vectors #TODO make controller support
        self.acceleration_dict = {
            (0, 0, 0, 0): (pygame.math.Vector2(0, 0), PlayerStatus.IDLE),
            (0, 1, 0, 0): (pygame.math.Vector2(0, self.walking_acceleration).rotate(-90), PlayerStatus.WALKING),
            (1, 0, 0, 0): (pygame.math.Vector2(0, self.walking_acceleration).rotate(90), PlayerStatus.WALKING),
            (0, 0, 1, 0): (pygame.math.Vector2(0, self.walking_acceleration).rotate(180), PlayerStatus.WALKING),
            (0, 0, 0, 1): (pygame.math.Vector2(0, self.walking_acceleration), PlayerStatus.WALKING),
            (0, 1, 1, 0): (pygame.math.Vector2(0, self.walking_acceleration).rotate(225), PlayerStatus.WALKING),
            (1, 0, 1, 0): (pygame.math.Vector2(0, self.walking_acceleration).rotate(135), PlayerStatus.WALKING),
            (1, 0, 0, 1): (pygame.math.Vector2(0, self.walking_acceleration).rotate(45), PlayerStatus.WALKING),
            (0, 1, 0, 1): (pygame.math.Vector2(0, self.walking_acceleration).rotate(-45), PlayerStatus.WALKING),

        }
        self.gun = Gun(BULLET_FIRE_RATE, MAX_BULLETS, self)

    def process_inputs(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.inputs[1] = True
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.inputs[0] = True
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                self.inputs[2] = True
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.inputs[3] = True
            if event.key == pygame.K_SPACE:
                self.inputs[4] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.inputs[1] = False
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.inputs[0] = False
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                self.inputs[2] = False
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.inputs[3] = False

    def draw(self, screen, scroll, lod):
        # getting angle
        x1, y1 = pygame.mouse.get_pos()
        x1, y1 = x1 * self.zoom + scroll[0], y1 * self.zoom + scroll[1]
        x2, y2 = self.rect.center
        self.angle = 180 + math.degrees(math.atan2((y2 - y1), (x2 - x1)))
        self.animation_tick += 1 * self.dt
        # counting frames for animation
        if self.animation_tick >= 23 and self.status == PlayerStatus.IDLE:
            self.animation_tick = 0
        if self.animation_tick >= 4 and self.status == PlayerStatus.WALKING:
            self.animation_tick = 0
        if self.animation_tick >= 23 and self.status == PlayerStatus.DASH:
            self.animation_tick = 0

        # drawing
        self.particle_system.draw(screen, scroll, lod)
        screen.blit(self.textures[self.status][int(self.animation_tick + 1)][lod],
                    ((self.rect.x - scroll[0]) * 1 / lod,
                     (self.rect.y - scroll[1]) * 1 / lod))
        pygame.draw.rect(screen, (255, 255, 255),
                         ((self.rect.x - scroll[0]) / lod, (self.rect.y - scroll[1]) / lod, self.rect.width / lod,
                          self.rect.height / lod),
                         width=int(5 / lod))

        radar_len = 1000
        x = self.rect.centerx - scroll[0] + math.cos(math.radians(self.angle)) * radar_len
        y = self.rect.centery - scroll[1] + math.sin(math.radians(self.angle)) * radar_len
        pygame.draw.aaline(screen, (255, 0, 255),
                           ((self.rect.centerx - scroll[0]) / lod, (self.rect.centery - scroll[1]) / lod),
                           (x / lod, y / lod), 10 // lod, )
        self.gun.draw(screen, scroll, lod)

    def update(self, physics_objects, gun_physical_objects=None):
        # update player particle system
        self.particle_system.update(self.dt)

        # update Gun
        self.gun.update(gun_physical_objects)

        # update stamina
        if self.stamina < self.max_stamina:
            self.stamina += self.stamina_gain * self.dt

        # physics
        self.status = PlayerStatus.IDLE
        self.player_movement = pygame.math.Vector2(0, 0)

        # inputs
        # noinspection PyTypeChecker
        x_y_inputs: Tuple[bool, bool, bool, bool] = tuple(self.inputs[:4])
        try:
            self.player_movement, self.status = self.acceleration_dict[x_y_inputs]
        except KeyError as e:
            print(e)

        self.direction = (
            self.player_movement[0] / self.walking_acceleration, self.player_movement[1] / self.walking_acceleration)

        # dash
        if self.inputs[4] and self.stamina > 25:
            self.player_movement = pygame.math.Vector2(
                self.player_movement[0] * self.dash_acceleration / self.walking_acceleration,
                self.player_movement[1] * self.dash_acceleration / self.walking_acceleration)
            self.stamina -= self.stamina_dash_drain
            self.animation_tick = 0
        if self.speed.length() > 10:
            self.status = PlayerStatus.DASH
        if self.player_movement != [0, 0]:
            if self.status == PlayerStatus.DASH:
                self.particle_system.add_particles(4, self.rect.centerx, self.rect.centery, 4)
            self.particle_system.add_particles(1, self.rect.centerx, self.rect.centery)

        # updating acceleration and speed
        self.apply_acceleration(self.player_movement)
        self.update_speed()
        player_collisions = self.update_position(physics_objects)
        # bouncing with everything
        if player_collisions['left'] or player_collisions['right']:
            self.speed = pygame.math.Vector2(-self.speed[0], self.speed[1] * WALL_BOUNCINESS)
        if player_collisions['top'] or player_collisions['bottom']:
            self.speed = pygame.math.Vector2(self.speed[0], -self.speed[1] * WALL_BOUNCINESS)
        # reset shift toggle
        self.inputs[4] = False

        # add resistance to the ground
        self.speed = self.speed * (1 / 1.2)


class Bullet(PhysicalObject):
    dt = 1

    def __init__(self, x, y, x_size, y_size, angle, parent_obj, lifetime):
        super().__init__(x, y, x_size, y_size, ObjectType.BULLET, 'bullet')
        self.rect.center = (x, y)
        self.texture = textures['bullet']
        self.angle = angle
        self.acceleration = pygame.math.Vector2(0.5, 0)
        self.acceleration = self.acceleration.rotate_rad(math.radians(self.angle))
        self.max_bullet_speed = 20
        self.dt = Bullet.dt
        self.lifetime = 0
        self.max_lifetime = lifetime
        self.particle_system = ParticleSystem(self.rect.center, color=(255, 0, 128))
        self.parent_obj = parent_obj

    def update_speed(self):
        if not (abs(self.speed[0]) > self.max_bullet_speed):
            self.speed = self.speed + self.acceleration

    def draw(self, screen, scroll, lod):
        surface = pygame.transform.scale(textures['bullet']['in_flight_no_scale'][1],
                                         (TILE_SIZE // (4 * lod), TILE_SIZE // (2 * lod)))

        # self.particle_system.draw(screen, scroll,lod)

        x, y = self.rect.center
        blit_rotate(screen, surface, (x // lod, y // lod), 90 - self.angle,
                    ((x - scroll[0]) // lod, (y - scroll[1]) // lod))

    def update(self, platforms, var2=None):
        self.lifetime += self.dt
        if self.lifetime > self.max_lifetime:
            self.parent_obj.bullets.remove(self)
            del self
            return 0
        self.update_speed()
        self.angle = pygame.math.Vector2(1, 0).angle_to(self.speed)
        collisions = self.update_position(platforms)
        if collisions['left'] or collisions['right']:
            self.speed = pygame.math.Vector2(self.speed[0] * -1, self.speed[1])
            self.acceleration[0] *= -1
        if collisions['top'] or collisions['bottom']:
            self.speed = pygame.math.Vector2(self.speed[0], self.speed[1] * -1)
            self.acceleration[1] *= -1

        for key, value in collisions['data'].items():
            if key.type == ObjectType.CHEST:
                key.open()

        # self.particle_system.add_particles(2, self.rect.centerx, self.rect.centery)
        # self.particle_system.update(self.dt)
