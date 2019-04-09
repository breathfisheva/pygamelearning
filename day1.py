'''
1.set_mode会返回一个Surface对象，代表了在桌面上出现的那个窗口，三个参数第一个为元祖，代表分 辨率（必须）；第二个是一个标志位，具体意思见下表，如果不用什么特性，就指定0；第三个为色深。
FULLSCREEN	创建一个全屏窗口
DOUBLEBUF	创建一个“双缓冲”窗口，建议在HWSURFACE或者OPENGL时使用
HWSURFACE	创建一个硬件加速的窗口，必须和FULLSCREEN同时使用
OPENGL	创建一个OPENGL渲染的窗口
RESIZABLE	创建一个可以改变大小的窗口
NOFRAME	创建一个没有边框的窗口


2.blit是个重要函数，第一个参数为一个Surface对象，第二个为左上角位置。画完以后一定记得用update更新一下，否则画面一片漆黑。
'''


background_image_filename = 'sushiplate.jpg'
mouse_image_filename = 'fugu.png'

import pygame
from pygame.locals import *
from sys import exit

#1.初始化：为硬件做准备
pygame.init()

#2.窗口：创建窗口指定大小 & 设置窗口标题
screen = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption("Hello World!")

#3.图片（背景图片，光标图片）：加载图片并转换为surface对象
background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert()

#4.游戏主循环
while True:
    #4.1 事件：监测事件，如果接收到退出事件则退出程序
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    #4.2 背景图片画上去
    screen.blit(background, (0,0))

    #4.3 让光标图案跟着鼠标移动
    # 获取鼠标位置
    x, y = pygame.mouse.get_pos()
    # 计算出光标的左上角的位置
    x -= mouse_cursor.get_width()/2
    y -= mouse_cursor.get_height()/2
    # 把光标画上去
    screen.blit(mouse_cursor, (x,y))

    #4.4 刷新下画面，否则会是黑屏
    pygame.display.update()


