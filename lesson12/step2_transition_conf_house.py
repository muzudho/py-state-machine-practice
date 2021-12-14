from lesson12.step1_const_conf_house import (
    E_ENTER,
    E_PULLED_KNOB,
    E_TURNED_KNOB,
    OUT,
    E_FAILED,
    E_SITTING_DOWN,
    E_UP,
    MY_ROOM,
    CLOSE_DOOR,
    OPEN_DOOR,
    STAIRS,
)

transition_conf = {
    OUT: {
        E_TURNED_KNOB: CLOSE_DOOR,
        E_FAILED: OUT,
    },
    CLOSE_DOOR: {
        E_PULLED_KNOB: OPEN_DOOR,
        E_FAILED: OUT,
    },
    OPEN_DOOR: {
        E_ENTER: STAIRS,
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
