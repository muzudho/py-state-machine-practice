from lesson12_projects.house3.data.const import E_ENTER, MSG_ENTER, E_FAILED


class OutOpendoorState:
    def __init__(self):
        pass

    def update(self, c_sock, pull_trigger):
        c_sock.send("You can see the open door.".encode())

        # 入力
        message = pull_trigger()

        # 外に居ます。 'Enter' とメッセージを送ってくるのが正解です
        if message == MSG_ENTER:
            return E_ENTER

        else:
            return E_FAILED
