from random import randint
import pygame


# sizes
WIDTH, HEIGHT = 800, 800
SIZE = 50
XY = (SIZE, SIZE)

# gameplay
BG_COLOR = (242, 188, 82)
DELAY = 15
HERO_STEP = 5


# sprites
class MainCharacter(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self, mc_group)
        self.image = pygame.transform.scale(pygame.image.load("img/mc.png").convert_alpha(), XY)
        self.rect = self.image.get_rect(center=(x, y))
        self.dead = False
        self.on_bomb = False

    def control(self, keys):
        if keys[pygame.K_d]:
            self.rect.x += HERO_STEP
            if is_stop_collision(self):
                self.rect.x -= HERO_STEP
        if keys[pygame.K_a]:
            self.rect.x -= HERO_STEP
            if is_stop_collision(self):
                self.rect.x += HERO_STEP
        if keys[pygame.K_w]:
            self.rect.y -= HERO_STEP
            if is_stop_collision(self):
                self.rect.y += HERO_STEP
        if keys[pygame.K_s]:
            self.rect.y += HERO_STEP
            if is_stop_collision(self):
                self.rect.y -= HERO_STEP

    def is_dead(self):
        if pygame.sprite.spritecollideany(self, enemy_group):
            self.dead = True


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self, wall_group)
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

mc = MainCharacter(map_scaling(17), map_scaling(15))
