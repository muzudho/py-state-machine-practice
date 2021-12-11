from lesson13.keywords import E_ENTER, MSG_ENTER, E_FAILED


class OutOpenDoorState():
    def __init__(self):
        pass

    def update(self, req):
        req.c_sock.send("You can see the open door.".encode())

        # 入力
        message = req.pull_trigger()

        # 外に居ます。 'Enter' とメッセージを送ってくるのが正解です
        if message == MSG_ENTER:
            return E_ENTER

        else:
            return E_FAILED
