from lesson11n2.keywords import SIT_DOWN
from lesson11n2.states.out import OutState


class MyRoomState():
    def __init__(self):
        pass

    def react(self, message, c_sock):
        # 'Sit down' とメッセージを送ってくるのが正解です
        if message == SIT_DOWN:
            c_sock.send("Clear!".encode())
            return self

        else:
            c_sock.send("You can see the house.".encode())
            return OutState()
