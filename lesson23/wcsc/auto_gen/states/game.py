from lesson23_projects.wcsc.data.auto_gen.const import E_GAME_OVER_FLOODGATE, E_GAME_OVER_WCSC, E_MOVE, E_MOVE_ECHO

class GameState():
    def update(self, req):

        self.on_entry(req)

        # 入力
        msg = self.on_trigger(req)

        # 分岐
        if msg == E_MOVE:
            self.on_move(req)
            return E_MOVE

        elif msg == E_MOVE_ECHO:
            self.on_move_echo(req)
            return E_MOVE_ECHO

        elif msg == E_GAME_OVER_FLOODGATE:
            self.on_game_over_floodgate(req)
            return E_GAME_OVER_FLOODGATE

        elif msg == E_GAME_OVER_WCSC:
            self.on_game_over_wcsc(req)
            return E_GAME_OVER_WCSC

        else:
            raise ValueError(f"Unexpected msg:{msg}")

    def on_entry(self, req):
        pass

    def on_trigger(self, req):
        return req.context.pull_trigger()

    def on_move(self, req):
        pass

    def on_move_echo(self, req):
        pass

    def on_game_over_floodgate(self, req):
        pass

    def on_game_over_wcsc(self, req):
        pass

