from typing import Tuple

import pygame
import math
from enum import Enum
from loading import load, TILE_SIZE
import random

GRAVITY = 0
JUMP_HEIGHT = 40
WALKING_ACCELERATION = 2
MAX_STAMINA = 120
STAMINA_GAIN = 0.2
STAMINA_DASH_DRAIN = 50
INPUT_HANDLING_DICT = {
    pygame.K_RIGHT: (0, 1),
    pygame.K_LEFT: (0, -1),
    pygame.K_UP: (1, 0),
    pygame.K_DOWN: (-1, 0),
}
WALL_BOUNCINESS = 1
BULLET_FIRE_RATE = 1  # delay in milliseconds between shots
GAME_SIZE = [1920, 1080]
MAX_BULLETS = 200


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


def find_collisions(_object, object_to_collide_with_list):
    collided_with = []
    for obj in object_to_collide_with_list:
        if obj.rect.colliderect(_object.rect):
            collided_with.append(obj)
    return collided_with


all_lod_textures = load()
textures = all_lod_textures[TILE_SIZE]


# TODO MAKE LODs

class PlayerStatus(Enum):
    IDLE = 0
    WALKING = 1
    DASH = 2


class PhysicalObject:
    def __init__(self, x, y, x_size, y_size, object_type):
        self.width = x_size
        self.height = y_size
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.x = x
        self.y = y
        self.acceleration = pygame.math.Vector2(0, GRAVITY)
        self.speed = pygame.math.Vector2(0, 0)
        self.player_movement = [0, 0]
        self.dt = 1
        self.object_type = object_type

    def update_speed(self):
        # print(isinstance(self.speed, pygame.Vector2))
        if self.speed.length() < 0.2:
            self.speed = pygame.math.Vector2(0, 0)
        self.speed = self.speed + self.acceleration

        # self.speed = (self.speed[0] + self.acceleration[0] * self.dt, self.speed[1] + self.acceleration[1] * self.dt)

    def apply_acceleration(self, movement):
        self.acceleration = movement
        # self.acceleration = (movement[0]* self.dt, (movement[1] + GRAVITY)* self.dt)

    def update_position(self, platforms):
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

    def __init__(self, x, y, x_size, y_size):
        super().__init__(x, y, x_size, y_size, ObjectType.PLAYER)
        self.stamina = MAX_STAMINA
        self.angle = 0
        # PLayer specific code
        self.direction = (0, 0)
        self.inputs_old = {
            'Left': False,
            'Right': False,
            'Up': False,
            'Down': False,
            'Shift': False,
        }
        self.inputs = [0, 0, 0, 0, 0]  # format (left,right,up,down,shift)
        self.textures = {
            PlayerStatus.IDLE: textures['player']['idle'],
            PlayerStatus.WALKING: textures['player']['walking'],
            PlayerStatus.DASH: textures['player']['dash']

        }

        self.status = None
        self.particle_system = ParticleSystem((self.x, self.y))
        self.animation_tick = 0
        self.bullets = []
        self.bullet_delay_timer = 0

        self.acceleration_dict = {
            (0, 0, 0, 0): (pygame.math.Vector2(0, 0), PlayerStatus.IDLE),
            (0, 1, 0, 0): (pygame.math.Vector2(0, WALKING_ACCELERATION).rotate(-90), PlayerStatus.WALKING),
            (1, 0, 0, 0): (pygame.math.Vector2(0, WALKING_ACCELERATION).rotate(90), PlayerStatus.WALKING),
            (0, 0, 1, 0): (pygame.math.Vector2(0, WALKING_ACCELERATION).rotate(180), PlayerStatus.WALKING),
            (0, 0, 0, 1): (pygame.math.Vector2(0, WALKING_ACCELERATION), PlayerStatus.WALKING),
            (0, 1, 1, 0): (pygame.math.Vector2(0, WALKING_ACCELERATION).rotate(225), PlayerStatus.WALKING),
            (1, 0, 1, 0): (pygame.math.Vector2(0, WALKING_ACCELERATION).rotate(135), PlayerStatus.WALKING),
            (1, 0, 0, 1): (pygame.math.Vector2(0, WALKING_ACCELERATION).rotate(45), PlayerStatus.WALKING),
            (0, 1, 0, 1): (pygame.math.Vector2(0, WALKING_ACCELERATION).rotate(-45), PlayerStatus.WALKING),

        }

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

    def draw(self, screen, scroll):
        try:
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
            self.particle_system.draw(screen, scroll)
            screen.blit(self.textures[self.status][int(self.animation_tick + 1)],
                        (self.rect.x - scroll[0], self.rect.y - scroll[1]))
            pygame.draw.rect(screen, (255, 255, 255),
                             (self.rect.x - scroll[0], self.rect.y - scroll[1], self.rect.width, self.rect.height),
                             width=1)

            radar_len = 1000
            x = self.rect.centerx - scroll[0] + math.cos(math.radians(self.angle)) * radar_len
            y = self.rect.centery - scroll[1] + math.sin(math.radians(self.angle)) * radar_len
            pygame.draw.line(screen, (255, 0, 255), (self.rect.centerx - scroll[0], self.rect.centery - scroll[1]),
                             (x, y), 10)
            for bullet in self.bullets:
                bullet.draw(screen, scroll)
        except KeyError as e:
            print(e)
            pygame.draw.rect(screen, (255, 0, 0), self.rect)
            # print(e)

    def handle_bullets(self, physics_objects):
        mouse_buttons = pygame.mouse.get_pressed(num_buttons=3)
        current_time = pygame.time.get_ticks()
        Bullet.dt = self.dt
        if mouse_buttons[0] and (current_time - self.bullet_delay_timer > BULLET_FIRE_RATE):
            # TODO: FIX NOT CENTRERED EMMITER
            self.bullets.append(Bullet(self.rect.x, self.rect.y + 20, TILE_SIZE, TILE_SIZE // 2, self.angle))
            self.bullet_delay_timer = current_time
        for bullet in self.bullets:
            bullet.update(physics_objects)
        if len(self.bullets) > MAX_BULLETS:
            del self.bullets[0]

    def update(self, physics_objects):
        self.particle_system.update(self.dt)
        self.handle_bullets(physics_objects)
        # update stamina

        if self.stamina < MAX_STAMINA:
            self.stamina += STAMINA_GAIN * self.dt

        # physics
        self.status = PlayerStatus.IDLE
        self.player_movement = pygame.math.Vector2(0, 0)
        # noinspection PyTypeChecker
        x_y_inputs: Tuple[bool, bool, bool, bool] = tuple(self.inputs[:4])
        try:
            self.player_movement, self.status = self.acceleration_dict[x_y_inputs]
        except KeyError as e:
            print(e)

        self.direction = (
            self.player_movement[0] / WALKING_ACCELERATION, self.player_movement[1] / WALKING_ACCELERATION)

        # dash
        if self.inputs[4] and self.stamina > 25:
            self.player_movement = pygame.math.Vector2(self.player_movement[0] * JUMP_HEIGHT / WALKING_ACCELERATION,
                                                       self.player_movement[1] * JUMP_HEIGHT / WALKING_ACCELERATION)
            self.stamina -= STAMINA_DASH_DRAIN
            self.animation_tick = 0
        if self.speed.length() > 10:
            self.status = PlayerStatus.DASH
        if self.player_movement != [0, 0]:
            if self.status == PlayerStatus.DASH:
                self.particle_system.add_particles(4, self.rect.centerx, self.rect.centery, 4)
            self.particle_system.add_particles(1, self.rect.centerx, self.rect.centery)
        self.apply_acceleration(self.player_movement)
        self.update_speed()
        player_collisions = self.update_position(physics_objects)

        if player_collisions['left'] or player_collisions['right']:
            self.speed = pygame.math.Vector2(-self.speed[0], self.speed[1] * WALL_BOUNCINESS)
        if player_collisions['top'] or player_collisions['bottom']:
            self.speed = pygame.math.Vector2(self.speed[0], -self.speed[1] * WALL_BOUNCINESS)
        # reset shift toggle
        self.inputs[4] = False
        # add resistance to the ground
        self.speed = self.speed * (1 / 1.2)


class StaticObject:
    def __init__(self, x, y, x_size, y_size, object_type=ObjectType.GROUND):
        self.width = x_size
        self.height = y_size
        self.type = object_type
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.x = x
        self.y = y
        if self.type != ObjectType.EMPTY:
            self.texture = textures["enviroment_textures"][str(self.type.value)][1]

    def __repr__(self):
        return str(self.type.value)

    def draw(self, screen, scroll):
        if 0 <= int(self.x - scroll[0]) <= GAME_SIZE[0] and 0 <= int(self.y - scroll[1]) <= GAME_SIZE[1]:
            screen.blit(self.texture, (self.rect.x - scroll[0], self.rect.y - scroll[1]))


class Bullet(PhysicalObject):
    dt = 1

    def __init__(self, x, y, x_size, y_size, angle):
        super().__init__(x, y, x_size, y_size, ObjectType.BULLET)
        self.rect.center = (x, y)
        self.texture = textures['bullet']
        self.angle = angle
        self.acceleration = pygame.math.Vector2(0.5, 0)
        self.acceleration = self.acceleration.rotate_rad(math.radians(self.angle))
        self.max_bullet_speed = 20
        self.dt = Bullet.dt
        self.particle_system = ParticleSystem(self.rect.center, color=(255, 0, 128))

    def update_speed(self):
        if not (abs(self.speed[0]) > self.max_bullet_speed):
            self.speed = self.speed + self.acceleration

    def draw(self, screen, scroll):
        if 0 < self.x - scroll[0] < GAME_SIZE[0] and 0 < self.y - scroll[1] < GAME_SIZE[1]:
            surface = pygame.transform.scale(textures['bullet']['in_flight_no_scale'][1],
                                             (TILE_SIZE // 4, TILE_SIZE // 2))
            self.particle_system.draw(screen, scroll)

            x, y = self.rect.center
            blit_rotate(screen, surface, (x, y), 90 - self.angle,
                        (x - scroll[0], y - scroll[1]))

    def update(self, platforms):
        self.update_speed()
        collisions = self.update_position(platforms)
        if collisions['left'] or collisions['right']:
            self.speed = pygame.math.Vector2(self.speed[0] * -1, self.speed[1])
            self.acceleration[0] *= -1
            self.angle = 45 - self.angle
        if collisions['top'] or collisions['bottom']:
            self.speed = pygame.math.Vector2(self.speed[0], self.speed[1] * -1)
            self.acceleration[1] *= -1
            self.angle = 45 + self.angle
        self.particle_system.add_particles(2, self.rect.centerx, self.rect.centery)
        self.particle_system.update(self.dt)


class Particle:
    def __init__(self, parent_obj, pos, color, randomness=2, rad=5):
        self.parent_obj = parent_obj
        self.x, self.y = pos[0], pos[1]
        self.vx, self.vy = random.randint(-randomness, randomness), random.randint(-randomness * 10,
                                                                                   randomness * 10) * .1
        self.color = color
        self.rad = rad
        self.randomness = randomness

    def draw(self, win, scroll):
        pygame.draw.circle(win, self.color, (self.x - scroll[0], self.y - scroll[1]), self.rad / (100 / TILE_SIZE))

    def update(self, dt):
        self.x += self.vx * dt / (100 / TILE_SIZE)
        self.y += self.vy * dt / (100 / TILE_SIZE)
        if random.randint(0, self.randomness * 50) < 40:
            self.rad -= 1
        if self.rad < 0:
            self.parent_obj.particles.remove(self)
            del self


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

    def draw(self, win, scroll):
        for i in self.particles:
            if 0 < i.x - scroll[0] < GAME_SIZE[0] and 0 < i.y - scroll[1] < GAME_SIZE[1]:
                i.draw(win, scroll)
