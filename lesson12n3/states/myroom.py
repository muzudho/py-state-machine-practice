from lesson12_projects.house3.data.const import MSG_SIT_DOWN, E_FAILED, E_SITTING_DOWN


class MyroomState:
    def __init__(self):
        pass

    def update(self, req):
        req.c_sock.send("You can see the your room.".encode())

        # 入力
        message = req.pull_trigger()

        # 'Sit down' とメッセージを送ってくるのが正解です
        if message == MSG_SIT_DOWN:
            req.c_sock.send(
                """Clear!
Please push q key to quit.""".encode()
            )
            return E_SITTING_DOWN

        else:
            return E_FAILED
