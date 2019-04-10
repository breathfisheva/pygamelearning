'''
字体:
text_surface = my_font.render("Pygame is cool!", True, (0,0,0), (255, 255, 255))
第一个参数是写的文字；第二个参数是个布尔值，以为这是否开启抗锯齿，就是说True的话字体会比较平滑，不过相应的速度有一点点影响；第三个参数是字体的颜色；第四个是背景色，如果你想没有背景色（也就是透明），那么可以不加这第四个参数。


1.获取当前系统所有可用的字体
print(pygame.font.get_fonts())

2.初始化pygame
pygame.init()

3.使用arial字体，大小是16
my_font = pygame.font.SysFont('arial', 16)

3.使用ttf字体，前面用的字体和操作系统有关，如果操作系统不支持就会使用一个默认的字体，可是使用ttf字体则可以把字体文件随游戏一起分发，避免用户机器上没有需要的字体
my_font = pygame.font.SysFont("my_font.ttf", 16)

4.render
text_surface = my_font.render("hello world", True, (0,0,0), (255, 255, 255))
'''

#1.把文字存成一个图片
# my_name = "lucy liu"
# import pygame
# pygame.init()
# my_font = pygame.font.SysFont("arial", 64)
# name_surface = my_font.render(my_name, True, (0, 0, 0), (255, 255, 255))
# pygame.image.save(name_surface, "name.png")

#2.支持中文保存成图片
# my_name = "呼啦"
# import pygame
# pygame.init()
# my_font = pygame.font.SysFont("simsunnsimsun", 64)
# name_surface = my_font.render(my_name, True, (0, 0, 0), (255, 255, 255))
# pygame.image.save(name_surface, "name.png")

#3.显示文字
import pygame
from pygame.locals import * #这样像event.type 的QUIT关键字才能识别
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
font = pygame.font.SysFont("simsunnsimsun", 40)
text_surface = font.render(u"您好", True, (0, 0, 255))

x = 0
y = (480 - text_surface.get_height())/2

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    x -=12 #文字滚动太快的话，改改这个数字

    #如果这个字已经跑到屏幕外面了，则从右边开始出现
    if x < -text_surface.get_width():
        x = 640 - text_surface.get_width()

    screen.blit(text_surface, (x, y))
    pygame.display.update()




