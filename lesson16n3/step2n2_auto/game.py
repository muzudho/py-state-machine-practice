class GameState():

    def update(self, req):

        # TODO 入力
        msg = ""

        # 分岐
        if msg == 'move':
            return ['Game']

        elif msg == 'move_echo':
            return ['Game']

        elif msg == 'game_over_floodgate':
            return ['Init']

        elif msg == 'game_over_wcsc':
            return ['Lobby']

        else:
            raise ValueError("Unexpected condition")
