from lesson12_projects.house3.data.const import (
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

house3_transition_py_dict = {
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
