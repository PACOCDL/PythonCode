# coding=utf-8
import pygame


class PlayerPlane(object):
    def __init__(self):
        self.bulletList = []

        planeImageName = 'G:\PythonCode\\feiji\img\\bg_02.jpg'
        self.image = pygame.image.load(planeImageName).convert()

        self.x = 230
        self.y = 600

        self.speed = 5

        self.planName = 'player'

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


if __name__ == '__main__':
    screen = pygame.display.set_mode((480, 800), 0, 32)
    bgImageFile = 'G:\PythonCode\\feiji\img\\bg_02.jpg'
    background = pygame.image.load(bgImageFile).convert()

    player = PlayerPlane()

    while True:
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print ("exit")
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    print ('left')
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    print ('right')
                elif event.key == pygame.K_SPACE:
                    print ('space')
        player.draw(screen)
        pygame.display.update()
        pygame.time.sleep(0.01)
