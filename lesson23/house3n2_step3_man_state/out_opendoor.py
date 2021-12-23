def create_out_opendoor(state):
    def __on_entry(self, req):
        req.c_sock.send("You can see the open door.".encode())

    # def __on_trigger(self, req):
    #    pass

    # def __on_enter(self, req):
    #    pass

    # def __on_failed(self, req):
    #    pass

    state.on_entry = __on_entry
    # state.on_trigger = __on_trigger
    # state.on_enter = __on_enter
    # state.on_failed = __on_failed
    return state
