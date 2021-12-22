from lesson18_data.step1n2_auto_const.pen_const import E_FAILED, E_UP

class StairsState():
    def update(self, req):

        self.on_entry(req)

        # 入力
        msg = self.on_trigger(req)

        # 分岐
        if msg == E_UP:
            self.on_up(req)
            return E_UP

        elif msg == E_FAILED:
            self.on_failed(req)
            return E_FAILED

        else:
            raise ValueError(f"Unexpected msg:{msg}")

    def on_entry(self, req):
        pass

    def on_trigger(self, req):
        return req.pull_trigger()

    def on_up(self, req):
        pass

    def on_failed(self, req):
        pass

