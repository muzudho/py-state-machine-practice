from lesson17.step2_auto.const import (
    E_MOVE_ECHO,
    E_GAME_OVER_WCSC,
    E_GAME_OVER_FLOODGATE,
    E_MOVE,
)


class GameState:
    def update(self, req):

        # TODO 入力
        msg = ""

        # 分岐
        if msg == E_MOVE:
            return ["Game"]
        elif msg == E_MOVE_ECHO:
            return ["Game"]
        elif msg == E_GAME_OVER_FLOODGATE:
            return ["Init"]
        elif msg == E_GAME_OVER_WCSC:
            return ["Lobby"]
        else:
            raise ValueError("Unexpected condition")
