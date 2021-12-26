class NaraBehavior:
    def create_message_v06(self, message):
        if message in ["TAKOYAKI", "YATSUHASHI", "AKASHIYAKI", "SHIKA_SENBEI", "MIKAN"]:
            # 食べ物に釣られます
            return "SHIKA_SENBEI"
        else:
            return "DEER"
