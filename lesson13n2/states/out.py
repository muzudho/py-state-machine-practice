from lesson12_projects.house3.data.const import E_TURNED_KNOB, MSG_TURN_KNOB, E_FAILED


class OutState:
    def update(self, req):

        self.on_entry(req)

        # 入力
        msg = self.on_trigger(req)

        # 外に居ます。 'Turn knob' とメッセージを送ってくるのが正解です
        if msg == MSG_TURN_KNOB:
            self.on_turned_knob(req)
            return E_TURNED_KNOB

        else:
            self.on_failed(req)
            return E_FAILED

    def on_entry(self, req):
        req.c_sock.send(
            """You can see the house.
You can see the close knob.""".encode()
        )

    def on_trigger(self, req):
        return req.pull_trigger()

    def on_turned_knob(self, req):
        pass

    def on_failed(self, req):
        pass
