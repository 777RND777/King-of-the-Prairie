from consts import *
import levels.level_1 as l1
import levels.level_2 as l2
import levels.level_3 as l3


class Level:
    def __init__(self):
        self.number = 0
        self.created = False
        self.walls = []
        self.enemies = []
        self.spawned_enemies = []
        self.spawned = 0
        self.spawn_timer = 50

    def create_level(self):
        self.created = True
        self.number += 1
        self.get_level()

    def get_level(self):
        if self.number == 1:
            self.walls = l1.create_walls()
            self.update_walls()
            self.enemies = l1.enemies
        elif self.number == 2:
            wall_group.empty()
            self.walls = l1.create_walls()
            self.walls += l2.walls
            self.update_walls()
        elif self.number == 3:
            self.walls = l1.create_walls()
            self.walls += l3.walls
            self.update_walls()

    def update_walls(self):
        wall_group.empty()
        for wall in self.walls:
            wall_group.add(wall)

    def spawn_enemy(self):
        if self.spawned < len(self.enemies):
            if self.spawn_timer == 0:
                self.spawned_enemies.append(self.enemies[self.spawned])
                self.spawned += 1
                self.spawn_timer = 50
            else:
                self.spawn_timer -= 1

    def draw_level(self):
        self.draw_walls()
        self.draw_enemies()

    def draw_walls(self):
        for wall in self.walls:
            screen.blit(wall.image, (wall.rect.x, wall.rect.y))

    def draw_enemies(self):
        enemy_group.empty()
        for enemy in self.spawned_enemies:
            enemy.is_dead()
            if not enemy.dead:
                enemy_group.add(enemy)
                screen.blit(enemy.image, (enemy.rect.x, enemy.rect.y))

    def is_finished(self):
        if len(self.spawned_enemies) == len(self.enemies) and len(enemy_group) == 0:
            self.created = False
