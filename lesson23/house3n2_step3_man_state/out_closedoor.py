def create_out_close_door(state):
    def __on_entry(self, req):
        req.c_sock.send("""You can see the close door.""".encode())

    # def __on_trigger(self, req):
    #    pass

    # def __on_pulled_knob(self, req):
    #    pass

    # def __on_failed(self, req):
    #    pass

    state.on_entry = __on_entry
    # state.on_trigger = __on_trigger
    # state.on_pulled_knob = __on_pulled_knob
    # state.on_failed = __on_failed
    return state
