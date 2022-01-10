from lesson12_projects.house3.data.const import E_PULLED_KNOB, MSG_PULL_KNOB, E_FAILED


class OutClosedoorState:
    def update(self, req):

        self.on_entry(req)

        # 入力
        msg = self.on_trigger(req)

        # 外に居ます。 'Pull knob' とメッセージを送ってくるのが正解です
        if msg == MSG_PULL_KNOB:
            self.on_pulled_knob(req)
            return E_PULLED_KNOB

        else:
            self.on_failed(req)
            return E_FAILED

    def on_entry(self, req):
        req.c_sock.send("""You can see the close door.""".encode())

    def on_trigger(self, req):
        return req.pull_trigger()

    def on_pulled_knob(self, req):
        pass

    def on_failed(self, req):
        pass
