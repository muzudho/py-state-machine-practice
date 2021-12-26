import datetime


class KyotoBehavior:
    def print(self):
        text = datetime.datetime.now().strftime("%H時%M分%S秒")
        print(text)
