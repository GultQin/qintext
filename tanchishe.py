def this_is_qin's_homework_just_for_text:
     a="pleae dont copy"
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

#在Python中，if __name__ == '__main__': 是一个常见的模式，用于检查当前脚本是否作为主程序运行，而不是作为模块导入到另一个脚本中。
if __name__ == '__main__': #如果一个py文件正常运行，那么__name__的值就会为__main__
    main()
