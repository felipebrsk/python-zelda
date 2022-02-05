import pygame

from debug import debug
from settings import *
from tile import Tile
from player import Player


class Level:
    def __init__(self):
        self.player = None
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        self.create_map()

    def create_map(self):
        for i, r in enumerate(WORLD_MAP):
            for c_i, c in enumerate(r):
                x = c_i * TILESIZE
                y = i * TILESIZE
                if c == 'x':
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites])
                if c == 'p':
                    self.player = Player(
                        (x, y),
                        [self.visible_sprites],
                        self.obstacle_sprites)

    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        for sprite in self.sprites():
            offset_position = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_position)
