from lesson11n2.keywords import OPEN, OUT, STAIRS


class OutState():
    def __init__(self):
        pass

    def react(self, message, c_sock):
        # 外に居ます。 'Open' とメッセージを送ってくるのが正解です
        if message == OPEN:
            c_sock.send("You can see the stairs.".encode())
            return STAIRS

        else:
            c_sock.send("You can see the house.".encode())
            return OUT
