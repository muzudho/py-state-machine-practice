from lesson11n1.keywords import OPEN
from lesson11n1.states.stairs import StairsState


class OutState():
    def __init__(self):
        pass

    def react(self, message, c_sock):
        # 外に居ます。 'Open' とメッセージを送ってくるのが正解です
        if message == OPEN:
            c_sock.send("You can see the stairs.".encode())
            return StairsState()

        else:
            c_sock.send("You can see the house.".encode())
            return OutState()
