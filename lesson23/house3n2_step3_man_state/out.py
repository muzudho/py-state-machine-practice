def create_out(state):
    def on_entry(req):
        req.c_sock.send(
            """You can see the house.
You can see the close knob.""".encode()
        )

    state.on_entry = on_entry
    return state
