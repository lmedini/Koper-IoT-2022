import numpy as np


class Counter:
    c = 0
    x1 = 0  # remove some noise but not much
    current = 0
    v_max = 640  # max value

    def __init__(self):
        pass

    def normalize(self, num):
        if num > self.v_max * 0.5:
            return 0
        else:
            return 1

    def count(self, value):
        value = self.normalize(value)
        if value != self.current:  # different
            if value != self.x1:
                self.c += 1
                self.x1 = value
                return []
            else:
                # return the counter
                arr = [self.current, self.c]
                # print(arr)
                self.c = 0
                self.x1 = value
                self.current = value
                return arr
        else:
            self.c += 1
            self.x1 = value
            return []


class Detector:
    counter = None

    # first detector
    high_long_span = 17
    high_long_over = 40
    # second detector
    low_small_span = 8
    low_small_over = 24
    # third detector
    high_small_span = 3
    high_small_over = 20
    # fourth detector
    low_long_span = 40

    detected_steps = 0

    last4 = []

    def __init__(self):
        self.counter = Counter()
        pass

    def detect(self, value):
        res = self.counter.count(value)
        if len(res) > 1:
            if len(self.last4) < 4:
                self.last4.append(res)
                return False
            else:
                self.last4.pop(0)
                self.last4.append(res)
                # print(self.last4)
                if self.perform_detection():
                    return True
        return False

    def perform_detection(self):
        if self.last4[0][0] == 1 and self.high_long_span < self.last4[0][1] and self.last4[0][1] < self.high_long_over:
            if self.last4[1][0] == 0 and self.low_small_span < self.last4[1][1] and self.last4[1][1] < self.low_small_over:
                if self.last4[2][0] == 1 and self.high_small_span < self.last4[2][1] and self.last4[2][1] < self.high_small_over:
                    if self.last4[3][0] == 0 and self.low_long_span < self.last4[3][1]:
                        return True
