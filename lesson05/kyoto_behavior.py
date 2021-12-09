import datetime


class KyotoBehavior():
    def __init__(self):
        pass

    def print(self):
        text = datetime.datetime.now().strftime('%H時%M分%S秒')
        print(text)
