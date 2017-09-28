import time

def longIo():
    print("开始处理耗时操作")
    time.sleep(5)
    print("结束处理耗时操作")
    return "sunck is a good man"

def reqA():
    print("开始处理请求A")
    res = longIo()
    print("接收到返回的数据", res)
    print("结束处理请求A")


def reqB():
    print("开始处理请求B")
    print("结束处理请求B")

def main():
    reqA()
    reqB()

if __name__ == "__main__":
    main()