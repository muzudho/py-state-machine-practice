from lesson12_projects.house3.data.const import MSG_SIT_DOWN, E_FAILED, E_SITTING_DOWN


class MyroomState:
    def update(self, req):

        self.on_entry(req)

        # 入力
        msg = self.on_trigger(req)

        # 'Sit down' とメッセージを送ってくるのが正解です
        if msg == MSG_SIT_DOWN:
            self.on_sitting_down(req)
            return E_SITTING_DOWN

        else:
            self.on_failed(req)
            return E_FAILED

    def on_entry(self, req):
        req.c_sock.send("You can see the your room.".encode())

    def on_trigger(self, req):
        return req.pull_trigger()

    def on_sitting_down(self, req):
        req.c_sock.send(
            """Clear!
Please push q key to quit.""".encode()
        )

    def on_failed(self, req):
        pass
