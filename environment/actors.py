import math

import pygame

class Misile(pygame.sprite.Sprite):

    def __init__(self, x, y, angle, color):
        super().__init__()
        self.color = color

        self.image = pygame.Surface([8, 8])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.belongs_to = None
        self.rect.x = x
        self.rect.y = y
        self.angle = angle
        self.current_step = 0

    def step(self):
        self.current_step+=0.1
        if self.current_step > 10:
            self.current_step = 10
        self.rect.x = self.rect.x + self.current_step * math.cos(math.radians(self.angle))
        self.rect.y = self.rect.y + self.current_step * math.sin(math.radians(self.angle))

        print(self.rect.x, self.rect.y)

class Tank(pygame.sprite.Sprite):

    def __init__(self, x,y, rotation , color, name):
        super().__init__()
        self.color = color
        self.name = name
        self.rotation = rotation
        self.x = x
        self.y = y

        self.image = pygame.Surface([32,32])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.firing = False

        self.rect.x = x
        self.rect.y = y

    def up(self):
        self.rect.y-=1

    def down(self):
        self.rect.y+=1

    def left(self):
        self.rect.x -= 1

    def right(self):
        self.rect.x += 1

    def rotate_left(self):
        self.angle-=1

    def rotate_right(self):
        self.angle+=1

    def fire(self, angle):

        if not self.firing:
            self.firing = True

