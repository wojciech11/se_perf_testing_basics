import timeit
import time

def complex_func():
    print('start')
    time.sleep(2)
    print('end')

print(timeit.Timer(complex_func).timeit(number=3))
