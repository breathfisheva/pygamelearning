import pygame, random, sys, time
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640, 480))

snake_segments_position = [[100, 100], [80, 100], [60, 100]]
head = [100, 100]

#1.食物的初始位置
food_position = [160, 100]
#2.标记是否迟到苹果
eatfood = False

direction = 'right'

clock = pygame.time.Clock()

def gameOver():
    textfont = pygame.font.SysFont('arial', 67)
    oversurf = textfont.render('Game Over', True, (150, 150, 150))
    textposition = oversurf.get_rect()
    textposition.midtop = (320, 10) #让text居中
    screen.blit(oversurf, textposition)
    pygame.display.update()
    time.sleep(5)
    pygame.quit()
    exit()

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT:
                direction = 'right'
            if event.key == K_LEFT:
                direction = 'left'
            if event.key == K_UP:
                direction = 'up'
            if event.key == K_DOWN:
                direction = 'down'

    if direction == 'right':
        head[0] += 20
    if direction == 'left':
        head[0] -= 20
    if direction == 'up':
        head[1] -= 20
    if direction == 'down':
        head[1] += 20

    snake_segments_position.insert(0, (head[0], head[1])) #这里要传的head里面具体的值，如果直接把head传进去，会导致之前的值也变化。

    #3.如果头的位置等于苹果的位置，则迟到苹果，eatfood设为True
    if head == food_position:
        eatfood = True
    #4.如果没吃到苹果，则蛇的长度不会变，尾巴的坐标要丢掉，保存蛇长度不变位置变化
    else:
        snake_segments_position.pop()
    #5.注意新画的东西都要在screen.fill后面，也就是重新起一个干净的屏幕画蛇和苹果

    print(snake_segments_position)
    screen.fill((0, 0, 0))
    for body in snake_segments_position:
        pygame.draw.rect(screen, (255, 255, 255), Rect(body[0], body[1], 20, 20)) #身体的一个小单位是边长20的正方形
    #6.画苹果
    pygame.draw.rect(screen, (255, 0, 0), Rect(food_position[0], food_position[1], 20, 20))

    #7.如果吃到苹果则在另一个位置再生成一个苹果，并且把eatfood设为False
    if eatfood == True:
        food_position = [random.randrange(1, 32)*20, random.randrange(1, 24)*20] #苹果的位置随机生成
        eatfood = False
    print(food_position)

    clock.tick(9)
    pygame.display.update()

    #判断是否退出
    #1.如果超出屏幕边界则退出
    if head[0] < 0 or head[0] > 640 or head[1] < 0 or head[1] > 480:
        gameOver()

    #2.如果撞到自己的身体则退出
    for body in snake_segments_position:
        if head == body:
            gameOver()
