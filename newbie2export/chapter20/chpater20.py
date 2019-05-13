# LOOK 多线程
""" python 多线程编程
    threading 模块：
    threading.active_count():放回当前处于活动状态的线程个数
    threading.current_thread():放回当前的Tread对象
    threading.main_thread():返回主线程对象。
"""
import threading

def base_threading():
    # 当前线程对象
    t = threading.current_thread()
    print(t.name)

    # 返回活动状态的线程个数
    print(threading.active_count())

    # 当前线程对象
    t = threading.main_thread()
    print(t.name)

""" 创建线程
    两个要素:
        线程对象（Thread）
        线程体（线程执行函数):
            自定义函数
                threading.Thread(target=None, name=None, args=())
                target 线程体
                name 设置线程名，省略解释器会分配一个
                args 为自定义函数提供参数，一个元组
            继承Thread重写run()方法。
    time.sleep():
        让当前线程暂停执行，然后由其他线程来争夺执行的机会。
"""
import time

def thread_body():
    # 当前线程对象
    t = threading.current_thread()
    for n in range(5):
        print('第 {0} 次执行线程 {1}'.format(n, t.name))
        # 线程休眠,如果不sleep(),那么当前线程执行完，别的线程才有机会
        # sleep(秒数)，可以是小数，如 0.1 代表100毫秒
        time.sleep(0.1)
    print('线程{0}执行完成！'.format(t.name))

def main():
    # 创建线程对象 t1
    t1 = threading.Thread(target=thread_body, name='T1')
    # 启动线程
    t1.start()

    # 创建线程对象 t2
    t2 = threading.Thread(target=thread_body, name='T2')
    t2.start()

""" 继承Thread线程类实现线程体
    重写run()
"""
class MyThread(threading.Thread):
    def __init__(self, name=None):
        super().__init__(name=name)

    # 线程体函数
    def run(self):
        # 当前线程对象
        t = threading.current_thread()
        for n in range(5):
            # 当前线程名
            print('第 {0} 次执行线程{1}'.format(n, t.name))
            # 线程休眠
            time.sleep(0.1)
        print('线程 {0}执行完成'.format(t.name))

def run_main():
    # 创建线程 t1
    t1 = MyThread()
    t1.start()

    t2 = MyThread(name='MyThread')
    t2.start()
    
""" 线程管理
    线程创建、线程启动、线程休眠、等待线程结束和线程停止
    使用join()的场景是，一个线程依赖于另外一个线程的运行结果，所以
    调用另一个线程的join()方法等他运行完成。
"""
# 共享变量

value = 0

def thread_body1():
    global value
    # 当前线程对象
    print('ThreadA  start....')
    for n in range(2):
        print('ThreadA 执行...')
        value +=1 
        # 线程休眠
        time.sleep(1)
    print('ThreadA end....')

def main1():
    print('主线程开始....')
    # 创建线程对象
    t1 = threading.Thread(target=thread_body1, name='ThreadA')
    t1.start()
    # 主线程被阻塞，等待t1 线程结束
    t1.join()
    print('value = {0}'.format(value))
    print('主线程结束....')






if __name__ == "__main__":
    main1()


