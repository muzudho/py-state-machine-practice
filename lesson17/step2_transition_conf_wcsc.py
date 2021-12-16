from lesson17.step1n2_auto_const.pen import (
    AGREE,
    E_AGREE,
    E_COMPLETED,
    E_GAME_OVER_FLOODGATE,
    E_GAME_OVER_WCSC,
    E_GAME_SUMMARY,
    E_INCORRECT,
    E_LOGOUT,
    E_MOVE,
    E_MOVE_ECHO,
    E_OK,
    E_REJECT,
    E_START,
    GAME,
    INIT,
    LOBBY,
    LOGIN,
    LOGOUT,
    REJECT,
    REPLY,
)

transition_conf_data = {
    "@title": "CSA Server protocol 1.2.1",
    "@entry_node": INIT,
    "@data": {
        INIT: {
            "": [INIT, LOGIN],
            LOGIN: {E_OK: [LOBBY], E_INCORRECT: [INIT]},
        },
        LOBBY: {
            E_GAME_SUMMARY: [REPLY],
            E_LOGOUT: [LOBBY, LOGOUT],
            LOGOUT: {E_COMPLETED: [INIT]},
        },
        REPLY: {
            E_AGREE: [REPLY, AGREE],
            E_REJECT: [REPLY, REJECT],
            AGREE: {E_START: [GAME]},
            REJECT: {E_REJECT: [LOBBY]},
        },
        GAME: {
            E_MOVE: [GAME],
            E_MOVE_ECHO: [GAME],
            E_GAME_OVER_FLOODGATE: [INIT],
            E_GAME_OVER_WCSC: [LOBBY],
        },
    },
}
