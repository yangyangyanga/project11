import time
import threading

def longIo():
    print("开始处理耗时操作")
    time.sleep(5)
    print("结束处理耗时操作, 并唤醒请求A")
    yield "sunck is a cool man"

def genCorotine(f):
    def inner(*args, **kwargs):
        # reqA的生成器
        gen = f()
        # longIo的生成器
        g1 = next(gen)
        def run(g):
            # 执行longIOLoop，并在下面的子线程挂起
            res = next(g)
            try:
                gen.send(res)
            except StopIteration as e:
                pass
        threading.Thread(target=run, args=(g1,)).start()
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