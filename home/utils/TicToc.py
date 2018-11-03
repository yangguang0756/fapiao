import time


class Timer(object):
    def __init__(self):
        self.total_time = 0.
        self.calls = 0
        self.start_time = 0.
        self.diff = 0.
        self.average_time = 0.
        # 一共多少段时间
        self.times = {}

    def tic(self):
        self.start_time = time.time()

    def toc(self, average=True, content=""):
        self.diff = round(time.time() - self.start_time, 2)
        self.times[content] = self.diff

        self.total_time += self.diff
        self.calls += 1
        self.average_time = self.total_time / self.calls
        if average:
            return self.average_time
        else:
            return self.diff

    def __repr__(self):
        str = "【"
        for key, value in self.times:
            str += key + "耗时：" + value + "s<br>"

        str += "总耗时：" + str(self.total_time) + "s】"
