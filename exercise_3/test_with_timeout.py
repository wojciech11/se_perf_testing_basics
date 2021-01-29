import time
import pytest
import unittest

def complex_func():
    print("start")
    # przegląd bazy danych
    time.sleep(4)
    print("end")

class TestSimple(unittest.TestCase):

    @pytest.mark.timeout(1)
    def test_ile_trwa(self):
        t0 = time.time()
        complex_func()
        t1 = time.time()
        total = t1-t0
        print(f'Test trwał: {total}')
