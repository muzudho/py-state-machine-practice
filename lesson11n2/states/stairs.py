from lesson11n2.keywords import MY_ROOM, OUT, UP


class StairsState():
    def __init__(self):
        pass

    def react(self, message, c_sock):
        # `Up` とメッセージを送ってくるのが正解です
        if message == UP:
            c_sock.send("You can see the your room.".encode())
            return MY_ROOM

        else:
            c_sock.send("You can see the house.".encode())
            return OUT
