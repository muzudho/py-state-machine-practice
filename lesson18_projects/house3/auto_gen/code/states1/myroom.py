from lesson17_projects.house3.auto_gen.data.const import E_FAILED, E_SITTING_DOWN

class MyroomState():
    def update(self, req):

        self.on_entry(req)

        # 入力
        msg = self.on_trigger(req)

        # 分岐
        if msg == E_SITTING_DOWN:
            self.on_sitting_down(req)
            return E_SITTING_DOWN

        elif msg == E_FAILED:
            self.on_failed(req)
            return E_FAILED

        elif msg == None:
            return None

        else:
            raise ValueError(f"Unexpected msg:{msg}")

    def on_entry(self, req):
        pass

    def on_trigger(self, req):
        return req.context.pull_trigger()

    def on_sitting_down(self, req):
        pass

    def on_failed(self, req):
        pass

