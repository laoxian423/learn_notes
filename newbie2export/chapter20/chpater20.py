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

""" 等待线程结束
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

"""线程停止
"""

# 线程停止变量
isrunning = True

# 线程体函数
def thread_stop_body():
    while isrunning:
        # 线程开始工作
        print('下载中...')
        time.sleep(5)
    print('执行完成')
# 主函数
def main_stop_thread():
    # 创建线程1
    t1 = threading.Thread(target=thread_stop_body)
    t1.start()
    command = input('please stop:')
    if command == 'exit':
        global isrunning
        isrunning = False
    print('主进程结束')

"""线程安全
        临界资源问题
"""
class TicketDB:
    def __init__(self):
        # 机票的数量
        self.ticket_count = 5
    
    # 获取当前机票数量
    def get_ticket_cout(self):
        return self.ticket_count
    
    # 销售机票
    def sell_ticket(self):
        # 线程休眠，阻塞当前线程，模拟等待用户付款
        time.sleep(2)
        print("第 {0} 号票，已经售出".format(self.ticket_count))
        self.ticket_count -= 1

db = TicketDB()

# 线程体1函数
def thread1_body():
    global db
    while True:
        curr_ticket_count = db.get_ticket_cout()
        if curr_ticket_count > 0 :
            db.sell_ticket()
        else:
            # 无票退出
            break

def thread2_body():
    global db
    while True:
        curr_ticket_count = db.get_ticket_cout()
        if curr_ticket_count > 0 :
            db.sell_ticket()
        else:
            # 无票退出
            break

def main_ticket():
    # 创建线程对象t1
    t1 = threading.Thread(target=thread1_body)
    t1.start()
    t2 = threading.Thread(target=thread2_body)
    t2.start()


""" 多线程同步
    互斥锁： 为防止访问临界资源导致数据不一致，为资源对象加上互斥锁，任意时刻只有一个线程访问。
            线程同步客观上会导致性能下降。
    threading.Lock:
    Lock.acquire() 锁定
    Lock.release() 解锁
"""

# 创建TicketDB对象(上面已创建)

# 创建Lock对象
lock = threading.Lock()

# 线程体1函数
def thread1_lock():
    global db, lock
    while True:
        lock.acquire()  # 加锁
        curr_ticket_count = db.get_ticket_cout()
        if curr_ticket_count > 0 :
            db.sell_ticket()
        else:
            lock.release()
            # 无票退出
            break
        lock.release()
        time.sleep(1)

def thread2_lock():
    global db, lock
    while True:
        lock.acquire()
        curr_ticket_count = db.get_ticket_cout()
        if curr_ticket_count > 0 :
            db.sell_ticket()
        else:
            lock.release()
            # 无票退出
            break
        lock.release()
        time.sleep(1)

def main_ticket_lock():
    # 创建线程对象t1
    t1 = threading.Thread(target=thread1_lock)
    t1.start()
    t2 = threading.Thread(target=thread2_lock)
    t2.start()

""" 线程间通信
    线程间通信可以使用threading中的Condition类和 Event类
"""

""" Condition 条件变量
    .acquire()
    .release()
    .wiat(timeout=None):当前线程释放锁，然后处于阻塞状态，等待唤醒，timeout超时时间
    .notify(): 唤醒其他线程
    .notify_all(): 唤醒所有线程
    一个经典的线程间通信是”堆栈“数据结构，一个线程生成数据，将数据压栈，另一个消费数据，
    将数据出栈，当堆栈为空时消费线程通知生产线程生产数据，当堆栈已满，生产线程通知消费
    线程消费数据
"""
import random
# 创建条件变量对象
condition = threading.Condition()

class Stack():
    def __init__(self):
        # 堆栈指针初始值为0
        self.pointer = 0
        # 堆栈有5个数字的空间
        self.data = [-1, -1, -1, -1, -1]
    
    #压栈
    def push(self, c):
        global condition
        condition.acquire()
        # 堆栈已满，不能压栈
        while self.pointer == len(self.data):
            # 等待其他线程把数据出栈（我睡一会，没数据了喊我）
            print('wait...')
            condition.wait()
        # 通知其他线程把数据出栈
        condition.notify()
        # 数据压栈
        self.data[self.pointer] = c
        # 指针向上移动
        self.pointer += 1
        condition.release()
    #出栈
    def pop(self):
        global condition
        condition.acquire()
        # 堆栈无数据，不能出栈
        while self.pointer == 0 :
            # 等待其他进程把数据压栈
            condition.wait()
        # 通知其他线程压栈
        condition.notify()
        # 指针下移
        self.pointer -= 1
        data = self.data[self.pointer]
        condition.release()
        # 数据出栈
        return data

# 创建堆栈对象
stack = Stack()

# 生产者线程体函数
def producer_thread_body():
    global stack
    # 产生10个数字
    for i in range(0, 10):
        # 把数字压栈
        stack.push(i)
        print('生产:{0}'.format(i))
        # 每生产1个数字，线程就休眠
        time.sleep(1)
    
# 消费者线程体函数
def consumer_thread_body():
    global stack
    # 从堆栈中取数字
    for i in range(0, 10):
        x = stack.pop()
        print('消费：{0}'.format(x))
        # 每消费一个数字，线程就睡眠
        time.sleep(1)

# 主函数
def condition_main():
    # 创建生产者线程对象
    producer = threading.Thread(target=producer_thread_body)
    producer.start()
    consumer = threading.Thread(target=consumer_thread_body)
    consumer.start()

""" 使用 Event 实现线程间通信
    使用Condition较为繁琐，threading提供Event类来实现线程通讯
    Event对象调用wait()阻塞当前线程，直到另一个线程调用该Event对象的set()方法
    通知所有等待状态的线程恢复运行。
"""
event = threading.Event()

class Stack1():
    def __init__(self):
        # 堆栈指针初始值为0
        self.pointer = 0
        # 堆栈有5个数字的空间
        self.data = [-1, -1, -1, -1, -1]
    
    #压栈
    def push(self, c):
        global event
        # 堆栈已满，不能压栈
        while self.pointer == len(self.data):
            # 等待其他线程把数据出栈（我睡一会，没数据了喊我）
            print('wait...')
            event.wait()
        # 通知其他线程把数据出栈
        event.set()
        # 数据压栈
        self.data[self.pointer] = c
        # 指针向上移动
        self.pointer += 1
    #出栈
    def pop(self):
        global event
        # 堆栈无数据，不能出栈
        while self.pointer == 0 :
            # 等待其他进程把数据压栈
            event.wait()
        # 通知其他线程压栈
        event.set()
        # 指针下移
        self.pointer -= 1
        data = self.data[self.pointer]
        # 数据出栈
        return data

# 创建堆栈对象
stack = Stack1()

# 生产者线程体函数
def producer_thread_body_event():
    global stack
    # 产生10个数字
    for i in range(0, 10):
        # 把数字压栈
        stack.push(i)
        print('生产:{0}'.format(i))
        # 每生产1个数字，线程就休眠
        time.sleep(1)
    
# 消费者线程体函数
def consumer_thread_body_event():
    global stack
    # 从堆栈中取数字
    for i in range(0, 10):
        x = stack.pop()
        print('消费：{0}'.format(x))
        # 每消费一个数字，线程就睡眠
        time.sleep(1)
# 主函数
def event_main():
    # 创建生产者线程对象
    producer = threading.Thread(target=producer_thread_body_event)
    producer.start()
    consumer = threading.Thread(target=consumer_thread_body_event)
    consumer.start()

if __name__ == "__main__":
    event_main()


