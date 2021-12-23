def create_stairs(state):
    def __on_entry(self, req):
        req.c_sock.send("You can see the stairs.".encode())

    # def __on_trigger(self, req):
    #    pass

    # def __on_up(self, req):
    #    pass

    # def __on_failed(self, req):
    #    pass

    state.on_entry = __on_entry
    # state.on_trigger = __on_trigger
    # state.on_up = __on_up
    # state.on_failed = __on_failed
    return state
