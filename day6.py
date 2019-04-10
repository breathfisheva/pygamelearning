'''
pygame.draw.rect(Surface, color, Rect, width=0)
pygame.draw.polygon(Surface, color, pointlist, width=0)
pygame.draw.circle(Surface, color, pos, radius, width=0)
pygame.draw.ellipse(Surface, color, Rect, width=0)
pygame.draw.arc(Surface, color, Rect, start_angle, stop_angle, width=1)
pygame.draw.line(Surface, color, start_pos, end_pos, width=1)
pygame.draw.lines(Surface, color, closed, pointlist, width=1)
closed是一个布尔变量，指明是否需要多画一条线来使这些线条闭合（感觉就和polygone一样了），pointlist是一个点的数组。

'''

import pygame
from pygame.locals import *
import sys
from random import randint

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
points = []

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            #按任意键清屏，并把点回到原始状态
            points = []
            screen.fill((255, 255, 255))
        if event.type == MOUSEBUTTONDOWN:
            screen.fill((255, 255, 255))
            #画随机矩形
            rect_color = (randint(0,255), randint(0,255), randint(0,255))
            rect_position = (randint(0,639), randint(0,479))
            rect_widthheight = (639-randint(rect_position[0], 639), 479-randint(rect_position[1], 479))
            pygame.draw.rect(screen, rect_color, Rect(rect_position, rect_widthheight))

            #获取鼠标位置
            x, y = pygame.mouse.get_pos()
            points.append((x, y))

            #根据点的位置画椭圆
            pygame.draw.ellipse(screen, (0, 255, 0), (0, 0, x, y))
    pygame.display.update()

