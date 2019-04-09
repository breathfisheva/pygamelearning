'''
1. 获取机器支持的显示模式
'''

# import pygame
# pygame.init()
# print(pygame.display.list_modes())


'''
2. 按f键，屏幕在大小屏之间切换
'''
# background_image_filename = 'sushiplate.jpg'
#
# import pygame
# from pygame.locals import *
# from sys import exit
#
# pygame.init()
# screen = pygame.display.set_mode((640, 480), 0, 32)
# background = pygame.image.load(background_image_filename).convert()
#
# Fullscreen = False
#
# while True:
#
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             exit()
#     if event.type == KEYDOWN:
#         if event.key == K_f:
#             Fullscreen = not Fullscreen
#             if Fullscreen:
#                 screen = pygame.display.set_mode((640, 480), FULLSCREEN, 32)
#             else:
#                 screen = pygame.display.set_mode((640, 480), 0, 32)
#
#     screen.blit(background, (0, 0))
#     pygame.display.update()

''''
3.可改变窗口尺寸
虽然一般的程序窗口都能拖边框来改变大小，pygame的默认显示窗口是不行的，而事实上，很多游戏确实也不能改变显示窗口的大小，
我们可以使用一个参数来改变这个默认行为。

set_mode(SCREEN_SIZE, RESIZABLE, 32)
event.type == VIDEORESIZE
'''

background_image_filename = 'sushiplate.jpg'

import pygame
from pygame.locals import *
from sys import exit

SCREEN_SIZE = (640, 480)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE,32)
background = pygame.image.load(background_image_filename).convert()

while True:
    event = pygame.event.wait()
    if event.type == QUIT:
        exit()
    elif event.type == VIDEORESIZE:
        SCREEN_SIZE = event.size
        screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
        pygame.display.set_caption(" window resized to " + str(event.size))

    #随着把背景图案重新填满窗口
    screen_width, screen_height = SCREEN_SIZE
    for y in range(0, screen_height, background.get_height()):
        for x in range(0, screen_width, background.get_width()):
            screen.blit(background, (x,y))
    pygame.display.update()









