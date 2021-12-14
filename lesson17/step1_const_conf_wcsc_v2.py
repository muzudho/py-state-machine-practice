class ConstConf:
    def __init__(self):
        # (1) キーと値は 全単射にしてください
        # (2) 大文字と小文字は区別します
        self._data = {
            # States
            # ------
            #
            # "ステート定数": "ステートマシン図のノード名"
            # 本レッスンではノード名を PascalCase にします（エッジと被らないように）
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
            # "エッジ定数": "ステートマシン図のエッジ名"
            # 本レッスンではエッジ名を snake_case にします（ノード名と被らないように）
            # ディクショナリーのキーとして State と被らないように頭に E_ を付けます
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
            "E_OVER": "over",  # 'E_OVER' は練習プログラム用
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
