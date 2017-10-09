import time
import threading

# 全局的生成器
gen = None

def longIo():
    def run():
        print("开始处理耗时操作")
        time.sleep(5)
        print("结束处理耗时操作, 并唤醒请求A")
        try:
            gen.send("sunck is a handsome man")
        except StopIteration as e:
            pass

    threading.Thread(target=run,).start()

def genCorotine(f):
    def inner(*args, **kwargs):
        global gen
        gen = f()
        next(gen)
    return inner

@genCorotine
def reqA():
    print("开始处理请求A")
    res = yield longIo()
    print("接收到返回的数据", res)
    print("结束处理请求A")


def reqB():
    print("开始处理请求B")
    time.sleep(2)
    print("结束处理请求B")

def main():
    reqA()
    reqB()
    while 1:
        pass

if __name__ == "__main__":
    main()