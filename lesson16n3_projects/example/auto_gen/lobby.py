class LobbyState():

    def update(self, req):

        # TODO 入力
        msg = ""

        # 分岐
        if msg == 'game_summary':
            return ['Reply']

        elif msg == 'logout':
            return ['Lobby', 'Logout']

        else:
            raise ValueError("Unexpected condition")
