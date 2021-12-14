from lesson11n2.const_conf import MY_ROOM, OUT, MSG_UP


class StairsState:
    def __init__(self):
        pass

    def update(self, message, c_sock):
        # `Up` とメッセージを送ってくるのが正解です
        if message == MSG_UP:
            c_sock.send("You can see the your room.".encode())
            return MY_ROOM

        else:
            c_sock.send("You can see the house.".encode())
            return OUT
