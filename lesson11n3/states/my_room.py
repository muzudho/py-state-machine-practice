from lesson11n3.keywords import MSG_SIT_DOWN
from lesson11n3.keywords import E_FAILED, E_SITTING_DOWN


class MyRoomState():
    def __init__(self):
        pass

    def react(self, message, c_sock):
        # 'Sit down' とメッセージを送ってくるのが正解です
        if message == MSG_SIT_DOWN:
            c_sock.send("Clear!".encode())
            return E_SITTING_DOWN

        else:
            c_sock.send("You can see the house.".encode())
            return E_FAILED
