"""State Generator"""
from lesson23_data.step1n2_auto_const.wcsc_const import (
    INIT,
    LOGIN,
    LOBBY,
    LOGOUT,
    REPLY,
    AGREE,
    REJECT,
    GAME,
    E_OK,
    E_INCORRECT,
    E_LOGOUT,
    E_COMPLETED,
    E_GAME_SUMMARY,
    E_AGREE,
    E_REJECT,
    E_START,
    E_MOVE,
    E_MOVE_ECHO,
    E_GAME_OVER_FLOODGATE,
    E_GAME_OVER_WCSC,
    E_OVER,
)

# Lesson 23 State
from lesson23.wcsc_step2n2_auto_state.game import GameState
from lesson23.wcsc_step2n2_auto_state.init_login import InitLoginState
from lesson23.wcsc_step2n2_auto_state.init import InitState
from lesson23.wcsc_step2n2_auto_state.lobby_logout import LobbyLogoutState
from lesson23.wcsc_step2n2_auto_state.lobby import LobbyState
from lesson23.wcsc_step2n2_auto_state.reply_agree import ReplyAgreeState
from lesson23.wcsc_step2n2_auto_state.reply_reject import ReplyRejectState
from lesson23.wcsc_step2n2_auto_state.reply import ReplyState

# Lesson 23 State wrapper
from lesson23.wcsc_step3_man_state.game import create_game
from lesson23.wcsc_step3_man_state.init_login import create_init_login
from lesson23.wcsc_step3_man_state.init import create_init
from lesson23.wcsc_step3_man_state.lobby_logout import create_lobby_logout
from lesson23.wcsc_step3_man_state.lobby import create_lobby
from lesson23.wcsc_step3_man_state.reply_agree import create_reply_agree
from lesson23.wcsc_step3_man_state.reply_reject import create_reply_reject
from lesson23.wcsc_step3_man_state.reply import create_reply


# ステートを使い回すのではなく、アクセスするたびに ステートの生成を実行しなおせるよう、ラムダ関数を返します
wcsc_state_gen = {
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
