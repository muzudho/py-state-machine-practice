from lesson12n2.keywords import MSG_SIT_DOWN
from lesson12n2.keywords import E_FAILED, E_SITTING_DOWN


class MyRoomState():
    def __init__(self):
        pass

    def react(self, c_sock, pull_trigger):
        c_sock.send("You can see the your room.".encode())

        # 入力
        message = pull_trigger()

        # 'Sit down' とメッセージを送ってくるのが正解です
        if message == MSG_SIT_DOWN:
            c_sock.send("Clear!".encode())
            return E_SITTING_DOWN

        else:
            return E_FAILED