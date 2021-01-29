import time

import unittest

def complex_fun():
    print("start")
    # przegląd bazy danych
    time.sleep(1)
    print("end")

class TestSimple(unittest.TestCase):

    def test_ile_trwa(self):
        t0 = time.time()
        complex_fun()
        t1 = time.time()
        total = t1-t0
        print(f'Test trwał: {total}')
