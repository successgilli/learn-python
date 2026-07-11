import time
import pytest

@pytest.fixture(autouse=True)
def log_time_per_func():
    start = time.time()

    yield

    print('\n {:0.3} seconds'.format(time.time() - start))

@pytest.fixture(autouse=True, scope='session')
def log_time():
    yield

    print('\n ------ Completed at ------ \n {} \n'.
    format(time.strftime('%b %d %H', time.localtime(time.time()))))
    print('------------------------')

def test_1():
    time.sleep(1)


def test_2():
    time.sleep(1.23)
