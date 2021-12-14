# States
# ------
#
# "ステート定数": "ステートマシン図のノード名"
# 本レッスンではノード名を PascalCase にします（エッジと被らないように）

INIT = "Init"
LOGIN = "Login"
LOBBY = "Lobby"
LOGOUT = "Logout"
REPLY = "Reply"
AGREE = "Agree"
REJECT = "Reject"
GAME = "Game"

# Edges
# -----
#
# "エッジ定数": "ステートマシン図のエッジ名"
# 本レッスンではエッジ名を snake_case にします（ノード名と被らないように）
# ディクショナリーのキーとして State と被らないように頭に E_ を付けます

E_OK = "ok"
E_INCORRECT = "incorrect"
E_LOGOUT = "logout"
E_COMPLETED = "completed"
E_GAME_SUMMARY = "game_summary"
E_AGREE = "agree"
E_REJECT = "reject"
E_START = "start"
E_MOVE = "move"
E_MOVE_ECHO = "move_echo"
E_GAME_OVER_FLOODGATE = "game_over_floodgate"
E_GAME_OVER_WCSC = "game_over_wcsc"
E_OVER = "over"  # あとのレッスン用
