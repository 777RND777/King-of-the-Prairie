from consts import *


def create_walls():
    level = []
    for i in range(7):
        level.append(Wall(SIZE / 2, (i + 0.5) * SIZE))
        level.append(Wall(WIDTH - SIZE / 2, (i + 0.5) * SIZE))
    for i in range(10, 16):
        level.append(Wall(SIZE / 2, (i + 0.5) * SIZE))
        level.append(Wall(WIDTH - SIZE / 2, (i + 0.5) * SIZE))
    for i in range(1, 7):
        level.append(Wall((i + 0.5) * SIZE, SIZE / 2))
        level.append(Wall((i + 0.5) * SIZE, HEIGHT - SIZE / 2))
    for i in range(10, 15):
        level.append(Wall((i + 0.5) * SIZE, SIZE / 2))
        level.append(Wall((i + 0.5) * SIZE, HEIGHT - SIZE / 2))
    return level
