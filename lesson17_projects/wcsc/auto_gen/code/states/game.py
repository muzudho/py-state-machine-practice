from lesson17_projects.wcsc.data.auto_gen.const import INIT, LOBBY, GAME, E_MOVE_ECHO, E_MOVE, E_GAME_OVER_WCSC, E_GAME_OVER_FLOODGATE

class GameState():

    def update(self, req):

        # 入力
        msg = req.pull_trigger()

        # 分岐
        if msg == E_MOVE:
            return [GAME]

        elif msg == E_MOVE_ECHO:
            return [GAME]

        elif msg == E_GAME_OVER_FLOODGATE:
            return [INIT]

        elif msg == E_GAME_OVER_WCSC:
            return [LOBBY]

        else:
            raise ValueError(f"Unexpected msg:{msg}")

