from lesson17_projects.house3.auto_gen.data.const import E_FAILED, E_TURNED_KNOB

class OutState():
    def update(self, req):

        self.on_entry(req)

        # 入力
        msg = self.on_trigger(req)

        # 分岐
        if msg == E_TURNED_KNOB:
            self.on_turned_knob(req)
            return E_TURNED_KNOB

        elif msg == E_FAILED:
            self.on_failed(req)
            return E_FAILED

        else:
            raise ValueError(f"Unexpected msg:{msg}")

    def on_entry(self, req):
        pass

    def on_trigger(self, req):
        return req.context.pull_trigger()

    def on_turned_knob(self, req):
        pass

    def on_failed(self, req):
        pass

