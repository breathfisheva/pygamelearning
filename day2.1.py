'''
处理键盘事件:如果按键盘左键则左移，右键则右移
'''
background_image_filename = 'sushiplate.jpg'

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
background = pygame.image.load(background_image_filename).convert()

x, y = 0, 0
move_x, move_y = 0, 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            #如果是左方向键，则把x坐标减一
            if event.key == K_LEFT:
                move_x = -1
            elif event.key == K_RIGHT:
                move_x = 1
            elif event.key == K_UP:
                move_y = -1
            elif event.key == K_DOWN:
                move_y = 1
        #如果用户放开了键盘，图就不动了
        elif event.type == KEYUP:
            move_x = 0
            move_y = 0

        #计算出新的x，y坐标
        x += move_x
        y += move_y

        #在新的位置上画图
        screen.fill((0, 0, 0))
        screen.blit(background, (x,y))
        pygame.display.update()
