from lesson23_data.step1n2_auto_const.wcsc_const import E_COMPLETED

class LobbyLogoutState():
    def update(self, req):

        self.on_entry(req)

        # 入力
        msg = self.on_trigger(req)

        # 分岐
        if msg == E_COMPLETED:
            self.on_completed(req)
            return E_COMPLETED

        else:
            raise ValueError(f"Unexpected msg:{msg}")

    def on_entry(self, req):
        pass

    def on_trigger(self, req):
        return req.context.pull_trigger()

    def on_completed(self, req):
        pass

