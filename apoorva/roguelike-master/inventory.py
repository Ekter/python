import pygame
import pygame_gui


class Player1:
    def __init__(self):
        self.health_capacity = 100
        self.current_health = 20


image = pygame.image.load('download.png')
image.set_colorkey((255, 255, 255))


class Cell:
    def __init__(self, relative_rect: pygame.Rect, text: str, _manager, _container, _element):
        self.manager = _manager
        self.element = _element
        self.count = 0
        self.elements = []
        self.container = pygame_gui.core.UIContainer(manager=_manager, relative_rect=relative_rect,
                                                     container=_container)
        self.elements.append(self.container)
        rect = pygame.Rect((0, 0), (relative_rect.height, relative_rect.width))
        self.button = pygame_gui.elements.UIButton(rect, text, _manager, self.container)
        self.button.parent_elem = self
        self.elements.append(self.button)
        rect2 = pygame.Rect((0, 0), (relative_rect.height - 10, relative_rect.width - 10))
        rect2.center = rect.center
        text_rect = pygame.Rect((25, 25), (40, 40))
        text_rect.bottomright = (self.container.rect.width, self.container.rect.height)

        self.image = pygame_gui.elements.UIImage(relative_rect=rect2, image_surface=image, manager=_manager,
                                                 container=self.container, anchors={'left': 'left',
                                                                                    'right': 'right',
                                                                                    'top': 'top',
                                                                                    'bottom': 'bottom'})
        self.text = pygame_gui.elements.UILabel(text_rect,
                                                f"<font face=’verdana’ color=’#000000’ size=3.5>{self.count}</font>",
                                                manager=self.manager, container=self.container)
        self.item_image = None
        if self.element is not None:
            self.item_image = pygame_gui.elements.UIImage(relative_rect=rect2, image_surface=self.element.image,
                                                          manager=_manager,
                                                          container=self.container, anchors={'left': 'left',
                                                                                             'right': 'right',
                                                                                             'top': 'top',
                                                                                             'bottom': 'bottom'})
            self.elements.append(self.item_image)
        self.elements.append(self.image)
        self.elements.append(self.text)
        self.center_rect = rect2
        self.update()

    def add_image(self):
        self.item_image = pygame_gui.elements.UIImage(relative_rect=self.center_rect, image_surface=self.element.image,
                                                      manager=self.manager,
                                                      container=self.container, anchors={'left': 'left',
                                                                                         'right': 'right',
                                                                                         'top': 'top',
                                                                                         'bottom': 'bottom'})

        self.elements.append(self.item_image)
        self.text.kill()
        text_rect = pygame.Rect((25, 25), (40, 40))
        text_rect.bottomright = (self.container.rect.width, self.container.rect.height)

        self.text = pygame_gui.elements.UILabel(text_rect,
                                                f"<font face=’verdana’ color=’#000000’ size=3.5>{self.count}</font>",
                                                manager=self.manager, container=self.container)

        self.elements.append(self.text)

    def hide(self):
        for _element in self.elements:
            _element.visible = 0

    def show(self):
        for _element in self.elements:
            _element.visible = 1

    def update(self):
        self.text.set_text(str(self.count))
        # text_rect = pygame.Rect((25, 25), (40, 40))
        # text_rect.bottomright = (self.container.rect.width, self.container.rect.height)
        #
        # self.text = pygame_gui.elements.UILabel(text_rect,f"<font face=’verdana’ color=’#000000’ size=3.5>{self.count}</font>",_manager=self._manager,container=self.container)

    def use(self):
        if self.count != 0:
            self.count -= 1
            self.update()
        if self.count == 0:
            if self.item_image:
                self.item_image.kill()
            self.element = None


class Inventory:
    def __init__(self, _manager, size, cell_size, on_map_elements_list):
        self.rect = pygame.Rect((0, 0), (size[0] * cell_size, size[1] * cell_size))

        # self.rect.midbottom = _manager.window_resolution[0] / 2, _manager.window_resolution[1]
        self.rect.center = _manager.window_resolution[0] / 2, _manager.window_resolution[1] / 2
        self.container = pygame_gui.core.UIContainer(manager=_manager, relative_rect=self.rect)

        self.cells = []
        self.elements = [self.cells]
        self.on_map_elements_list = on_map_elements_list
        for y in range(size[0]):
            for x in range(size[1]):
                self.cells.append(
                    Cell(relative_rect=pygame.Rect((y * cell_size, x * cell_size), (cell_size, cell_size)),
                         text=f"{x}{y}",
                         _manager=_manager, _container=self.container, _element=None))

    def add_element(self, _element):
        self.on_map_elements_list.remove(_element)
        for item in self.cells:
            if item.element is not None:
                if item.element.name == _element.name:
                    item.count += 1
                    item.update()
                    return True
        for item in self.cells:
            if item.element is None:
                item.element = _element
                item.add_image()
                item.count += 1
                item.update()
                return False

    def hide(self):
        for item_list in self.elements:
            for item in item_list:
                item.hide()

    def show(self):
        for item_list in self.elements:
            for item in item_list:
                item.show()


if __name__ == '__main__':
    from bodies import Element, Player, PlayerStatus

    pygame.init()
    player = Player1()
    pygame.display.set_caption('Quick Start')
    DISPLAY_SIZE = (800, 600)
    window_surface = pygame.display.set_mode(DISPLAY_SIZE)

    background = pygame.Surface((800, 600))
    background.fill(pygame.Color('#000000'))

    manager = pygame_gui.UIManager(DISPLAY_SIZE)
    manager.set_visual_debug_mode(True)
    element_list = []
    inventory = Inventory(manager, [5, 1], 100, element_list)

    h = pygame_gui.elements.UIScreenSpaceHealthBar(relative_rect=pygame.Rect((0, 275), (100, 50)), manager=manager,
                                                   sprite_to_monitor=player)
    slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((0, 0), (100, 50)), start_value=0,
                                                    value_range=(0, 100), manager=manager)
    label = pygame_gui.elements.UILabel(pygame.Rect((100, 100), (200, 0)), text="ochinchin", manager=manager)
    clock = pygame.time.Clock()
    is_running = True
    element1 = Element('shwoe', image=pygame.image.load('download.png'), pos=(100, 100))
    element2 = Element('shwoe', image=pygame.image.load('ezgif-frame-001.jpg'), pos=(100, 100))
    element_list.append(element1)
    element_list.append(element2)
    player = Player(0, 0, 100, 100, 0, 10, 2, 100, 100, 10)
    player.inventory = inventory

    while is_running:
        window_surface.fill((255, 255, 255))
        time_delta = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            player.process_inputs(event)
            if event.type == pygame.QUIT:
                is_running = False

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if isinstance(event.ui_element, pygame_gui.elements.UIButton):
                        event.ui_element.parent_elem.use()
                    # if event.ui_element == hello_button:
                    #     print('Hello World!')
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    print('presed')
                    inventory.hide()
                if event.key == pygame.K_s:
                    inventory.show()
                if event.key == pygame.K_d:
                    inventory.add_element(element1)
                if event.key == pygame.K_f:
                    inventory.add_element(element2)

            manager.process_events(event)
        player.current_health = slider.get_current_value()
        for element in element_list:
            element.draw(window_surface, (0, 0), 1)
            element.update(player)
        if player.current_health == player.health_capacity:
            player.current_health = 0
        manager.update(time_delta)

        manager.draw_ui(window_surface)
        player.update([])
        player.draw(window_surface, (0, 0), 1)
        pygame.display.update()
