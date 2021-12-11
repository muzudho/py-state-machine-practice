import datetime


class KyotoBehavior():
    def __init__(self):
        pass

    def update(self, message):
        if message in ["TAKOYAKI", "YATSUHASHI", "AKASHIYAKI", "SHIKA_SENBEI", "MIKAN"]:
            # 食べ物に釣られます
            return "YATSUHASHI"
        else:
            return datetime.datetime.now().strftime('%H時%M分%S秒')
