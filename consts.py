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
BULLET_STEP = 10
ENEMY_STEP = 3


# sprites
class MainCharacter(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, mc_group)
        self.image = pygame.transform.scale(pygame.image.load("img/mc.png").convert_alpha(), XY)
        self.rect = self.image.get_rect(center=(map_scaling(1), map_scaling(1)))
        self.go_to_middle()
        self.dead = False
        self.on_bomb = False
        self.timer = 0

    def go_to_middle(self):
        self.rect = self.image.get_rect(center=(map_scaling(17), map_scaling(15)))

    def control(self, keys):
        if keys[pygame.K_w]:
            self.rect.y -= HERO_STEP
            if pygame.sprite.spritecollideany(self, wall_group):
                self.rect.y += HERO_STEP
        if keys[pygame.K_d]:
            self.rect.x += HERO_STEP
            if pygame.sprite.spritecollideany(self, wall_group):
                self.rect.x -= HERO_STEP
        if keys[pygame.K_s]:
            self.rect.y += HERO_STEP
            if pygame.sprite.spritecollideany(self, wall_group):
                self.rect.y -= HERO_STEP
        if keys[pygame.K_a]:
            self.rect.x -= HERO_STEP
            if pygame.sprite.spritecollideany(self, wall_group):
                self.rect.x += HERO_STEP

    def is_ready(self, keys):
        if self.timer == 0:
            self.fire(keys)
        else:
            self.timer -= 1

    def fire(self, keys):
        bullet = Bullet("")
        if keys[pygame.K_RIGHT] and keys[pygame.K_UP]:
            self.timer = 10
            bullet.direction = "right-up"
        elif keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
            self.timer = 10
            bullet.direction = "right-down"
        elif keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
            self.timer = 10
            bullet.direction = "left-down"
        elif keys[pygame.K_LEFT] and keys[pygame.K_UP]:
            self.timer = 10
            bullet.direction = "left-up"
        elif keys[pygame.K_UP]:
            self.timer = 10
            bullet.direction = "up"
        elif keys[pygame.K_RIGHT]:
            self.timer = 10
            bullet.direction = "right"
        elif keys[pygame.K_DOWN]:
            self.timer = 10
            bullet.direction = "down"
        elif keys[pygame.K_LEFT]:
            self.timer = 10
            bullet.direction = "left"
        if self.timer == 10:
            bullets.append(bullet)
            bullet_group.add(bullet)

    def is_dead(self):
        if pygame.sprite.spritecollideany(self, enemy_group):
            self.dead = True


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, enemy_group)
        self.image = pygame.transform.scale(pygame.image.load("img/enemy.png").convert_alpha(), XY)
        self.place = randint(1, 4)
        self.rect = self.image.get_rect(center=self.spawn())
        self.dead = False

    def spawn(self):
        if self.place == 1:
            return map_scaling(randint(7, 9) * 2 + 1), map_scaling(1)
        if self.place == 2:
            return map_scaling(31), map_scaling(randint(7, 9) * 2 + 1)
        if self.place == 3:
            return map_scaling(randint(7, 9) * 2 + 1), map_scaling(31)
        if self.place == 4:
            return map_scaling(1), map_scaling(randint(7, 9) * 2 + 1)

    def movement(self):
        if self.rect.y > mc.rect.y:
            self.rect.y -= ENEMY_STEP
        elif self.rect.x < mc.rect.x:
            self.rect.x += ENEMY_STEP
        elif self.rect.y < mc.rect.y:
            self.rect.y += ENEMY_STEP
        elif self.rect.x > mc.rect.x:
            self.rect.x -= ENEMY_STEP

    def is_dead(self):
        if pygame.sprite.spritecollideany(self, bullet_group):
            self.dead = True


class Bullet(pygame.sprite.Sprite):
    def __init__(self, direction):
        pygame.sprite.Sprite.__init__(self, bullet_group)
        self.image = pygame.transform.scale(pygame.image.load("img/blow.png").convert_alpha(), BULLET_XY)
        self.rect = self.image.get_rect(center=(mc.rect.x + SIZE / 2, mc.rect.y + SIZE / 2))
        self.direction = direction
        self.stopped = False

    def is_stopped(self):
        if pygame.sprite.spritecollideany(self, wall_group) or pygame.sprite.spritecollideany(self, enemy_group):
            self.stopped = True

    def move(self):
        if "up" in self.direction:
            self.rect.y -= BULLET_STEP
        if "right" in self.direction:
            self.rect.x += BULLET_STEP
        if "down" in self.direction:
            self.rect.y += BULLET_STEP
        if "left" in self.direction:
            self.rect.x -= BULLET_STEP


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
        bullet.is_stopped()
        if not bullet.stopped:
            bullet_group.add(bullet)
            bullet.move()
            screen.blit(bullet.image, (bullet.rect.x, bullet.rect.y))


# pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))
mc_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
wall_group = pygame.sprite.Group()

mc = MainCharacter()
bullets = []
