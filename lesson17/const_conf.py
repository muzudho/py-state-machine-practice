class ConstConf:
    def __init__(self):
        # 全単射にしてください
        self._data = {
            # States
            # ------
            #
            # ディクショナリーのキーとして Edge と被らないように PascalCase にします
            "INIT": "Init",
            "LOGIN": "Login",
            "LOBBY": "Lobby",
            "LOGOUT": "Logout",
            "REPLY": "Reply",
            "AGREE": "Agree",
            "REJECT": "Reject",
            "GAME": "Game",
            # Edges
            # -----
            #
            # ディクショナリーのキーとして State と被らないように頭に snake_case にします
            "E_OK": "ok",
            "E_INCORRECT": "incorrect",
            "E_LOGOUT": "logout",
            "E_COMPLETED": "completed",
            "E_GAME_SUMMARY": "game_summary",
            "E_AGREE": "agree",
            "E_REJECT": "reject",
            "E_START": "start",
            "E_MOVE": "move",
            "E_MOVE_ECHO": "move_echo",
            "E_GAME_OVER_FLOODGATE": "game_over_floodgate",
            "E_GAME_OVER_WCSC": "game_over_wcsc",
            "E_OVER": "over",  # 練習プログラム用
        }

        # 逆向きは自動生成します
        self._rev_data = {}

        for key, value in self._data.items():
            self._rev_data[value] = key

    @property
    def data(self):
        return self._data

    @property
    def rev_data(self):
        return self._rev_data
