from lesson12.keywords import E_TURNED_KNOB, MSG_TURN_KNOB
from lesson12.keywords import E_FAILED


class OutState():
    def __init__(self):
        pass

    def react(self, message, c_sock):
        # 外に居ます。 'Turn knob' とメッセージを送ってくるのが正解です
        if message == MSG_TURN_KNOB:
            c_sock.send("""You can see the close door.""".encode())
            return E_TURNED_KNOB

        else:
            c_sock.send("""You can see the house.
You can see the close knob.""".encode())
            return E_FAILED