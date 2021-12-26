from lesson23_data.step1n2_auto_const.house3n2_const import (
    E_FAILED,
    E_PULLED_KNOB,
    MSG_PULL_KNOB,
)


def create_out_closedoor(state):
    def __on_entry(req):
        req.context.c_sock.send("""You can see the close door.""".encode())

    def __on_trigger(req):
        msg = req.pull_trigger()
        if msg == MSG_PULL_KNOB:
            return E_PULLED_KNOB
        else:
            return E_FAILED

    state.on_entry = __on_entry
    state.on_trigger = __on_trigger
    return state
