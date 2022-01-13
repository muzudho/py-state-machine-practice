from lesson11n203_projects.house2.data.const import (
    OUT,
    E_FAILED,
    E_OPENED,
    E_SITTING_DOWN,
    E_UP,
    MY_ROOM,
    STAIRS,
)

house2_transition_py_dict = {
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
