from lesson23_data.auto_gen.house3n2_const import (
    E_FAILED,
    E_SITTING_DOWN,
    MSG_SIT_DOWN,
)


def create_myroom(state):
    def __on_entry(req):
        req.context.c_sock.send("You can see the your room.".encode())

    def __on_trigger(req):
        msg = req.pull_trigger()
        if msg == MSG_SIT_DOWN:
            return E_SITTING_DOWN
        else:
            return E_FAILED

    def __on_sitting_down(req):
        req.context.c_sock.send(
            """Clear!
Please push q key to quit.""".encode()
        )

    state.on_entry = __on_entry
    state.on_trigger = __on_trigger
    state.on_sitting_down = __on_sitting_down

    return state
