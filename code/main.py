import time

import pygame
import sys

from level import Level
from settings import *
from pygame import mixer


class Game:
    def __init__(self):
        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption('Zelda')
        self.clock = pygame.time.Clock()

        self.level = Level()

        # background sound
        mixer.music.load('../musics/rhythm.mp3')
        mixer.music.play(-1)
        mixer.music.set_volume(0.08)
        mixer.Sound('../musics/vamodançar.mp3').play().set_volume(0.3)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.level.toggle_menu()

            self.screen.fill('black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
