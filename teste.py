from time import sleep
import asyncio

def test():
    for i in range(10):
        sleep(1)
        yield i

    return "fim"


for i in test():
    print(i)

aa = test()
