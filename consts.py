from random import randint
import pygame


# sizes
WIDTH, HEIGHT = 1050, 770
SIZE = 50
XY = (SIZE, SIZE)

# gameplay
BG_COLOR = (0, 149, 0)
DELAY = 5


# sprites
class MainCharacter(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self, mc_group)
        self.image = pygame.transform.scale(pygame.image.load("img/mc.png").convert_alpha(), XY)
        self.rect = self.image.get_rect(center=(x, y))
        self.dead = False
        self.on_bomb = False

    def control(self, keys):
        if keys[pygame.K_RIGHT]:
            self.rect.x += 2
            if is_stop_collision(self):
                self.rect.x -= 2
        if keys[pygame.K_LEFT]:
            self.rect.x -= 2
            if is_stop_collision(self):
                self.rect.x += 2
        if keys[pygame.K_UP]:
            self.rect.y -= 2
            if is_stop_collision(self):
                self.rect.y += 2
        if keys[pygame.K_DOWN]:
            self.rect.y += 2
            if is_stop_collision(self):
                self.rect.y -= 2

    def is_dead(self):
        if pygame.sprite.spritecollideany(self, enemy_group):
            self.dead = True


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("img/wall.png").convert_alpha(), XY)
        self.rect = self.image.get_rect(center=(x, y))


def map_scaling(num):
    return num * SIZE / 2


def is_stop_collision(sprite):
    if pygame.sprite.spritecollideany(sprite, wall_group):
        return True
    if pygame.sprite.spritecollideany(sprite, bullet_group):
        if not sprite.on_bomb:
            return True
    else:
        sprite.on_bomb = False
    return False


# pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))
mc_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
wall_group = pygame.sprite.Group()

mc = MainCharacter(map_scaling(15), map_scaling(11))
