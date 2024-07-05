import time

class MeasurerCodeTime:
    def __init__(self):
        pass

    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        executeTime = (self.end_time - self.start_time) * 1000
        print(f"Execute time: { executeTime } ms")
