import os
import pygame
import math

ANIMATION_FOLDER = r"animations"
TILE_SIZE = 100


def load_lod(screen, rect, font):
    animation_dict = {}
    # load player animations
    for animations in os.listdir(ANIMATION_FOLDER):
        animation_dict[animations] = {}
        for animation_type in os.listdir(os.path.join(ANIMATION_FOLDER, animations)):
            img = font.render(f"loading: {animations}:{animation_type}", True, (255, 255, 255))
            screen.fill((0, 0, 0))
            img_rect = img.get_rect()
            img_rect.center = rect.center
            screen.blit(img, img_rect)
            pygame.display.flip()
            if '_no_scale' in animation_type:
                no_scale = True
            else:
                no_scale = False
            animation_dict[animations][animation_type] = {}
            for img in os.listdir(os.path.join(ANIMATION_FOLDER, animations, animation_type)):

                if not no_scale:
                    animation_dict[animations][animation_type][
                        int(img.split("-")[2].strip(".png"))] = {}
                    for loop in range(1, 20):
                        animation_dict[animations][animation_type][
                            int(img.split("-")[2].strip(".png"))][loop] = pygame.transform.scale(
                            pygame.image.load(os.path.join(ANIMATION_FOLDER, animations, animation_type, img)),
                            (math.ceil(TILE_SIZE / loop), math.ceil(TILE_SIZE / loop)))
                else:
                    animation_dict[animations][animation_type][
                        int(img.split("-")[2].strip(".png"))] = pygame.image.load(
                        os.path.join(ANIMATION_FOLDER, animations, animation_type, img))
    return animation_dict


def load():
    screen = pygame.display.get_surface()
    rect = screen.get_rect()
    font = pygame.font.SysFont('', 24)

    return load_lod(screen, rect, font)


print(load())
