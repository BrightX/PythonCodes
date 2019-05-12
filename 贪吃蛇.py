"""
    贪吃蛇 — 亮亮的游戏
    作者：徐亮亮
    author: Bright Xu
"""

import pygame
from pygame.locals import *
from random import randint
from time import sleep
from base64 import b64decode
from sys import exit
from os import environ
from os import path
from os import remove

# 初始化数据
W = 810  # 地图宽度
H = 594  # 地图高度
speed = [27, 0]  # 初始运动方向，向右运动
score = 0  # 初始游戏分数为0


def main():
    global score
    pedometer = 0  # 统计步数

    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (300, 80)  # 设置窗口初始位置
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("贪吃蛇 — 亮亮的游戏")
    # 设置背景色
    bg_color = (230, 230, 230)
    screen_rect = screen.get_rect()

    # 加载蛇图像并获取其外接矩形
    snake_image = pygame.image.load('snake.png')
    snake_rect = snake_image.get_rect()
    snake_rect.center = screen_rect.center  # 将新蛇放在屏幕中央

    # 食物
    food_image = pygame.image.load('food.png')
    food_rect = food_image.get_rect()
    food_num = 0

    # 墙
    wall_image = pygame.image.load('wall.png')
    wall_rect = wall_image.get_rect()

    image_delete()  # 即时删除图片
    font_1 = pygame.font.SysFont("dengxian", 15, bold=True)
    font_2 = pygame.font.SysFont("dengxian", 40, bold=True)

    while True:
        # 监视键盘和鼠标事件
        for events in pygame.event.get():
            if events.type == pygame.QUIT:  # 响应鼠标退出程序
                exit()
            elif events.type == KEYDOWN:
                if events.key == K_q:  # 按下Q键退出程序
                    exit()
                elif events.key in [K_LEFT, K_a]:  # 向左移动
                    speed[0] = -snake_rect.width
                    speed[1] = 0
                elif events.key in [K_RIGHT, K_d]:  # 向右移动
                    speed[0] = snake_rect.width
                    speed[1] = 0
                elif events.key in [K_UP, K_w]:  # 向上移动
                    speed[0] = 0
                    speed[1] = -snake_rect.height
                elif events.key in [K_DOWN, K_s]:  # 向下移动
                    speed[0] = 0
                    speed[1] = snake_rect.height
                elif events.key == K_SPACE:  # 按下空格键暂停游戏
                    f = 1
                    while f:
                        sleep(0.5)
                        for event in pygame.event.get():
                            if events.type == pygame.QUIT:  # 响应鼠标退出程序
                                exit()
                            if event.type == KEYDOWN:
                                if event.key == K_SPACE:  # 再按下空格键继续游戏
                                    f = 0

        screen.fill(bg_color)  # 每次循环时都重绘屏幕

        # 屏幕边缘铺满墙
        wall_rect.bottom = 0
        for i in range((H // wall_rect.width)):  # 左边墙
            wall_rect.centerx = screen_rect.left
            wall_rect.bottom += wall_rect.height
            screen.blit(wall_image, wall_rect)
        wall_rect.bottom = 0
        for i in range((H // wall_rect.width)):  # 右边墙
            wall_rect.centerx = screen_rect.right
            wall_rect.bottom += wall_rect.height
            screen.blit(wall_image, wall_rect)
        wall_rect.left = 0
        for i in range((W // wall_rect.height)):  # 上边墙
            wall_rect.centery = screen_rect.top
            screen.blit(wall_image, wall_rect)
            wall_rect.left += wall_rect.width
        wall_rect.left = 0
        for i in range((W // wall_rect.height)):  # 下边墙
            wall_rect.centery = screen_rect.bottom
            screen.blit(wall_image, wall_rect)
            wall_rect.left += wall_rect.width

        g = 0
        # 蛇撞墙时，结束游戏
        if snake_rect.left <= int(wall_rect.width/2) or snake_rect.right >= W - wall_rect.width/2 + 1 \
                or snake_rect.top <= int(wall_rect.height/2) or snake_rect.bottom >= H - wall_rect.height/2 + 1:
            speed[0] = 0
            speed[1] = 0
            txt = "游戏结束"
            screen.blit(font_2.render(txt, True, (255, 0, 0)), (W/2 - 80, H/2 - 40))
            g = 1

        if abs(abs(snake_rect.centerx - food_rect.centerx) + abs(snake_rect.centery - food_rect.centery)) <= 1:
            score += 1  # 遇到食物加分
            food_num = 0

        grade = score//10 + 1    # 等级
        n = 10 + score//10    # 难度系数n
        if g == 0:
            pedometer += 1
        text = "        分数: {}          步数：{}           等级: {}".format(score, pedometer, grade)
        screen.blit(font_1.render(text, True, (0, 255, 0)), (0, 0))

        # 将食物放在屏幕随机位置，保证屏幕上只有一个食物
        if food_num == 0:
            food_rect.centerx = randint(1, W / 27 - 1) * 27
            food_rect.centery = randint(1, H / 27 - 1) * 27
            food_num += 1
        if food_num != 0:
            screen.blit(food_image, food_rect)

        # 蛇
        snake_rect = snake_rect.move(speed)
        screen.blit(snake_image, snake_rect)

        # 让最近绘制的屏幕可见
        pygame.display.flip()
        sleep(5 / n)  # 休眠函数，不然蛇跑的太快，n是我们定义的难度系数


def image_food():
    """生成食物位图"""
    string = b'iVBORw0KGgoAAAANSUhEUgAAABsAAAAbCAIAAAACtmMCAAAACXBIWXMAAAsTAAALEwEAmpwYAAAFHGlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNS42LWMxNDUgNzkuMTYzNDk5LCAyMDE4LzA4LzEzLTE2OjQwOjIyICAgICAgICAiPiA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPiA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyIgeG1sbnM6cGhvdG9zaG9wPSJodHRwOi8vbnMuYWRvYmUuY29tL3Bob3Rvc2hvcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RFdnQ9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZUV2ZW50IyIgeG1wOkNyZWF0b3JUb29sPSJBZG9iZSBQaG90b3Nob3AgQ0MgMjAxOSAoV2luZG93cykiIHhtcDpDcmVhdGVEYXRlPSIyMDE5LTAzLTAxVDIwOjMzOjEwKzA4OjAwIiB4bXA6TW9kaWZ5RGF0ZT0iMjAxOS0wMy0wMVQyMDo1MTowMSswODowMCIgeG1wOk1ldGFkYXRhRGF0ZT0iMjAxOS0wMy0wMVQyMDo1MTowMSswODowMCIgZGM6Zm9ybWF0PSJpbWFnZS9wbmciIHBob3Rvc2hvcDpDb2xvck1vZGU9IjMiIHBob3Rvc2hvcDpJQ0NQcm9maWxlPSJzUkdCIElFQzYxOTY2LTIuMSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDo1M2MxMDM3Yy02ZjM3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'
    file = open('food.png', 'wb')
    file.write(b64decode(string))
    file.close()


def image_snake():
    """生成蛇位图"""
    string = b'iVBORw0KGgoAAAANSUhEUgAAABsAAAAbCAIAAAACtmMCAAAACXBIWXMAAAsTAAALEwEAmpwYAAAGymlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNS42LWMxNDUgNzkuMTYzNDk5LCAyMDE4LzA4LzEzLTE2OjQwOjIyICAgICAgICAiPiA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPiA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIiB4bWxuczpzdEV2dD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlRXZlbnQjIiB4bWxuczpkYz0iaHR0cDovL3B1cmwub3JnL2RjL2VsZW1lbnRzLzEuMS8iIHhtbG5zOnBob3Rvc2hvcD0iaHR0cDovL25zLmFkb2JlLmNvbS9waG90b3Nob3AvMS4wLyIgeG1wOkNyZWF0b3JUb29sPSJBZG9iZSBQaG90b3Nob3AgQ0MgMjAxOSAoV2luZG93cykiIHhtcDpDcmVhdGVEYXRlPSIyMDE5LTAzLTAxVDE2OjM4OjUyKzA4OjAwIiB4bXA6TWV0YWRhdGFEYXRlPSIyMDE5LTAzLTAxVDE2OjUzOjAxKzA4OjAwIiB4bXA6TW9kaWZ5RGF0ZT0iMjAxOS0wMy0wMVQxNjo1MzowMSswODowMCIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDo5ODY5Mzk0MC1hNmZlLTdiNDItOWUxMy1jOGU3YTAwYTVhNjAiIHhtcE1NOkRvY3VtZW50SUQ9ImFkb2JlOmRvY2lkOnBob3Rvc2hvcDo0ZjAyZjMwMC04ZDExLWZkNDAtOTBmZS03Mzk2MjhiYzEzZDkiIHhtcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD0ieG1wLmRpZDo0ZDQwMDRiZi04ZmZlLTdiNDItOTQyNy0zOWI0ZDM5NmQzNDQiIGRjOmZvcm1hdD0iaW1hZ2UvcG5nIiBwaG90b3Nob3A6Q29sb3JNb2RlPSIzIiBwaG90b3Nob3A6SUNDUHJvZmlsZT0ic1JHQiBJRUM2MTk2Ni0yLjEiPiA8eG1wTU06SGlzdG9yeT4gPHJkZjpTZXE+IDxyZGY6bGkgc3RFdnQ6YWN0aW9uPSJjcmVhdGVkIiBzdEV2dDppbnN0YW5jZUlEPSJ4bXAuaWlkOjRkNDAwNGJmLThmZmUtN2I0Mi05NDI3LTM5YjRkMzk2ZDM0NCIgc3RFdnQ6d2hlbj0iMjAxOS0wMy0wMVQxNjozODo1MiswODowMCIgc3RFdnQ6c29mdHdhcmVBZ2VudD0iQWRvYmUgUGhvdG9zaG9wIENDIDIwMTkgKFdpbmRvd3MpIi8+IDxyZGY6bGkgc3RFdnQ6YWN0aW9uPSJzYXZlZCIgc3RFdnQ6aW5zdGFuY2VJRD0ieG1wLmlpZDpjOTU5NTc1NC00ZmRhLTRjNGUtYjIwNS1kZjM2MDQ2ODBkYTEiIHN0RXZ0OndoZW49IjIwMTktMDMtMDFUMTY6Mzg6NTIrMDg6MDAiIHN0RXZ0OnNvZnR3YXJlQWdlbnQ9IkFkb2JlIFBob3Rvc2hvcCBDQyAyMDE5IChXaW5kb3dzKSIgc3RFdnQ6Y2hhbmdlZD0iLyIvPiA8cmRmOmxpIHN0RXZ0OmFjdGlvbj0ic2F2ZWQiIHN0RXZ0Omluc3RhbmNlSUQ9InhtcC5paWQ6OTg2OTM5NDAtYTZmZS03YjQyLTllMTMtYzhlN2EwMGE1YTYwIiBzdEV2dDp3aGVuPSIyMDE5LTAzLTAxVDE2OjUzOjAxKzA4OjAwIiBzdEV2dDpzb2Z0d2FyZUFnZW50PSJBZG9iZSBQaG90b3Nob3AgQ0MgMjAxOSAoV2luZG93cykiIHN0RXZ0OmNoYW5nZWQ9Ii8iLz4gPC9yZGY6U2VxPiA8L3htcE1NOkhpc3Rvcnk+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+UFMLDwAABFhJREFUSImVlV9MWmcUwM+9XP5c8Api6Iw6itdmqdWsK8ZJm4VkrJs1uoTQYcqDS1NbE4zJXPbgtpA0Ln1xcf5JjA8+rRlNNNg+LGncS7cguqjYNnFV1624Crcowqig7AJeLnu4d8o/O3ueDuec73fPOd/hfIjf7wcAAEin00aj0e12wxHS1NSk1Wq7u7sRBDkqBgCQA6LFYvE9dgHAepTVXhAQ8txQ53SKU2w2W1dX1/8TGxsbr6oC5VLEOpsYvCOpq0c5+6YvTcfS5GkUAJ48ZB/8yNyfZKqrq2dmZgomyx/zer0A8LM/demkKCfi9gjTZUpyel09+lmfyDYk9ng8er2+YI48sbe3V73vH9CJZUJYbis6x6IHEUVyhJBn5aJvFnDQsbGxI6uenp7u6Oi4ViNmWRYAlCRiuCUQyXhQdCddrMgtcORm8v4k4/V6MQwrQOSgoVAIAAKBgMPhUL3pN13FpLJcEFEhPVkWB4AtKv3pRdputxsMhsLETPF6vWaz2efz5bsuf1H6wcfYqbJdAPjyWiIS0LhcrswALP8MAKjV6oWFhWAwSNN0pn14eHjiu4mqeg1HfLsB/X7Ek3O2MJETlUqVY+np6ZmYmGASLPcTlyEAwDBMZitReH1JxHmlVHX0PL6WiCW8ojxRgFigaoZhlpaWZmdnHQ5HQaLgVa3KJqbTabvdPjo66vP5TtWgZB1S9RaK5w6QSEHwf/AkIgaIj4+Pd3Z2HrQya3osFovT6Wy7Lmy9gpVVvmrBcOJeKXo0k7w7sgMAq6urCoUiizg/P28ymWxDYn2zgLNQYWkgIkkyghzQ6fJoiSwBAIueUpk4he+Fx7/df/RryuPx4DietXvUdcGbQ/xdPQ/Knm7mbTQAXMjoa7a5761QikrlP7WVO3vR9I3WuIIgXS5XVh9P1BDPtlBuemPB5LY7QK3GMwPOnUe0HwkAkEAE//1FMZJKyaVJACgqRqxfiW597qFp+pBIkqR7epHUVSQYQXkJXXsmUXsGAIT5aT7bIp4HZZtP6R9sm4N3JJVKFACK3pAAJKampg6J/f39ZrN5/m5Yd1lJhaUyMSPCUjJxKpMVpYWxBJZiEepJbPKbTQCg/mK53bxD84v1kKhWq0mSdE46N5bpd5rkVWclIpn4ZSw3wb836Ic/7f72IAoAbdeFlz7BACAQwaNxoUajMRqNh8SBgYH19XUAoNZoao1fEJU1eEk5X3h8j/1zYU97QaCUg/Vr0dl3Ue6poMLStRfFrnshACVBENgBzuFwtLYHzhvwvElkMnRppoMbr9CuZPuP2K5HOTg4yFcdjUYdDkfzjWjDxWIGgArnX8Z/7BQSSwgzGwosu74YeXxPZjKZdDodT5ybm/P5fBINuUIde3GwbCKS2FimXVNRBV5htVrb29s5DwYA3GPwy+3QMWkv/fvUGo2iqFqtvvT+h319fQRBHHgPb4a7vuNIQ0PDe1eqDQZDS0tL/pP9L4vl0ui4CRJXAAAAAElFTkSuQmCC'
    file = open('snake.png', 'wb')
    file.write(b64decode(string))
    file.close()


def image_wall():
    """生成墙位图"""
    string = b'iVBORw0KGgoAAAANSUhEUgAAABsAAAAbCAIAAAACtmMCAAAAOklEQVRIDWO0sXdkoCpgoqppIMNGTaROkI6G42g4kh8Co6mH/LBD1jkajsihQT57NBzJDztknUMhHAFK/ADy7E6jZAAAAABJRU5ErkJggg=='
    file = open('wall.png', 'wb')
    file.write(b64decode(string))
    file.close()


def image_delete():
    """即时删除位图"""
    if path.exists('snake.png'):
        remove('snake.png')
    if path.exists('food.png'):
        remove('food.png')
    if path.exists('wall.png'):
        remove('wall.png')


if __name__ == "__main__":
    image_food()
    image_snake()
    image_wall()
    main()
