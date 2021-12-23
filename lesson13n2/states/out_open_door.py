from lesson12_data.step1_house3_const import E_ENTER, MSG_ENTER, E_FAILED


class OutOpenDoorState:
    def update(self, req):

        self.on_entry(req)

        # 入力
        msg = self.on_trigger(req)

        # 外に居ます。 'Enter' とメッセージを送ってくるのが正解です
        if msg == MSG_ENTER:
            self.on_enter(req)
            return E_ENTER

        else:
            self.on_failed(req)
            return E_FAILED

    def on_entry(self, req):
        req.c_sock.send("You can see the open door.".encode())

    def on_trigger(self, req):
        return req.pull_trigger()

    def on_enter(self, req):
        pass

    def on_failed(self, req):
        pass
