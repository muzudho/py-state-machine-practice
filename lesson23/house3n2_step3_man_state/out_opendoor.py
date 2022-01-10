from lesson23_projects.house3n2.data.auto_gen.const import (
    E_FAILED,
    E_ENTER,
    MSG_ENTER,
)


def create_out_opendoor(state):
    def __on_entry(req):
        req.context.c_sock.send("You can see the open door.".encode())

    def __on_trigger(req):
        msg = req.pull_trigger()
        if msg == MSG_ENTER:
            return E_ENTER
        else:
            return E_FAILED

    state.on_entry = __on_entry
    state.on_trigger = __on_trigger
    return state
