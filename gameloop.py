import pygame

from environment.actors import Tank, Misile

t1 = Tank(10,50, 90, [0,255,0], "T1")
t2 = Tank(650,350, 90, [0,0,255], "T2")

pygame.init()

screen_width  = 700
screen_heigth = 400
screen = pygame.display.set_mode([screen_width ,screen_heigth])

sprite_group = pygame.sprite.Group()

sprite_group.add(t1)
sprite_group.add(t2)

clock = pygame.time.Clock()
game_over = False

mis = Misile(10,50, 27, [0,255,0])
sprite_group.add(mis)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    mis.step()
    if mis.rect.y > 400:
        mis.rect.y = 0
    if mis.rect.x > 700:
        mis.rect.x = 0

    screen.fill([0,0,0])

    sprite_group.draw(screen)

    clock.tick(60)

    pygame.display.flip()

pygame.quit()