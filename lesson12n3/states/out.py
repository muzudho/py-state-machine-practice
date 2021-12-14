from lesson12n3.step1_const_conf_house import E_TURNED_KNOB, MSG_TURN_KNOB, E_FAILED


class OutState:
    def __init__(self):
        pass

    def update(self, req):
        req.c_sock.send(
            """You can see the house.
You can see the close knob.""".encode()
        )

        # 入力
        message = req.pull_trigger()

        # 外に居ます。 'Turn knob' とメッセージを送ってくるのが正解です
        if message == MSG_TURN_KNOB:
            return E_TURNED_KNOB

        else:
            return E_FAILED
