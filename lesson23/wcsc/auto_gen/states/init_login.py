from lesson23_projects.wcsc.data.auto_gen.const import E_INCORRECT, E_OK

class InitLoginState():
    def update(self, req):

        self.on_entry(req)

        # 入力
        msg = self.on_trigger(req)

        # 分岐
        if msg == E_OK:
            self.on_ok(req)
            return E_OK

        elif msg == E_INCORRECT:
            self.on_incorrect(req)
            return E_INCORRECT

        else:
            raise ValueError(f"Unexpected msg:{msg}")

    def on_entry(self, req):
        pass

    def on_trigger(self, req):
        return req.context.pull_trigger()

    def on_ok(self, req):
        pass

    def on_incorrect(self, req):
        pass

