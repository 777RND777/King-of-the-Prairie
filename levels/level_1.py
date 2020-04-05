from consts import *


def create_walls():
    level = []
    for i in range(11):
        level.append(Wall(SIZE / 2, (i + 0.5) * SIZE))
        level.append(Wall(WIDTH - SIZE / 2, (i + 0.5) * SIZE))
    for i in range(1, 14):
        level.append(Wall((i + 0.5) * SIZE, SIZE / 2))
        level.append(Wall((i + 0.5) * SIZE, HEIGHT - SIZE / 2))
    for i in range(1, 7):
        for j in range(1, 5):
            level.append(Wall(2 * i * SIZE + SIZE / 2, 2 * j * SIZE + SIZE / 2))
    return level
