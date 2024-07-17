from selectors import EVENT_WRITE
from lib1 import *
res = None
import time

a = [0, 0, 0, 0]
begin = b'\xFF\xFF'
end = b'\xFE'
global LL
value1 = 0.0
time.sleep(1.5)

import os, struct
#函数库路径导入
import threading
import time
# 线程功能操作库
import inspect
import ctypes
import serial
import os
from lib1 import *
import math as cm
import struct
import numpy
from math import sin, cos, pi, sqrt, asin, acos


# 足端运动曲线参数
pi = 3.1415926;
height = 300  # height为足端初始高度  #height
x1 = 0;
x2 = 0;
x3 = 0;
x4 = 0;
Y1 = 0;
y2 = 0;
y3 = 0;
y4 = 0;
r1 = 1;
r2 = 1;
r3 = 1;
r4 = 1;
faai = 0.5;
Ts = 3;  # faai=0.7;有点问题-》0.5
# faai：支撑相占空比；Ts：周期（支撑相占空比可以理解为一个运动周期内足端触地时间和一个周期的比例，若faai为0.5则表示一周期内足端有一半时间触地）
xf = 0
xs = -40
h = 70  # xf：曲线终点； xs：曲线起点；h：与初始高度之间的差值（单位：毫米。当前参数较小仅用于前期测试，之后可调大参数即调大步幅）
# sita1_1 = 0;
# sita2_1 = 0;  # 初始摆角θ1，θ2的角度
l1 = 166;
l2 = 332;  # l1和l2是腿长，已经修改为我们的四足机器人的参数（单位：毫米）
t = 1;

aa=0;
sita1_1=[13.0,-0.70,17.5,45]
sita2_1=[-0.70,13.0,45,11.4]
sita1_2=[17.5,45,13.0,-0.7]
sita2_2=[45,11.5,-0.7,13]
Sita2_2=[0,45,0,45]

def stand(i,j):
    set_angle(id_num=i, angle=0, speed=50, limit_cur=23)
    set_angle(id_num=j, angle=0, speed=50, limit_cur=23)

def thread1():
    global t
    global aa
    global sita1_1, sita2_1, Y1,x1  # sita1_1是腿1的1号电机转角（弧度制），sita2_1是腿1的2号电机转角，以此类推。
    global sita1_2, sita2_2, y2,x2
    global sita1_3, sita2_3, y3
    global sita1_4, sita2_4, y4
    
    while True:
        if aa==1:   #forward

            t = t+1  # 步频调节，参数越大步频越快
            if t >= Ts+1:
                t = 0
            forspeed=100
              #腿1
            set_angle(id_num=6, angle=sita2_1[t]+25, speed=forspeed, limit_cur=23)
            set_angle(id_num=4, angle=sita1_1[t]+25, speed=forspeed, limit_cur=23)

             #腿3
            set_angle(id_num=9, angle=sita1_1[t]*1.2+20, speed=forspeed, limit_cur=23)
            set_angle(id_num=8, angle=sita2_1[t]*1.2+20, speed=forspeed, limit_cur=23)

            #腿2
            set_angle(id_num=3, angle=-sita1_2[t]-20, speed=forspeed, limit_cur=23)
            set_angle(id_num=2, angle=-sita2_2[t]-20, speed=forspeed, limit_cur=23)

           

            set_angle(id_num=7, angle=-sita2_2[t]-25, speed=forspeed, limit_cur=20)
            set_angle(id_num=5, angle=-sita1_2[t]-25, speed=forspeed, limit_cur=20)
            
            time.sleep(0.05)
        elif aa==2:#back
        
            t = t+1  # 步频调节，参数越大步频越快
            if t >= Ts+1:
                t = 0

            #腿1
            set_angle(id_num=4, angle=sita2_1[t]+25, speed=100, limit_cur=23)
            set_angle(id_num=6, angle=sita1_1[t]+25, speed=100, limit_cur=23)
            #腿3
            set_angle(id_num=8, angle=sita1_1[t]+20, speed=100, limit_cur=23)
            set_angle(id_num=9, angle=sita2_1[t]+20, speed=100, limit_cur=23)

            #腿2
            set_angle(id_num=2, angle=-sita1_2[t]*1.2-20, speed=100, limit_cur=23)
            set_angle(id_num=3, angle=-sita2_2[t]*1.2-20, speed=100, limit_cur=23)


            set_angle(id_num=5, angle=-sita2_2[t]-25, speed=100, limit_cur=23)
            set_angle(id_num=7, angle=-sita1_2[t]-25, speed=100, limit_cur=23)
            time.sleep(0.05)
        elif aa==3:#left
            t = t+1  # 步频调节，参数越大步频越快
            if t >= Ts+1:
                t = 0

                    #腿1
            set_angle(id_num=6, angle=sita2_1[t]+20, speed=180, limit_cur=23)
            set_angle(id_num=4, angle=sita1_1[t]+20, speed=180, limit_cur=23)
                        #腿3
            set_angle(id_num=9, angle=sita2_1[t]+20, speed=80, limit_cur=23)
            set_angle(id_num=8, angle=sita1_1[t]+20, speed=80, limit_cur=23)
            #腿2
            set_angle(id_num=2, angle=-sita1_2[t]-20, speed=80, limit_cur=23)
            set_angle(id_num=3, angle=-sita2_2[t]-20, speed=80, limit_cur=23)

            set_angle(id_num=7, angle=-sita2_2[t]-20, speed=80, limit_cur=23)
            set_angle(id_num=5, angle=-sita1_2[t]-20, speed=80, limit_cur=23)
            time.sleep(0.05)
        elif aa==4:#right
            t = t+1  # 步频调节，参数越大步频越快
            if t >= Ts+1:
                t = 0
            
            set_angle(id_num=6, angle=sita1_1[t]+20, speed=180, limit_cur=23)
            set_angle(id_num=4, angle=sita2_1[t]+20, speed=180, limit_cur=23)
                        #腿3
            set_angle(id_num=9, angle=sita1_1[t]+20, speed=80, limit_cur=23)
            set_angle(id_num=8, angle=sita2_1[t]+20, speed=80, limit_cur=23)
            #腿2
            set_angle(id_num=2, angle=-sita2_2[t]-20, speed=80, limit_cur=23)
            set_angle(id_num=3, angle=-sita1_2[t]-20, speed=80, limit_cur=23)

            set_angle(id_num=7, angle=-sita1_2[t]-20, speed=80, limit_cur=23)
            set_angle(id_num=5, angle=-sita2_2[t]-20, speed=80, limit_cur=23)
            time.sleep(0.05)
        elif aa==6:
            set_angle(id_num=2, angle=-45, speed=80, limit_cur=23)
            set_angle(id_num=3, angle=-45, speed=80, limit_cur=23)
            set_angle(id_num=4, angle=45, speed=80, limit_cur=23)
            set_angle(id_num=5, angle=-45, speed=80, limit_cur=23)
            set_angle(id_num=6, angle=45, speed=80, limit_cur=23)
            set_angle(id_num=7, angle=-45, speed=80, limit_cur=23)
            set_angle(id_num=9, angle=45, speed=80, limit_cur=23)
            set_angle(id_num=8, angle=45, speed=80, limit_cur=23)


t_back = threading.Thread(target=thread1,daemon=True)

t_back.start()

class JoyStick:
    def __init__(self):  # 初始化
        print('avaliable devices')
        for fn in os.listdir('/dev/input'):
            if fn.startswith('js'):
                print('/dev/input/%s' % fn)  #找到js0

        self.fn = '/dev/input/js0'
        self.x_axis = 0;

    def open(self):
        self.jsdev = open(self.fn, 'rb')

    def read(self):
        self.evbuf = self.jsdev.read(8)
        return struct.unpack('IhBB', self.evbuf)
    def type(self, type_):
        if type_ & 0x01:
            return "button";
        if type_ & 0x02:
            return "axis";
    def button_state(self):
        return 1;

    def get_x_axis(self):
        time, value, type_, number = struct.unpack('IhBB', self.evbuf)
        if number == 1:
            fvalue = value / 32767
            return fvalue;

js = JoyStick()

def joystick_thread(num, model, sudo, ki):
    global aa
    global t
    global event_trot
    global event_right0
    global event_left0
    global event_back
    js.open()
    while True:
        time, value, type_, number = js.read()
        if js.type(type_) == "button":
            print("button:{} state: {}".format(number, value))
            if number == 4 and value == 1:                      #Y   forward
                model = 1
                aa=1
             

            if number == 0 and value == 1:                     #A   event_back
                ki += 0.00001
                print("KI+", ki)
                aa=2
              
  
            if number == 3 and value == 1:                      #X   event_left0
                num += 0.00001
                print("KD+", num)
                aa=3
               

            if number == 1 and value == 1:                     #B  event_right0
                if num > 0:
                    num -= 0.00001
                    print("KD-", num)
                aa=4
                

            if number ==10 and value ==1:     
                aa=0                  #select   zero
                print('select')
                set_zero(2,3)
                set_zero(4,5)
                set_zero(6,7)
                set_zero(8,9)
                print('22')
                
            if number ==11 and value ==1:                       #start 
                print('star')

            if number == 6 and value == 1:                    #L1    
                aa=0
                sudo += 0.001 
                print("KP+", sudo)
                motor_estop(id_num=2)
                motor_estop(id_num=3)

                motor_estop(id_num=5)
                motor_estop(id_num=4)

                motor_estop(id_num=6)
                motor_estop(id_num=7)

                motor_estop(id_num=9)
                motor_estop(id_num=8)
            if number == 8 and value == 1:                     #L2  break!!
                aa=0
                model = 2
                print("break")

            if number == 7 and value == 1:                    #R1  stand
                aa=6
            if number ==9 and value ==1:                       #R2
                print('R2')

            if model == 2:
                break


if __name__ == "__main__":
    num = 0.00145  # KD
    model = 0  # moshi
    sudo = 0.021  # KP
    ki = 0.000000  # KI
    joystick_thread(num, model, sudo, ki)
