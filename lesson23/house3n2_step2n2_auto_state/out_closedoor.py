from lesson23_data.step1n2_auto_const.house3n2_const import E_FAILED, E_PULLED_KNOB

class OutCloseDoorState():
    def update(self, req):

        self.on_entry(req)

        # 入力
        msg = self.on_trigger(req)

        # 分岐
        if msg == E_PULLED_KNOB:
            self.on_pulled_knob(req)
            return E_PULLED_KNOB

        elif msg == E_FAILED:
            self.on_failed(req)
            return E_FAILED

        else:
            raise ValueError(f"Unexpected msg:{msg}")

    def on_entry(self, req):
        pass

    def on_trigger(self, req):
        return req.pull_trigger()

    def on_pulled_knob(self, req):
        pass

    def on_failed(self, req):
        pass

