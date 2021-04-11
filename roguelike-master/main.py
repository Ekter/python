from multiprocessing import Process, Array, Manager

if __name__ == '__main__':
    import pygame
    import bodies
    import map_generation

    # init
    pygame.init()
    clock = pygame.time.Clock()
    GRAVITY = 0
    # Set up the drawing window
    fullscreen = True
    zoom = 1
    if fullscreen:
        base_display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # | pygame.HWSURFACE | pygame.DOUBLEBUF)
        DISPLAY_SIZE = base_display.get_size()
    else:
        DISPLAY_SIZE = (1920 // 2, 1080 // 2)
        base_display = pygame.display.set_mode(DISPLAY_SIZE)
    bodies.GAME_SIZE = GAME_SIZE = (DISPLAY_SIZE[0] * zoom, DISPLAY_SIZE[1] * zoom)
    screen = pygame.Surface(GAME_SIZE)

    player = bodies.Player(5000, 5000, bodies.TILE_SIZE, bodies.TILE_SIZE)
    font = pygame.font.SysFont(None, 24)
    player.jump = False
    pygame.key.set_repeat(0)
    pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
    # Run until the user asks to quit
    running = True
    moving_left = moving_right = False
    dt = 1

    # loading map
    game_map = map_generation.Map()
    game_map.load_chunks('mapchunck.npy')

    base_scroll = [0, 0]
    player.zoom = zoom
    fps_target = 60
    index = 0, 0
    radius = 6
    game_map.render_map(radius, index)
    physics_objects = []
    background_img = pygame.image.load('background_img.jfif')
    while running:
        if index != (int(player.x // (bodies.TILE_SIZE * map_generation.CHUNK_SIZE)),
                     int(player.y // (bodies.TILE_SIZE * map_generation.CHUNK_SIZE))):
            index = (int(player.x // (bodies.TILE_SIZE * map_generation.CHUNK_SIZE)),
                     int(player.y // (bodies.TILE_SIZE * map_generation.CHUNK_SIZE)))
            game_map.render_map(radius, index)
            physics_objects = []
            for loop in game_map.get_position(index, radius):
                physics_objects.extend(game_map._mat[loop]['border'])
        player.dt = clock.tick(fps_target) / (1000 / 60)
        screen = pygame.Surface(GAME_SIZE)

        base_scroll[0] += (player.rect.centerx - base_scroll[0] - (GAME_SIZE[0] / 2)) * player.dt / 20
        base_scroll[1] += (player.rect.centery - base_scroll[1] - (GAME_SIZE[1] / 2)) * player.dt / 20
        draw_scroll = (int(base_scroll[0]), int(base_scroll[1]))
        # print(clock.get_fps())

        # player.dt = 1
        # print(player.dt, clock.get_fps(), fps_target)

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    zoom += 0.1
                    player.zoom = zoom
                    bodies.GAME_SIZE = GAME_SIZE = (DISPLAY_SIZE[0] * zoom, DISPLAY_SIZE[1] * zoom)
                if event.key == pygame.K_8:
                    # bodies.TILE_SIZE = bodies.TILE_SIZE // 2
                    # map_generation.TILE_SIZE = bodies.TILE_SIZE
                    bodies.textures = bodies.all_lod_textures[bodies.TILE_SIZE]
                    game_map.update_drawing(_index=index)
                    game_map.update_drawing((index[0] + 1, index[1]))
                    game_map.update_drawing((index[0], index[1] + 1))
                    game_map.update_drawing((index[0] + 1, index[1] + 1))
                if event.key == pygame.K_2:
                    zoom -= 0.1
                    player.zoom = zoom
                    bodies.GAME_SIZE = GAME_SIZE = (DISPLAY_SIZE[0] * zoom, DISPLAY_SIZE[1] * zoom)
                if event.key == pygame.K_3:
                    fps_target -= 10
                if event.key == pygame.K_4:
                    fps_target += 10
                if event.key == pygame.K_5:
                    zoom = 1
                    player.zoom = zoom
                    bodies.GAME_SIZE = GAME_SIZE = (DISPLAY_SIZE[0] * zoom, DISPLAY_SIZE[1] * zoom)

            player.process_inputs(event)

            # else:
            #     player.acceleration = (0, GRAVITY)
            #     pass
        # print(player.acceleration)
        # update physics
        # print(moving_left,moving_right)
        # player.dt = dt
        player.update(physics_objects)
        # print(player.status)
        # print('colliding with floor')

        # Fill the background with white
        screen.fill((0, 0, 0))

        # Draw
        # game_map.draw(screen, draw_scroll, _index)
        # game_map.draw(screen, draw_scroll, (_index[0] + 1, _index[1]))
        # game_map.draw(screen, draw_scroll, (_index[0], _index[1] + 1))
        # game_map.draw(screen, draw_scroll, (_index[0] + 1, _index[1] + 1))
        game_map.draw_map_chunks(screen, draw_scroll, radius, index)
        player.draw(screen, draw_scroll)
        img = font.render(
            'stamina' + str(round(player.stamina, 2)) + 'fps:' + str(round(clock.get_fps(), 2)) + 'zoom' + str(zoom),
            True,
            (255, 255, 0))
        screen.set_colorkey((0, 0, 0))
        base_display.blit(pygame.transform.scale(background_img, DISPLAY_SIZE), (0, 0))
        base_display.blit(pygame.transform.scale(screen, DISPLAY_SIZE), (0, 0))
        base_display.blit(img, (400, 400))

        # Flip the display
        pygame.display.flip()

    # Done! Time to quit..
    pygame.quit()
