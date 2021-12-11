from lesson12n3.keywords import E_ENTER, E_PULLED_KNOB, E_TURNED_KNOB, OUT, E_FAILED, E_SITTING_DOWN, E_UP, MY_ROOM, OUT_CLOSE_DOOR, OUT_OPEN_DOOR, STAIRS

transition = {
    OUT: {
        E_TURNED_KNOB: OUT_CLOSE_DOOR,
        E_FAILED: OUT,
    },
    OUT_CLOSE_DOOR: {
        E_PULLED_KNOB: OUT_OPEN_DOOR,
        E_FAILED: OUT,
    },
    OUT_OPEN_DOOR: {
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
    }
}
