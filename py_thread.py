from threading import Thread
import  threading


cur_thread = threading.current_thread()
print(cur_thread, cur_thread.getName(), sep='\n')   # 获取的当前线程为主线程MainThread

new_thread = threading.Thread(name='liu')
print(new_thread, new_thread.getName(), sep='\n')   # 创建一个新线程,默认名为Thread-n,命名为liu















