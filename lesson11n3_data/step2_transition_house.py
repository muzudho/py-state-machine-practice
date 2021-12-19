from lesson11n3_data.step1_const_house_v2 import (
    OUT,
    E_FAILED,
    E_OPENED,
    E_SITTING_DOWN,
    E_UP,
    MY_ROOM,
    STAIRS,
)

transition_house_py_dict = {
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
