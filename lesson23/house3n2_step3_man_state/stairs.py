from lesson23_data.step1n2_auto_const.house3n2_const import E_FAILED, E_UP, MSG_UP


def create_stairs(state):
    def __on_entry(req):
        req.c_sock.send("You can see the stairs.".encode())

    def __on_trigger(req):
        msg = req.pull_trigger()
        if msg == MSG_UP:
            return E_UP
        else:
            return E_FAILED

    state.on_entry = __on_entry
    state.on_trigger = __on_trigger
    return state
