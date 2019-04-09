'''
代码实现功能：打印除所有的事件信息，在你移动鼠标的时候产生了海量的信息，让我们知道了Pygame是多么的繁忙

1 pygame.event.get()    获取事件的返回值，使用event.type == 进行区分 -- get events from the queue
2 pygame.event.wait()    等待发生一个事件才会继续下去；
3 pygame.event.poll()    会根据现在的情形返回一个真实的事件 -- get a single event from the queue
4 pygame.event.set_blocked(事件名)    过滤
5 pygame.event.set_allowed() 允许事件

自定义事件
1 my_event = pygame.event.Event(KEYDOWN,key=K_SPACE,mod=0,unicode=u' ')
2 pygame.event.post(my_event)

'''

import pygame
from pygame.locals import *
from sys import exit

#1.初始化：为硬件做准备
pygame.init()

#2.窗口：创建窗口指定大小
SCREEN_SIZE = (640, 480)
screen = pygame.display.set_mode((640, 480), 0, 32)

#3.设置字体样式大小
font = pygame.font.SysFont("arial", 16)
font_height = font.get_linesize()

#4.存事件的名称
event_text = []

#5.游戏主循环
while True:
    event = pygame.event.wait()
    #获取事件名称
    event_text.append(str(event))

    #窗口高度除以字体高度取负数的切片操作，保证只保留一个屏幕的文字，而且是最新的
    event_text = event_text[-int(SCREEN_SIZE[1]/font_height):]

    #如果接收到退出事件则退出程序
    if event.type == QUIT:
        exit()

    #设置背景色
    screen.fill((255,255,255))

    #找到一个合适的起笔位置，最下面开始起笔，但是保留一行空
    y = SCREEN_SIZE[1] - font_height

    for text in reversed(event_text):
        screen.blit(font.render(text, True, (0, 0, 0)), (0,y))
        #把笔提一行
        y -= font_height

    pygame.display.update()