"""State Generator"""
from lesson17_projects.wcsc.auto_gen.data.const import (
    INIT,
    LOGIN,
    LOBBY,
    LOGOUT,
    REPLY,
    AGREE,
    REJECT,
    GAME,
)

# State
from lesson18_projects.wcsc.auto_gen.code.states1.game import GameState
from lesson18_projects.wcsc.auto_gen.code.states1.init_login import InitLoginState
from lesson18_projects.wcsc.auto_gen.code.states1.init import InitState
from lesson18_projects.wcsc.auto_gen.code.states1.lobby_logout import LobbyLogoutState
from lesson18_projects.wcsc.auto_gen.code.states1.lobby import LobbyState
from lesson18_projects.wcsc.auto_gen.code.states1.reply_agree import ReplyAgreeState
from lesson18_projects.wcsc.auto_gen.code.states1.reply_reject import ReplyRejectState
from lesson18_projects.wcsc.auto_gen.code.states1.reply import ReplyState

# State wrapper
from lesson23_projects.wcsc.code.states2.game import create_game
from lesson23_projects.wcsc.code.states2.init_login import create_init_login
from lesson23_projects.wcsc.code.states2.init import create_init
from lesson23_projects.wcsc.code.states2.lobby_logout import create_lobby_logout
from lesson23_projects.wcsc.code.states2.lobby import create_lobby
from lesson23_projects.wcsc.code.states2.reply_agree import create_reply_agree
from lesson23_projects.wcsc.code.states2.reply_reject import create_reply_reject
from lesson23_projects.wcsc.code.states2.reply import create_reply


# ステートを使い回すのではなく、アクセスするたびに ステートの生成を実行しなおせるよう、ラムダ関数を返します
wcsc_state_gen_v23 = {
    INIT: {
        "": lambda: create_init(InitState()),
        LOGIN: lambda: create_init_login(InitLoginState()),
    },
    LOBBY: {
        "": lambda: create_lobby(LobbyState()),
        LOGOUT: lambda: create_lobby_logout(LobbyLogoutState()),
    },
    REPLY: {
        "": lambda: create_reply(ReplyState()),
        AGREE: lambda: create_reply_agree(ReplyAgreeState()),
        REJECT: lambda: create_reply_reject(ReplyRejectState()),
    },
    GAME: {
        "": lambda: create_game(GameState()),
    },
}
