class OsakaBehavior():
    def __init__(self):
        pass

    def react(self, message):
        if message in ["TAKOYAKI", "YATSUHASHI", "AKASHIYAKI", "SHIKA_SENBEI", "MIKAN"]:
            # 食べ物を止めます
            return "TSUTEN_KAKU"
        else:
            # 食べ物に入ります
            return "TAKOYAKI"
