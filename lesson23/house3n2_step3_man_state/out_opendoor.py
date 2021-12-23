def create_out_opendoor(state):
    def __on_entry(req):
        req.c_sock.send("You can see the open door.".encode())

    state.on_entry = __on_entry
    return state
