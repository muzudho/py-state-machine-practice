import datetime


class KyotoBehavior:
    def create_message_v06(self, message):
        if message in ["TAKOYAKI", "YATSUHASHI", "AKASHIYAKI", "SHIKA_SENBEI", "MIKAN"]:
            # 食べ物に釣られます
            return "YATSUHASHI"
        else:
            return datetime.datetime.now().strftime("%H時%M分%S秒")
