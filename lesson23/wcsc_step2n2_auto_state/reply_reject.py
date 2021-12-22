from lesson18_data.step1n2_auto_const.pen_const import E_REJECT

class ReplyRejectState():
    def update(self, req):

        self.on_entry(req)

        # 入力
        msg = self.on_trigger(req)

        # 分岐
        if msg == E_REJECT:
            self.on_reject(req)
            return E_REJECT

        else:
            raise ValueError(f"Unexpected msg:{msg}")

    def on_entry(self, req):
        pass

    def on_trigger(self, req):
        return req.pull_trigger()

    def on_reject(self, req):
        pass
