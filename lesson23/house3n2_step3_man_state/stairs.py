def create_stairs(state):
    def __on_entry(req):
        req.c_sock.send("You can see the stairs.".encode())

    state.on_entry = __on_entry
    return state
