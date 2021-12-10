from lesson11n2.keywords import UP
from lesson11n2.states.my_room import MyRoomState
from lesson11n2.states.out import OutState


class StairsState():
    def __init__(self):
        pass

    def react(self, message, c_sock):
        # `Up` とメッセージを送ってくるのが正解です
        if message == UP:
            c_sock.send("You can see the your room.".encode())
            return MyRoomState()

        else:
            c_sock.send("You can see the house.".encode())
            return OutState()
