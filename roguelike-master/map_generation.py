import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pygame
# from multiprocessing import Manager
from bodies import StaticObject, TILE_SIZE, ObjectType, all_lod_textures

CHUNK_SIZE = 10
MAP_SIZE = 1000
PERLIN_FACTOR = 20


class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Coord):
            return self.x == other.x and self.y == other.y

    def __add__(self, other):
        if isinstance(other, Coord):
            return Coord(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"<{self.x},{self.y}>"


class Map:
    def __init__(self, ground='0', size=5, pos=Coord(1, 1), hero="@", ):
        # self.manager = Manager()
        self._mat = {}
        self.hero = hero
        self.hero_pos = pos
        self.size = size
        self.ground = ground
        self.dir = {
            'w': Coord(0, -1),
            's': Coord(0, 1),
            'd': Coord(1, 0),
            'a': Coord(-1, 0),
        }
        self.blit_list = None
        self.surface = None
        self.surface_dict = {}
        self._elem = {}

        # self._mat[pos.y][pos.x] = self.hero
        # self._elem['@'] = self.hero_pos

    def load_chunks(self, map_path):
        load_map = np.load(map_path)
        self._mat['size'] = (load_map.size, load_map[0].size)
        x = y = 0
        for index, chunk in enumerate(load_map.tolist()):
            self._mat[(x, y)] = {
                'objects': [],
                'ground': [],
                "border": [],
                'not_empty': [],
                'empty': []
            }

            map_length = MAP_SIZE // CHUNK_SIZE
            for y_index, y_arr in enumerate(chunk):

                self._mat[(x, y)]['objects'].append([[] for _ in range(len(chunk))])
                for x_index, env_object in enumerate(y_arr):
                    if env_object == 10:
                        self._mat[(x, y)]['objects'][y_index][x_index] = StaticObject(
                            TILE_SIZE * CHUNK_SIZE * x + x_index * TILE_SIZE,
                            TILE_SIZE * CHUNK_SIZE * y + y_index * TILE_SIZE,
                            TILE_SIZE,
                            TILE_SIZE,
                            object_type=ObjectType.GROUND)
                        self._mat[(x, y)]['ground'].append(self._mat[(x, y)]['objects'][y_index][x_index])
                        self._mat[(x, y)]['not_empty'].append(self._mat[(x, y)]['objects'][y_index][x_index])
                    elif env_object == 0:
                        self._mat[(x, y)]['objects'][y_index][x_index] = StaticObject(
                            TILE_SIZE * CHUNK_SIZE * x + x_index * TILE_SIZE,
                            TILE_SIZE * CHUNK_SIZE * y + y_index * TILE_SIZE,
                            TILE_SIZE,
                            TILE_SIZE,
                            object_type=ObjectType.BORDER)
                        self._mat[(x, y)]['border'].append(self._mat[(x, y)]['objects'][y_index][x_index])
                        self._mat[(x, y)]['not_empty'].append(self._mat[(x, y)]['objects'][y_index][x_index])
                    else:
                        self._mat[(x, y)]['objects'][y_index][x_index] = StaticObject(
                            TILE_SIZE * CHUNK_SIZE * x + x_index * TILE_SIZE,
                            TILE_SIZE * CHUNK_SIZE * y + y_index * TILE_SIZE,
                            TILE_SIZE,
                            TILE_SIZE,
                            object_type=ObjectType.EMPTY)
                        self._mat[(x, y)]['empty'].append(self._mat[(x, y)]['objects'][y_index][x_index])
            x += 1
            if x == map_length:
                x = 0
                y += 1

    def __repr__(self):
        index = 0, 0
        string = ''
        for y in self._mat[index]['objects']:
            for x in y:
                if isinstance(x, StaticObject):
                    string += str(x)
            string += '\n'
        return string

    def __len__(self):
        return self.size

    def __contains__(self, item):
        if isinstance(item, Coord):
            if 0 <= item.x < self.size and 0 <= item.y < self.size:
                return True
            else:
                return False
        else:
            for y in self._mat:
                for x in y:
                    if x == item:
                        return True
            return False

    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, key, value):
        self.put(value, key)

    def get(self, coord):
        if isinstance(coord, Coord):
            try:
                return self._mat[coord.y][coord.x]
            except IndexError as e:
                print(e)

    def pos(self, element):
        for y, y_ele in enumerate(self._mat):
            for x, x_ele in enumerate(y_ele):
                if x_ele == element:
                    return Coord(x, y)

    def put(self, coord, element):
        if isinstance(coord, Coord):
            try:
                if self._mat[coord.y][coord.x] == self.ground:
                    self._mat[coord.y][coord.x] = element
                    self._elem[element] = coord
                else:
                    raise IndexError(f"{self._mat[coord.y][coord.x]} is at that position cannot put {element} there")
            except IndexError as e:
                print(e)

    def rm(self, coord):
        if isinstance(coord, Coord):
            try:
                if self._mat[coord.y][coord.x] != self.ground:
                    del self._elem[self._mat[coord.y][coord.x]]
                    self._mat[coord.y][coord.x] = self.ground
                else:
                    raise IndexError(f"{self._mat[coord.y][coord.x]} there is nothing here at {coord}")
            except IndexError as e:
                print(e)

    def move(self, element, direction):
        position = self.pos(element)
        new_pos = position + direction
        if new_pos in self:
            if self._mat[new_pos.y][new_pos.x] == self.ground:
                self.rm(position)
                self.put(new_pos, element)

    def update_drawing(self, _index):
        chunk_size = (CHUNK_SIZE * TILE_SIZE, CHUNK_SIZE * TILE_SIZE)
        # all_lod_textures[TILE_SIZE]["enviroment_textures"][str(item.type.value)][1]
        self.blit_list = [
            (item.texture,
             (item.rect.x - TILE_SIZE * CHUNK_SIZE * _index[0], item.rect.y - TILE_SIZE * CHUNK_SIZE * _index[1])) for
            item
            in self._mat[_index]['not_empty']]
        self.surface_dict[_index] = pygame.Surface(chunk_size)
        self.surface_dict[_index].blits(self.blit_list)
        # self.surface = self.surface_dict[_index]
        # self.surface.blits(self.blit_list)

    def draw(self, screen, scroll, index=(0, 0)):
        screen.blit(self.surface_dict[index],
                    (-scroll[0] + TILE_SIZE * CHUNK_SIZE * index[0], -scroll[1] + TILE_SIZE * CHUNK_SIZE * index[1]))

    @staticmethod
    def get_position(index, radius):
        output = []
        for loop in range(index[1] - radius // 2, index[1] + radius // 2):
            for loop2 in range(index[0] - radius // 2, index[0] + radius // 2):
                if loop2 > 0 and loop > 0:
                    output.append((loop2, loop))
        return output

    # TODO FIX THIS NOT WORKING
    def render_map(self, radius, index,force=False):
        self.update_drawing(_index=index)
        indexes = self.get_position(index, radius)
        for index_ in indexes:
            if not force:
                try:
                    self.surface_dict[index_]
                except KeyError:
                    self.update_drawing(index_)

            else:
                self.update_drawing(index_)


    def draw_map_chunks(self, screen, draw_scroll, radius, index):
        self.draw(screen, draw_scroll, index)

        indexes = self.get_position(index, radius)
        for index_ in indexes:
            try:
                self.draw(screen, draw_scroll, index_)
            except KeyError as e:
                pass
                # print(e)


def generate_perlin_noise_2d(shape, res):
    """https://pvigier.github.io/2018/06/13/perlin-noise-numpy.html"""

    def f(_t):
        return 6 * _t ** 5 - 15 * _t ** 4 + 10 * _t ** 3

    delta = (res[0] / shape[0], res[1] / shape[1])
    d = (shape[0] // res[0], shape[1] // res[1])
    grid = np.mgrid[0:res[0]:delta[0], 0:res[1]:delta[1]].transpose(1, 2, 0) % 1
    # Gradients
    angles = 2 * np.pi * np.random.rand(res[0] + 1, res[1] + 1)
    gradients = np.dstack((np.cos(angles), np.sin(angles)))
    g00 = gradients[0:-1, 0:-1].repeat(d[0], 0).repeat(d[1], 1)
    g10 = gradients[1:, 0:-1].repeat(d[0], 0).repeat(d[1], 1)
    g01 = gradients[0:-1, 1:].repeat(d[0], 0).repeat(d[1], 1)
    g11 = gradients[1:, 1:].repeat(d[0], 0).repeat(d[1], 1)
    # Ramps
    n00 = np.sum(grid * g00, 2)
    n10 = np.sum(np.dstack((grid[:, :, 0] - 1, grid[:, :, 1])) * g10, 2)
    n01 = np.sum(np.dstack((grid[:, :, 0], grid[:, :, 1] - 1)) * g01, 2)
    n11 = np.sum(np.dstack((grid[:, :, 0] - 1, grid[:, :, 1] - 1)) * g11, 2)
    # Interpolation
    t = f(grid)
    n0 = n00 * (1 - t[:, :, 0]) + t[:, :, 0] * n10
    n1 = n01 * (1 - t[:, :, 0]) + t[:, :, 0] * n11
    return np.sqrt(2) * ((1 - t[:, :, 1]) * n0 + t[:, :, 1] * n1)


def is_thing(a, threshold):
    if -0.2 < a < threshold:
        return True


def block_shaped(arr, chunk_size_y, chunk_size_x):
    """
    https://stackoverflow.com/questions/16856788/slice-2d-array-into-smaller-2d-arrays
    Return an array of shape (n, chunk_size_y, chunk_size_x) where
    n * chunk_size_y * chunk_size_x = arr.size

    If arr is a 2D array, the returned array should look like n subblocks with
    each subblock preserving the "physical" layout of arr.
    """
    h, w = arr.shape
    assert h % chunk_size_y == 0, "{} rows is not evenly divisble by {}".format(h, chunk_size_y)
    assert w % chunk_size_x == 0, "{} cols is not evenly divisble by {}".format(w, chunk_size_x)
    return (arr.reshape(h // chunk_size_y, chunk_size_y, -1, chunk_size_x)
            .swapaxes(1, 2)
            .reshape(-1, chunk_size_y, chunk_size_x))


def generate_map_file():
    if __name__ == '__main__':
        max_threshold = -0.15
        min_threshold = -0.25

        x = generate_perlin_noise_2d((MAP_SIZE, MAP_SIZE), (MAP_SIZE // PERLIN_FACTOR, MAP_SIZE // PERLIN_FACTOR))

        x[np.logical_and(min_threshold < x, x < max_threshold)] = 0
        x[x < min_threshold] = 10
        print()
        list_arr = block_shaped(x, CHUNK_SIZE, CHUNK_SIZE)
        np.save('mapchunck', list_arr)
        for loop in list_arr:
            plt.imshow(loop, interpolation='nearest')
            plt.show()
        plt.imshow(x, interpolation='nearest')
        plt.show()
        np.savetxt('map2', x)

        # convert your array into a dataframe
        df = pd.DataFrame(x)

        # save to xlsx file

        filepath = 'my_excel_file.xlsx'

        df.to_excel(filepath, index=False)
        print()


game_map = Map()
game_map.load_chunks('mapchunck.npy')
print(game_map._mat['size'])
print(game_map)
# print(game_map)
generate_map_file()
# print(np.load('mapchunck.npy'))
