from lesson13n2.keywords import E_PULLED_KNOB, MSG_PULL_KNOB, E_FAILED


class OutCloseDoorState():
    def __init__(self):
        pass

    def update(self, req):
        req.c_sock.send("""You can see the close door.""".encode())

        # 入力
        message = req.pull_trigger()

        # 外に居ます。 'Pull knob' とメッセージを送ってくるのが正解です
        if message == MSG_PULL_KNOB:
            return E_PULLED_KNOB

        else:
            return E_FAILED
