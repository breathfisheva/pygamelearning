'''
运动：直线运动
1.我们通过调节 “x += 10.” 来控制鱼游的运动，动画很简单，所以应该会很快；而有些时候动画元素很多，速度就会慢下来。

2.解决上述问题的方法，就是让我们的动画基于时间运作，使用时间来计算加减的量以在不同性能的计算机上获得一致的动画效果
clock = pygame.time.Clock()
time_passed = clock.tick() 返回一个上次调用的时间（以毫秒计）
time_passed = clock.tick(30) 参数30是游戏绘制的最大帧率，仅仅是“最大帧率”，并不能代表用户看到的就是这个数字，有些时候机器性能不足，或者动画太复杂，实际的帧率达不到这个值，我们需要一种更有效的手段来控制我们的动画效果。

'''

# #1.直线运动 基于位置
# background_image_filename = 'sushiplate.jpg'
# sprite_image_filename = 'fugu.png'
#
# import pygame
# from pygame.locals import *
# from sys import exit
#
# pygame.init()
# screen = pygame.display.set_mode((640, 480), 0, 32)
#
# background = pygame.image.load(background_image_filename).convert()
# sprite = pygame.image.load(sprite_image_filename).convert()
#
# #sprite起始坐标
# x = 0
#
# while True:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             exit()
#
#     screen.blit(background, (0, 0))
#     screen.blit(sprite, (x, 100))
#
#     x += 10 #如果你的机器性能太好以至于看不清，可以把这个数字改小一些
#
#     #如果移出屏幕则搬到开始位置
#     if x > 640:
#         x = 0
#
#     pygame.display.update()


#2. 直线运动，基于时间的
background_image_filename = 'sushiplate.jpg'
sprite_image_filename = 'fugu.png'

import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename)

clock = pygame.time.Clock()

x = 0
#每秒移动250个像素
speed = 250

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))
    screen.blit(sprite, (x, 100))

    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0 #time_passed是毫秒，不要忘了除以1000.0

    distance_moved = time_passed_seconds*speed #算出像素移动的距离
    x += distance_moved

    #如果归零则每次超过则重新从x=0的坐标处开始，也就是每次都从左右游到右边
    #可是-640，超过则出现在右边，效果就是从右往左游，一直重复
    if x > 640:
        x -= 640

    pygame.display.update()



