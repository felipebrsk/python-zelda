import pygame

from debug import debug
from settings import *
from tile import Tile
from player import Player


class Level:
    def __init__(self):
        self.player = None
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = pygame.sprite.Group()
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
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
