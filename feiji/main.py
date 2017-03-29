# coding=utf-8

import time

import pygame


class PlayerPlane(object):
    def __init__(self, screen):
        self.bulletList = []

        planeImageName = 'G:\PythonCode\\feiji\img\hero.png'
        self.image = pygame.image.load(planeImageName).convert()

        self.x = 240
        self.y = 600
        self.bullet = ''
        self.speed = 5
        self.planName = 'player'

        self.bullet = []
        self.screen = screen

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))
        for temp in self.bullet:
            temp.draw()

    def keyHandle(self, keyValue):

        if keyValue == 'left':
            self.x -= 20
        elif keyValue == 'right':
            self.x += 20
        elif keyValue == 'space':
            print ('space')
            self.bullet.append(Bullet(self.screen, self.x + 40, self.y - 15))

        self.draw()


class Enemy(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        enmeyImageFile = 'G:\PythonCode\\feiji\img\enemy0.png'
        self.image = pygame.image.load(enmeyImageFile).convert()
        self.fowrd = 'right'

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def move(self):

        if self.fowrd == 'right':
            self.x += 2
            if self.x > 430:
                self.fowrd = 'left'
        else:
            self.x -= 2
            if self.x < 0:
                self.fowrd = 'right'


class Bullet(object):
    def __init__(self, screen, x, y):
        print ("调用了这个子弹")
        bgImage = 'G:\PythonCode\\feiji\\bullet.png'
        self.zidan = pygame.image.load(bgImage).convert()
        self.x = x
        self.y = y
        self.screen = screen

    def draw(self):
        self.y -= 4
        self.screen.blit(self.zidan, (self.x, self.y))


if __name__ == '__main__':
    screen = pygame.display.set_mode((480, 800), 0, 32)
    bgImageFile = 'G:\PythonCode\\feiji\\background.png'
    background = pygame.image.load(bgImageFile).convert()

    player = PlayerPlane(screen)
    enemt = Enemy()
    while True:
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print ("exit")
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    print ('left')
                    player.keyHandle('left')
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    print ('right')
                    player.keyHandle('right')
                elif event.key == pygame.K_SPACE:
                    player.keyHandle('space')
                    print ('space')

        player.draw()
        enemt.move()
        enemt.draw()
        pygame.display.update()

        time.sleep(0.01)
