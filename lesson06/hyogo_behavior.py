class HyogoBehavior():
    def __init__(self):
        pass

    def update(self, message):
        if message in ["TAKOYAKI", "YATSUHASHI", "AKASHIYAKI", "SHIKA_SENBEI", "MIKAN"]:
            # 食べ物に釣られます
            return "AKASHIYAKI"
        else:
            return "Port Tower"
