def create_out_closedoor(state):
    def __on_entry(req):
        req.c_sock.send("""You can see the close door.""".encode())

    state.on_entry = __on_entry
    return state
