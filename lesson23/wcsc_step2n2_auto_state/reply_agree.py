from lesson18_data.step1n2_auto_const.pen_const import E_START

class ReplyAgreeState():
    def update(self, req):

        self.on_entry(req)

        # 入力
        msg = self.on_trigger(req)

        # 分岐
        if msg == E_START:
            self.on_start(req)
            return E_START

        else:
            raise ValueError(f"Unexpected msg:{msg}")

    def on_entry(self, req):
        pass

    def on_trigger(self, req):
        return req.pull_trigger()

    def on_start(self, req):
        pass

