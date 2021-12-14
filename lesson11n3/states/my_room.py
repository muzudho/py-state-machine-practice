from lesson11n3.const_conf import MSG_SIT_DOWN, E_FAILED, E_SITTING_DOWN


class MyRoomState():
    def __init__(self):
        pass

    def update(self, message, c_sock):
        # 'Sit down' とメッセージを送ってくるのが正解です
        if message == MSG_SIT_DOWN:
            c_sock.send("""Clear!
Please push q key to quit.""".encode())
            return E_SITTING_DOWN

        else:
            c_sock.send("You can see the house.".encode())
            return E_FAILED
