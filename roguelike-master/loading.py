import os
import pygame

ANIMATION_FOLDER = r"animations"
TILE_SIZE = 50


def load_lod():
    animation_dict = {}
    # load player animations
    for animations in os.listdir(ANIMATION_FOLDER):
        animation_dict[animations] = {}
        for animation_type in os.listdir(os.path.join(ANIMATION_FOLDER, animations)):
            if '_no_scale' in animation_type:
                no_scale = True
            else:
                no_scale = False
            animation_dict[animations][animation_type] = {}
            for img in os.listdir(os.path.join(ANIMATION_FOLDER, animations, animation_type)):
                print(os.path.join(ANIMATION_FOLDER, animations, animation_type, img))
                if not no_scale:
                    animation_dict[animations][animation_type][
                        int(img.split("-")[2].strip(".png"))] = pygame.transform.scale(
                        pygame.image.load(os.path.join(ANIMATION_FOLDER, animations, animation_type, img)),
                        (TILE_SIZE, TILE_SIZE))

                else:
                    animation_dict[animations][animation_type][
                        int(img.split("-")[2].strip(".png"))] = pygame.image.load(
                        os.path.join(ANIMATION_FOLDER, animations, animation_type, img))
    return animation_dict


def load():
    global TILE_SIZE
    textures = {}
    textures[TILE_SIZE] = load_lod()
    TILE_SIZE = TILE_SIZE // 2
    textures[TILE_SIZE] = load_lod()
    TILE_SIZE = TILE_SIZE // 2
    textures[TILE_SIZE] = load_lod()
    TILE_SIZE=50
    return textures

print(load())
