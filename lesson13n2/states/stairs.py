from lesson12_data.step1_house3_const import MSG_UP, E_FAILED, E_UP


class StairsState:
    def update(self, req):

        self.on_entry(req)

        # 入力
        msg = self.on_trigger(req)

        # `Up` とメッセージを送ってくるのが正解です
        if msg == MSG_UP:
            self.on_up(req)
            return E_UP

        else:
            self.on_failed(req)
            return E_FAILED

    def on_entry(self, req):
        req.c_sock.send("You can see the stairs.".encode())

    def on_trigger(self, req):
        return req.pull_trigger()

    def on_up(self, req):
        pass

    def on_failed(self, req):
        pass
