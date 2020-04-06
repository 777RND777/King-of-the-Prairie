from random import randint
import pygame


# sizes
WIDTH, HEIGHT = 800, 800
SIZE = 50
BULLET_SIZE = 5
XY = (SIZE, SIZE)
BULLET_XY = (BULLET_SIZE, BULLET_SIZE)

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
        self.fired = False
        self.timer = 0

    def control(self, keys):
        if keys[pygame.K_d]:
            self.rect.x += HERO_STEP
            if pygame.sprite.spritecollideany(self, wall_group):
                self.rect.x -= HERO_STEP
        if keys[pygame.K_a]:
            self.rect.x -= HERO_STEP
            if pygame.sprite.spritecollideany(self, wall_group):
                self.rect.x += HERO_STEP
        if keys[pygame.K_w]:
            self.rect.y -= HERO_STEP
            if pygame.sprite.spritecollideany(self, wall_group):
                self.rect.y += HERO_STEP
        if keys[pygame.K_s]:
            self.rect.y += HERO_STEP
            if pygame.sprite.spritecollideany(self, wall_group):
                self.rect.y -= HERO_STEP

    def fire(self, keys):
        if keys[pygame.K_UP]:
            self.fired = True
            self.timer = 10
            bullet = Bullet("up")
            bullets.append(bullet)
            bullet_group.add(bullet)

    def timer_action(self):
        self.timer -= 1
        if self.timer == 0:
            self.fired = False

    def is_dead(self):
        if pygame.sprite.spritecollideany(self, enemy_group):
            self.dead = True


class Bullet(pygame.sprite.Sprite):
    def __init__(self, direction):
        pygame.sprite.Sprite.__init__(self, bullet_group)
        self.image = pygame.transform.scale(pygame.image.load("img/blow.png").convert_alpha(), BULLET_XY)
        self.rect = self.image.get_rect(center=(mc.rect.x + SIZE / 2, mc.rect.y + SIZE / 2))
        self.direction = direction
        self.stopped = False

    def is_stopped(self):
        if pygame.sprite.spritecollideany(self, wall_group):
            self.stopped = True

    def move(self):
        if self.direction == "up":
            self.rect.y -= 10


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self, wall_group)
        self.image = pygame.transform.scale(pygame.image.load("img/wall.png").convert_alpha(), XY)
        self.rect = self.image.get_rect(center=(x, y))


def map_scaling(num):
    return num * SIZE / 2


def draw_bullets():
    bullet_group.empty()
    for bullet in bullets:
        bullet.move()
        bullet.is_stopped()
        if not bullet.stopped:
            bullet_group.add(bullet)
            screen.blit(bullet.image, (bullet.rect.x, bullet.rect.y))


# pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))
mc_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
wall_group = pygame.sprite.Group()

mc = MainCharacter(map_scaling(17), map_scaling(15))
bullets = []
