from lesson23_projects.house3n2.auto_gen.data.const import (
    E_FAILED,
    E_TURNED_KNOB,
    MSG_TURN_KNOB,
)


def create_out(state):
    def __on_entry(req):
        req.context.c_sock.send(
            """You can see the house.
You can see the close knob.""".encode()
        )

    def __on_trigger(req):
        msg = req.pull_trigger()
        if msg == MSG_TURN_KNOB:
            return E_TURNED_KNOB
        else:
            return E_FAILED

    state.on_entry = __on_entry
    state.on_trigger = __on_trigger
    return state
