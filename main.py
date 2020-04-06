from consts import *
from levels.control import Level


pygame.init()
pygame.display.set_caption("King of Preria")
level = Level()


while not mc.dead:
    if not level.created:
        level.create_level()
    level.is_finished()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mc.dead = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        mc.dead = True
    mc.control(keys)
    mc.is_dead()

    screen.fill(BG_COLOR)
    level.draw_level()
    screen.blit(mc.image, mc.rect)

    pygame.display.update()
    pygame.time.delay(DELAY)

    mc.update()
