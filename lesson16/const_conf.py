# States
# ------
#
# ディクショナリーのキーとして Edge と被らないように PascalCase にします

INIT = "Init"
if INIT:  # インデントしてるだけ
    LOGIN = "Login"

LOBBY = "Lobby"
if LOBBY:
    LOGOUT = "Logout"

REPLY = "Reply"
if REPLY:
    AGREE = "Agree"
    REJECT = "Reject"

GAME = "Game"
if GAME:
    pass

# Edges
# -----
#
# ディクショナリーのキーとして State と被らないように頭に snake_case にします

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

E_OVER = "over"  # 練習プログラム用
