def create_myroom(state):
    def __on_entry(self, req):
        req.c_sock.send("You can see the your room.".encode())

    # def __on_trigger(self, req):
    #    pass

    def __on_sitting_down(self, req):
        req.c_sock.send(
            """Clear!
Please push q key to quit.""".encode()
        )

    # def __on_failed(self, req):
    #    pass

    state.on_entry = __on_entry
    # state.on_trigger = __on_trigger
    state.on_sitting_down = __on_sitting_down
    # state.on_failed = __on_failed

    return state
