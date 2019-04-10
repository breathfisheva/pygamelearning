'''
图像

1.创建surface对象
- pygame.image.load

- bland_alpha_surface = pygame.Surface((256, 256), flags=SRCALPHA, depth=32)
第一个参数是尺寸：
如果不指定尺寸，那么就创建一个和屏幕一样大小的。
第二个参数是flags：
SRCALPHA – 有Alpha通道的surface，如果你需要透明，就要这个选项。这个选项的使用需要第二个参数为32~
第三个参数是depth：

2.转换Surfaces
不用在意surface里的具体内容，把这些surface转换一下以获得更高的性能

background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()
第一句是普通的转换，相同于display；第二句是带alpha通道的转换。
如果你给convert或者conver_alpha一个surface对象作为参数，那么这个会被作为目标来转换。

2.矩形对象(Rectangle Objects)
my_rect1 = (100, 100, 200, 150)
my_rect2 = ((100, 100), (200, 150))

3.剪裁(Clipping)
我们可以使用set_clip来设定，使用get_clip来获得这个区域。
screen.set_clip(0, 400, 200, 600)
draw_map()

4.子表面（在一个图片上扣出需要的图）
比如从font.png上扣除字母a和字母b
my_font_image = Pygame.load("font.png")
letters = []
letters["a"] = my_font_image.subsurface((0,0), (80,80))
letters["b"] = my_font_image.subsurface((80,0), (80,80))

5.填充surface（清屏）
screen.fill((0, 0, 0))

6.设置surface像素
设置某个像素点的像素值
screen.set_at((0,0), (100,100))

7.获得Surface上的像素
get_at

8.锁定surface

9.Blitting 把图像画到屏幕上
blit(self, source, dest, area=None, special_flags=0)

'''


import pygame
pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

background_image_filename = 'sushiplate.jpg'
background = pygame.image.load(background_image_filename).convert()

#把sushiplate的某个部分画出来
screen.blit(background, (300, 200), (100* 2, 0, 100, 100))

pygame.display.update()
