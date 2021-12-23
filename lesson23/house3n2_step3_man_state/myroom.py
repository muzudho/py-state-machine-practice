def create_myroom(state):
    def __on_entry(req):
        req.c_sock.send("You can see the your room.".encode())

    def __on_sitting_down(req):
        req.c_sock.send(
            """Clear!
Please push q key to quit.""".encode()
        )

    state.on_entry = __on_entry
    state.on_sitting_down = __on_sitting_down

    return state
