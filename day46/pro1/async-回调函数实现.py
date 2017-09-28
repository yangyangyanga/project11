import time
import threading

def longIo(callback):
    def run(cb):
        print("开始处理耗时操作")
        time.sleep(5)
        print("结束处理耗时操作")
        # 调用回调函数
        cb("sunck is a good man")
    threading.Thread(target=run, args=(callback,)).start()

# 回调函数
def finish(res):
    print("开始处理回调函数")
    print("接收到返回的数据：", res)
    print("结束处理回调函数")

def reqA():
    print("开始处理请求A")
    res = longIo(finish)
    print("接收到返回的数据", res)
    print("结束处理请求A")


def reqB():
    print("开始处理请求B")
    print("结束处理请求B")

def main():
    reqA()
    reqB()
    while 1:
        pass

if __name__ == "__main__":
    main()