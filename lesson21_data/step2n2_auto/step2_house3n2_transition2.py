from lesson18_data.step1n2_auto_const.pen_const import CLOSE_DOOR, E_ENTER, E_FAILED, E_PULLED_KNOB, E_SITTING_DOWN, E_TURNED_KNOB, E_UP, MY_ROOM, OPEN_DOOR, OUT, STAIRS

house3n2_transition2_py_dict = {
    "title": "House",
    "entry_node": OUT,
    "data": {
        OUT: {
            E_TURNED_KNOB: [OUT, CLOSE_DOOR],
            E_FAILED: [OUT],
            CLOSE_DOOR: {
                E_PULLED_KNOB: [OUT, OPEN_DOOR],
                E_FAILED: [OUT]
            },
            OPEN_DOOR: {
                E_ENTER: [STAIRS],
                E_FAILED: [OUT]
            }
        },
        STAIRS: {
            E_UP: [MY_ROOM],
            E_FAILED: [OUT]
        },
        MY_ROOM: {
            E_SITTING_DOWN: None,
            E_FAILED: [OUT]
        }
    }
}
