import time

class Dataset:
    def __init__(self):
        self.data = None

    def load_data(self):
        time.sleep(1000)
        self.data = 'slow data'

