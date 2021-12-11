from lesson12n2.keywords import E_TURNED_KNOB, MSG_TURN_KNOB
from lesson12n2.keywords import E_FAILED


class OutState():
    def __init__(self):
        pass

    def react(self, c_sock, pull_trigger):
        c_sock.send("""You can see the house.
You can see the close knob.""".encode())

        # 入力
        message = pull_trigger()

        # 外に居ます。 'Turn knob' とメッセージを送ってくるのが正解です
        if message == MSG_TURN_KNOB:
            return E_TURNED_KNOB

        else:
            return E_FAILED
