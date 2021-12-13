from lesson11n3.keywords import (
    OUT,
    E_FAILED,
    E_OPENED,
    E_SITTING_DOWN,
    E_UP,
    MY_ROOM,
    STAIRS,
)

transition_conf = {
    OUT: {
        E_OPENED: STAIRS,
        E_FAILED: OUT,
    },
    STAIRS: {
        E_UP: MY_ROOM,
        E_FAILED: OUT,
    },
    MY_ROOM: {
        E_SITTING_DOWN: MY_ROOM,
        E_FAILED: OUT,
    },
}
