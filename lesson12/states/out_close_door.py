from lesson12_data.step1_house3_const import E_PULLED_KNOB, MSG_PULL_KNOB, E_FAILED


class OutCloseDoorState:
    def __init__(self):
        pass

    def update(self, message, c_sock):
        # 外に居ます。 'Pull knob' とメッセージを送ってくるのが正解です
        if message == MSG_PULL_KNOB:
            c_sock.send("You can see the open door.".encode())
            return E_PULLED_KNOB

        else:
            c_sock.send(
                """You can see the house.
You can see the close knob.""".encode()
            )
            return E_FAILED
