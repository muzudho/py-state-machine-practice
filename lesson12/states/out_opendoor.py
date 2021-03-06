from lesson12_projects.house3.data.const import E_ENTER, MSG_ENTER, E_FAILED


class OutOpendoorState:
    def __init__(self):
        pass

    def update(self, message, c_sock):
        # 外に居ます。 'Enter' とメッセージを送ってくるのが正解です
        if message == MSG_ENTER:
            c_sock.send("You can see the stairs.".encode())
            return E_ENTER

        else:
            c_sock.send(
                """You can see the house.
You can see the close knob.""".encode()
            )
            return E_FAILED
