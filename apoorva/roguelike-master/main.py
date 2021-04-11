from multiprocessing import Process, Array, Manager

if __name__ == '__main__':
    import pygame

    # init
    pygame.init()
    font = pygame.font.SysFont('', 24)
    clock = pygame.time.Clock()
    GRAVITY = 0
    # Set up the drawing window
    fullscreen = False

    if fullscreen:
        base_display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | pygame.HWSURFACE)
        DISPLAY_SIZE = base_display.get_size()
    else:
        DISPLAY_SIZE = (1920 // 2, 1080 // 2)
        base_display = pygame.display.set_mode(DISPLAY_SIZE)
    # importing modules
    import bodies
    import map_generation
    import pygame_gui
    import random

    zoom = 1 * bodies.TILE_SIZE // 50
    bodies.GAME_SIZE = GAME_SIZE = (DISPLAY_SIZE[0] * zoom, DISPLAY_SIZE[1] * zoom)
    screen = pygame.Surface(GAME_SIZE)
    manager = pygame_gui.UIManager(DISPLAY_SIZE)
    on_map_elements_list = []
    physical_elements_list = []
    for loop in range(100):
        on_map_elements_list.append(bodies.Element(str(1), pos=(4200, 5200)))
    player = bodies.Player(5000, 5000, bodies.TILE_SIZE, bodies.TILE_SIZE, manager, on_map_elements_list)

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
    radius = 2
    max_physics_radius = 6
    lod = 1  # * 50 // bodies.TILE_SIZE
    pygame.display.flip()
    game_map.render_map(lod, radius, index)
    physics_objects = []
    background_img = pygame.transform.scale(pygame.image.load('ezgif-frame-001.jpg'), (100, 100))
    chest1 = bodies.Chest(4500, 4500, bodies.TILE_SIZE, bodies.TILE_SIZE, on_map_elements_list, physical_elements_list)


    def update_physics_lists():
        _physics_objects = game_map.get_chunks_border_objects(index, 6)
        _physics_objects.extend(physical_elements_list)
        _player_collision = game_map.get_chunks_border_objects(index, 4)
        _player_collision.extend(physical_elements_list)
        return _physics_objects, _player_collision


    inventory_shown = False
    player.inventory.hide()
    while running:
        GAME_SIZE = [int(GAME_SIZE[0]), int(GAME_SIZE[1])]
        old_physical_elements_list = physical_elements_list.copy()
        if index != (int(player.x // (bodies.TILE_SIZE * map_generation.CHUNK_SIZE)),
                     int(player.y // (bodies.TILE_SIZE * map_generation.CHUNK_SIZE))):
            index = (int(player.x // (bodies.TILE_SIZE * map_generation.CHUNK_SIZE)),
                     int(player.y // (bodies.TILE_SIZE * map_generation.CHUNK_SIZE)))
            game_map.render_map(lod, radius, index)
            physics_objects, player_collision = update_physics_lists()

        # time_delta = clock.tick(fps_target) / 1000.0
        player.dt = clock.tick(fps_target) / (1000 / 60)
        screen = pygame.Surface(GAME_SIZE)
        base_scroll[0] += (player.rect.centerx - base_scroll[0] - (
                lod * GAME_SIZE[0] / 2)) * player.dt / 20
        base_scroll[1] += (player.rect.centery - base_scroll[1] - (
                lod * GAME_SIZE[1] / 2)) * player.dt / 20
        draw_scroll = (int(base_scroll[0]), int(base_scroll[1]))
        old_lod = lod
        lod = int(zoom)
        if old_lod != lod:
            if lod == 0:
                lod = 1
            else:
                game_map.clear_surfaces()
                game_map.render_map(lod, radius, index, force=True)
                bodies.GAME_SIZE = GAME_SIZE = (DISPLAY_SIZE[0] * zoom * 1 / lod, DISPLAY_SIZE[1] * zoom * 1 / lod)

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    zoom += 0.1
                    player.zoom = zoom
                    bodies.GAME_SIZE = GAME_SIZE = (DISPLAY_SIZE[0] * zoom * 1 / lod, DISPLAY_SIZE[1] * zoom * 1 / lod)
                if event.key == pygame.K_8:
                    # bodies.textures = bodies.all_lod_textures[bodies.TILE_SIZE]
                    game_map.render_map(lod, radius, index, force=True)
                if event.key == pygame.K_2:
                    zoom -= 0.1
                    player.zoom = zoom
                    bodies.GAME_SIZE = GAME_SIZE = (DISPLAY_SIZE[0] * zoom * 1 / lod, DISPLAY_SIZE[1] * zoom * 1 / lod)

                if event.key == pygame.K_3:
                    fps_target -= 10
                if event.key == pygame.K_4:
                    fps_target += 10
                if event.key == pygame.K_5:
                    zoom = 1
                    player.zoom = zoom
                    lod = 1
                    radius = 7
                    game_map.clear_surfaces()
                    game_map.render_map(lod, radius, index, force=True)
                    bodies.GAME_SIZE = GAME_SIZE = (DISPLAY_SIZE[0] * zoom * 1 / lod, DISPLAY_SIZE[1] * zoom * 1 / lod)

                if event.key == pygame.K_6:
                    lod += 1
                    game_map.clear_surfaces()
                    game_map.render_map(lod, radius, index, force=True)
                    bodies.GAME_SIZE = GAME_SIZE = (DISPLAY_SIZE[0] * zoom * 1 / lod, DISPLAY_SIZE[1] * zoom * 1 / lod)

                if event.key == pygame.K_7:
                    radius += 1
                    game_map.render_map(lod, radius, index, force=True)
                if event.key == pygame.K_i:
                    if not inventory_shown:
                        inventory_shown = True
                        player.inventory.show()
                    else:
                        inventory_shown = False
                        player.inventory.hide()

            player.process_inputs(event)
        player.update(player_collision, physics_objects)

        # Fill the background with white
        screen.fill((0, 0, 0))

        # Draw
        game_map.draw_map_chunks(lod, screen, draw_scroll, radius, index)
        player.draw(screen, draw_scroll, lod)
        img = font.render(
            'stamina' + str(round(player.stamina, 2)) + 'fps:' + str(round(clock.get_fps(), 2)) + 'zoom' + str(
                zoom) + 'lod' + str(lod),
            True,
            (255, 255, 0))
        # screen.set_colorkey((0, 0, 0))
        manager.update(10)
        i = 0
        while i < len(on_map_elements_list):
            if not on_map_elements_list[i].update(player):
                on_map_elements_list[i].draw(screen, draw_scroll, lod)
                i += 1
        base_display.blit(pygame.transform.scale(screen, DISPLAY_SIZE), (0, 0))

        manager.draw_ui(base_display)
        base_display.blit(img, (400, 400))
        if physical_elements_list != old_physical_elements_list:
            physics_objects, player_collision = update_physics_lists()
        # Flip the display
        pygame.display.flip()

    # Done! Time to quit..
    pygame.quit()
