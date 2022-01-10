from lesson23_projects.house3n2.data.auto_gen.const import E_FAILED, E_UP, MSG_UP


def create_stairs(state):
    def __on_entry(req):
        req.context.c_sock.send("You can see the stairs.".encode())

    def __on_trigger(req):
        msg = req.pull_trigger()
        if msg == MSG_UP:
            return E_UP
        else:
            return E_FAILED

    state.on_entry = __on_entry
    state.on_trigger = __on_trigger
    return state
