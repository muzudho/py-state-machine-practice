from lesson17.step1n2_auto.const import E_GAME_OVER_FLOODGATE, E_MOVE_ECHO, E_MOVE, E_GAME_OVER_WCSC

class GameState():

    def update(self, req):

        # 入力
        msg = req.pull_trigger()

        # 分岐
        if msg == E_MOVE:
            return ['Game']
        elif msg == E_MOVE_ECHO:
            return ['Game']
        elif msg == E_GAME_OVER_FLOODGATE:
            return ['Init']
        elif msg == E_GAME_OVER_WCSC:
            return ['Lobby']
        else:
            raise ValueError("Unexpected condition")

