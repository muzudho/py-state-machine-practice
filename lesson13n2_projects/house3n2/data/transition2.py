from lesson12_projects.house3.data.const import (
    CLOSE_DOOR,
    E_ENTER,
    E_PULLED_KNOB,
    E_TURNED_KNOB,
    OPEN_DOOR,
    OUT,
    E_FAILED,
    E_SITTING_DOWN,
    E_UP,
    MY_ROOM,
    STAIRS,
)

house3n2_transition2_py_dict = {
    OUT: {
        E_TURNED_KNOB: [OUT, CLOSE_DOOR],
        E_FAILED: [OUT],
        CLOSE_DOOR: {
            E_PULLED_KNOB: [OUT, OPEN_DOOR],
            E_FAILED: [OUT],
        },
        OPEN_DOOR: {
            E_ENTER: [STAIRS],
            E_FAILED: [OUT],
        },
    },
    STAIRS: {
        E_UP: [MY_ROOM],
        E_FAILED: [OUT],
    },
    MY_ROOM: {
        E_SITTING_DOWN: None,  # None に変更
        E_FAILED: [OUT],
    },
}
