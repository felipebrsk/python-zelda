import pygame

from settings import *
from random import randint


class MagicPlayer(pygame.sprite.Sprite):
    def __init__(self, animation_player):
        super().__init__()
        self.animation_player = animation_player

    def heal(self, player, strength, cost, groups):
        if player.energy >= cost:
            player.health += strength
            player.energy -= cost
            if player.health >= player.stats['health']:
                player.health = player.stats['health']
            self.animation_player.create_particles('aura', player.rect.center, groups)
            self.animation_player.create_particles('heal', player.rect.center + pygame.math.Vector2(0, -60), groups)

    def flame(self, player, cost, groups):
        if player.energy >= cost:
            player.energy -= cost
            self.define_skills_directions(player, groups, 'flame')

    def wind(self, player, cost, groups):
        if player.energy >= cost:
            player.energy -= cost
            self.define_skills_directions(player, groups, 'wind')

    def ice(self, player, cost, groups):
        if player.energy >= cost:
            player.energy -= cost
            self.define_skills_directions(player, groups, 'ice')

    def thunderball(self, player, cost, groups):
        if player.energy >= cost:
            player.energy -= cost
            self.define_skills_directions(player, groups, 'thunderball')

    def get_player_magic_direction(self, player):
        if player.status.split('_')[0] == 'right':
            return pygame.math.Vector2(1, 0)
        elif player.status.split('_')[0] == 'left':
            return pygame.math.Vector2(-1, 0)
        elif player.status.split('_')[0] == 'up':
            return pygame.math.Vector2(0, -1)
        else:
            return pygame.math.Vector2(0, 1)

    def define_skills_directions(self, player, groups, skill):
        for i in range(1, 6):
            direction = self.get_player_magic_direction(player)
            if direction.x:
                # horizontal
                offset_x = (direction.x * i) * TILESIZE
                x = player.rect.centerx + offset_x + randint(-TILESIZE // 6, TILESIZE // 6)
                y = player.rect.centery + randint(-TILESIZE // 6, TILESIZE // 6)
                self.animation_player.create_particles(skill, (x, y), groups)
            else:
                # vertical
                offset_y = (direction.y * i) * TILESIZE
                x = player.rect.centerx + randint(-TILESIZE // 6, TILESIZE // 6)
                y = player.rect.centery + offset_y + randint(-TILESIZE // 6, TILESIZE // 6)
                self.animation_player.create_particles(skill, (x, y), groups)
