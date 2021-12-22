from lesson18_data.step1n2_auto_const.pen_const import E_ENTER, E_FAILED

class OutOpenDoorState():
    def update(self, req):

        self.on_entry(req)

        # 入力
        msg = self.on_trigger(req)

        # 分岐
        if msg == E_ENTER:
            self.on_enter(req)
            return E_ENTER

        elif msg == E_FAILED:
            self.on_failed(req)
            return E_FAILED

        else:
            raise ValueError(f"Unexpected msg:{msg}")

    def on_entry(self, req):
        pass

    def on_trigger(self, req):
        return req.pull_trigger()

    def on_enter(self, req):
        pass

    def on_failed(self, req):
        pass

