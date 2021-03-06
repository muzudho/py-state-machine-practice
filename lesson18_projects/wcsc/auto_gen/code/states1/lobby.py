from lesson17_projects.wcsc.auto_gen.data.const import E_GAME_SUMMARY, E_LOGOUT

class LobbyState():
    def update(self, req):

        self.on_entry(req)

        # 入力
        msg = self.on_trigger(req)

        # 分岐
        if msg == E_GAME_SUMMARY:
            self.on_game_summary(req)
            return E_GAME_SUMMARY

        elif msg == E_LOGOUT:
            self.on_logout(req)
            return E_LOGOUT

        elif msg == None:
            return None

        else:
            raise ValueError(f"Unexpected msg:{msg}")

    def on_entry(self, req):
        pass

    def on_trigger(self, req):
        return req.context.pull_trigger()

    def on_game_summary(self, req):
        pass

    def on_logout(self, req):
        pass

