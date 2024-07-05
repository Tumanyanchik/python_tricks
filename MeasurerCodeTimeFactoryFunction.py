import time
from contextlib import contextmanager

@contextmanager
def measure_code_time() -> None:
    try:
        start_time = time.time()
        yield
    finally:
        end_time = time.time()
        execute_time = (end_time - start_time) * 1000
        print(f"Execute time: {execute_time} ms")
