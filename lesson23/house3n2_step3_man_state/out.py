def create_out(state):
    def on_entry(self, req):
        req.c_sock.send(
            """You can see the house.
You can see the close knob.""".encode()
        )

    # def on_trigger(self, req):
    #    return req.pull_trigger()

    # def on_turned_knob(self, req):
    #    pass

    def on_failed(self, req):
        pass

    state.on_entry = on_entry
    # state.on_trigger = on_trigger
    # state.on_turned_knob = on_turned_knob
    # state.on_failed = on_failed
    return state
