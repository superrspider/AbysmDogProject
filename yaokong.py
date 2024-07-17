# L1=B4,L2=B6
import threading
import time

from LinuxRobot.main import controller

if controller.buttons[4].value == True:#前进
    print('L1')
    time.sleep(delay_time)


event_right0=threading.Event() #false
event_left0=threading.Event() #false
event_back=threading.Event() #false

def thread_right0():
    global t
    while 1:
        event_right0.wait()
        #right代码

def thread_left0():
    global t
    while 1:
        event_left0.wait()
        # left代码

def thread_back():
    global t
    while 1:
        event_back.wait()
        # back代码

t_right0 = threading.Thread(target=thread_right0,daemon=True)
t_left0 = threading.Thread(target=thread_left0,daemon=True)
t_back = threading.Thread(target=thread_back,daemon=True)

t_right0.start()
t_left0.start()
t_back.start()


stop_thread(t_right0)
stop_thread(t_left0)
stop_thread(t_back)