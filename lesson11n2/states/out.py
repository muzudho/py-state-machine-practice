from lesson11_data.step1_const_house_v1 import MSG_OPEN, OUT, STAIRS


class OutState:
    def __init__(self):
        pass

    def update(self, message, c_sock):
        # 外に居ます。 'Open' とメッセージを送ってくるのが正解です
        if message == MSG_OPEN:
            c_sock.send("You can see the stairs.".encode())
            return STAIRS

        else:
            c_sock.send("You can see the house.".encode())
            return OUT
