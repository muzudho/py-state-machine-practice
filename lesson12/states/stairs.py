from lesson12.const_conf import MSG_UP, E_FAILED, E_UP


class StairsState:
    def __init__(self):
        pass

    def update(self, message, c_sock):
        # `Up` とメッセージを送ってくるのが正解です
        if message == MSG_UP:
            c_sock.send("You can see the your room.".encode())
            return E_UP

        else:
            c_sock.send(
                """You can see the house.
You can see the close knob.""".encode()
            )
            return E_FAILED
