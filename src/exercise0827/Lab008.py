import time


def time_dec(fun):
    def wrapper():
        start_time = time.time()
        print(start_time)
        fun()
        end_time = time.time()
        print(f"time taken by function{end_time - start_time}")
    return wrapper()


@time_dec
def test():
    print("time")
    time.sleep(1)
