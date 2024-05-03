import random #引入随机模块
import sys #系统模块，该模块提供一些接口，用于访问python解释器自身使用和维护的变量
import time #时间模块
import pygame #pygame 模块
from pygame.locals import *#将所有的PYgame常量导入，类似我们C语言中的include<stdio.h>
from collections import deque #deque（双向队列）类似list的容器，可以快速在队列头部和尾部添加,删除元素
#clloections 模块，python标准库，数据结构常用模块，collections包含一些特殊的容器，针对python的list，dict，set等，提供另一种选择

#------------------------------------------------------------------------------------------------------#
#以上导入模块完成，接下来先设置一些基础属性
# 基础设置
Screen_Height=480  #定义屏幕高度
Screen_Width=600   #定义屏幕宽度
Size=20 #方格大小
Line_Width=1
#游戏区域坐标范围 ，整个范围啊，x,y轴的大小
Area_x=(0,Screen_Width//Size-1)#0是左边界，1是右边界 #注：python中//为整数除法；/为浮点数除法
Area_y=(2,Screen_Height//Size-1)
#对食物的一些基础属性进行设置
Food_Style_List=[(10,(135,206,235)),(20,(255,215,0)),(30,(200,30,30))]
                       #蓝色              #金色            #红色
#对于整体的颜色设置，先写出变量，方便使用
Dark = (200, 200, 200)
Black = (0, 0, 0)
Red = (200, 30, 30)
Back_Ground = (0, 0, 0)
White=(255,255,255)
#-----------------------------------------------------------------------------------
#以上是基础设置，接下来对贪吃蛇的创造
#文本输出格式设置
def Print_Txt(screen, font, x, y, text, fcolor=(255, 255, 255)):#就是显示窗口那d打印文本，显示文字的
              #窗口，#在pygame中，font 对象用于文本的渲染， # x轴位置，y轴位置，#text，代表要打印的文本内容，#颜色
    # font.render参数意义：.render（内容，是否抗锯齿，字体颜色，字体背景颜色）
    Text =font.render(text, True, fcolor)#这一步负责将文本渲染（或转换）成一个 pygame.Surface 对象
    screen.blit(Text, (x, y))#这一步是将渲染好的文本放在窗口上
#这种方法是游戏开发和图形编程中非常常见的，因为它允许开发者在窗口或屏幕上的任意位置绘制图像或文本。在 pygame 中，你通常会在游戏循环中多次调用 blit 方法来更新屏幕上的内容

#初始化贪吃蛇
def init_snake():
    snake = deque()#前边导入的deque（）函数，是个双向队列
    snake.append((2, Area_y[0]))#设置出现的位置
    snake.append((1, Area_y[0]))#设置蛇出现的位置
    snake.append((0, Area_y[0]))#x,y位置
    return snake


#对食物进行创造
#把蛇放进去是要判断与保证食物不会出现在蛇身上
def Creat_Food(snake):
    food_x = random.randint(Area_x[0], Area_x[1])  #设置食物出现的X轴位置
    food_y = random.randint(Area_y[0], Area_y[1])  #设置食物出现的Y轴位置
    #如果食物出现在蛇身上，重新生成食物
    while (food_x, food_y) in snake:
        food_x = random.randint(Area_x[0], Area_x[1])   # 设置食物出现的X轴位置
        food_y = random.randint(Area_x[0], Area_y[1]) # 设置食物出现的Y轴位置
    return food_x, food_y#返回食物位置


#写食物风格函数咯
def Food_Style():
    return Food_Style_List[random.randint(0, 2)]  #返回我之前设置的食物风格的随机值

#---------------------------------------------------------------------#
#主函数
def main():
    pygame.init()  #初始化Pygame库，调用pygame的各种功能之前，先调用这个函数，确保pyganme正常运行
    screen = pygame.display.set_mode((Screen_Width, Screen_Height))  #创造显示的窗口
    # display.set_mode是pygame模块中的函数
    # 模板为pygame.display.set_mode((宽度, 高度), 可选参数，用于指定窗口的特性)
    pygame.display.set_caption('覃崇飞的贪吃蛇物语果然有问题')  # 窗口名字
    # 得分字体设置
    font1 = pygame.font.SysFont('SimHei', 24)#“SimHei”字体（通常用于显示中文），字体大小为24点
    # GO字体设置
    font2 = pygame.font.SysFont(None, 72)#“None”，意味着pygame会尝试使用系统的默认字体
    fwidth, fheight = font2.size('GAME OVER')  #使用size方法来获取渲染该文本所需的宽度和高度。
    # 程序bug修复：如果蛇在向右移动，快速点击分别施加向下、向左的命令，向下的命令会被覆盖，只有向左的命令被接受，直接GameOver
    # b变量为了防止这个情况发生
    b = True
    #在主函数中创造蛇出来
    snake = init_snake()
    #在主函数中创造食物出来
    food = Creat_Food(snake)
    food_style = Food_Style()
    #设置方向控制
    pos = (1, 0) #通常表示一个坐标点。这个坐标点由两个数值组成：第一个数值（这里是1）通常代表水平方向（x轴）的位置，而第二个数值（这里是0）代表垂直方向（y轴）的位置。

    #初始化一些启动游戏的相关变量，例如开始啊，结束什么的

    game_over = True  # 结束标志 # 是否开始，当start = True，game_over = True 时，才显示 GAME OVER
    game_start = False  # 开始标志
    score = 0  # 得分
    orispeed = 0.3  #蛇的初速度，数字越大越慢
    speed = orispeed  # 蛇速度
    last_move_time = None
    pause = False  # 暂停
    while True:#让窗口存在
        # pygame.event.get()是pygame库中的一个函数，用于从事件队列中获取所有待处理的时间
        # 当你调用 pygame.event.get() 时，它会返回一个事件列表，这个列表包含了从上次调用 pygame.event.get() 或 pygame.event.pump() 以来发生的所有事件。
        for event in pygame.event.get():#处理得到的事件
            if event.type == QUIT:## 检查当前事件是否是窗口关闭事件
                sys.exit()#退出python窗口
            elif event.type == KEYDOWN:#KEYDOWN,pygame里的一个常量，用于表示一个键盘被按下的事件
                if event.key == K_RETURN:#K_RETURN pygame中的一个常量，它代表回车
                    if game_over:
                        # 初始化
                        game_start = True
                        game_over = False
                        b = True
                        snake = init_snake()
                        food = Creat_Food(snake)
                        food_style = Food_Style()
                        pos = (1, 0)
                        # 得分
                        score = 0
                        last_move_time = time.time()
                        # 初始化以上↑
                elif event.key == K_SPACE:
                    if not game_over:
                        pause = not pause
                # 以下为防止蛇在向右移动时按向左键，导致GameOver
                elif event.key in (K_UP, K_w):
                    if b and not pos[1]:  ###
                        pos = (0, -1)
                        b = False
                elif event.key in (K_DOWN, K_s):
                    if b and not pos[1]:
                        pos = (0, 1)
                        b = False
                elif event.key in (K_LEFT, K_a):
                    if b and not pos[0]:
                        pos = (-1, 0)
                        b = False
                elif event.key in (K_RIGHT, K_d):
                    if b and not pos[0]:
                        pos = (1, 0)
                        b = False
        # 填充背景色
        screen.fill(Black)
        # 蛇的爬行过程
        if not game_over:
            curTime = time.time() #curTime储存获取当前时间
            # 通常，这种代码用于游戏中的时间管理或性能分析，例如计算游戏循环的帧率（FPS）或检测两个事件之间的时间间隔。
            if curTime - last_move_time > speed:  # 设置帧率
                if not pause:
                    b = True
                    last_move_time = curTime
                    next_s = (snake[0][0] + pos[0], snake[0][1] + pos[1])#下一步，如何操作
                    # 如果吃到了食物
                    if next_s == food:
                        snake.appendleft(next_s)# 头部加一个
                        score += food_style[0]
                        speed = orispeed - 0.03 * (score // 100)# 分数超过一百，就提速度
                        food = Creat_Food(snake)
                        food_style = Food_Style()
                    else:
                        # 在区域内，没迟到食物，但是在移动
                        if Area_x[0] <= next_s[0] <= Area_x[1] and Area_y[0] <= next_s[1] <= Area_y[1] and next_s not in snake:#这里就是判断贪吃蛇碰不碰到边界，以及碰不碰到自身
                            snake.appendleft(next_s)#之前添加的deque的功能，能在队列左侧增加，删除
                            snake.pop()# 删一个贪吃蛇的尾部
                        else:
                            game_over = True #游戏结束
        # 画食物
        if not game_over:
            '''
            good
            '''

        # 避免 GAME OVER 的时候把 GAME OVER 的字给遮住了
        pygame.draw.rect(screen, food_style[1], (food[0] * Size, food[1] * Size, Size, Size), 0)
        # 画蛇
        for s in snake:
            #pygame.draw.rect 是 Pygame 库中的一个函数，用于在 Surface 对象上绘制一个矩形
            pygame.draw.rect(screen, White, (s[0] * 20 + Line_Width, s[1] * Size + Line_Width,  Size - Line_Width * 2, Size - Line_Width * 2), 0)
        Print_Txt(screen, font1, 15, 7, f'牢大速度: {score // 100}')
        Print_Txt(screen,font1,200,7,"牢大的贪吃蛇游戏")
        Print_Txt(screen, font1, 450, 7, f'牢大得分: {score}')
        # 画GameOver
        if game_over:
            if game_start:
                # print('GameOver')
                Print_Txt(screen, font2, (Screen_Width - fwidth) // 2, (Screen_Height - fheight) // 2, 'GAME OVER', Red)#这里是让game over 能够居中输出
        pygame.display.update()#这行代码更新pygame的显示屏幕，使game，over文本立即显示，保证能显示

#在Python中，if __name__ == '__main__': 是一个常见的模式，用于检查当前脚本是否作为主程序运行，而不是作为模块导入到另一个脚本中。
if __name__ == '__main__': #如果一个py文件正常运行，那么__name__的值就会为__main__
    main()
