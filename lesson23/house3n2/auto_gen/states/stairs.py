from lesson23_projects.house3n2.data.auto_gen.const import E_FAILED, E_UP

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
        return req.context.pull_trigger()

    def on_up(self, req):
        pass

    def on_failed(self, req):
        pass

