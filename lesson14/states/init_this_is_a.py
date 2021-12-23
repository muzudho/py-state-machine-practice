from lesson14_data.step1_pen_const import E_PEN, E_PIN, E_OVER, MSG_PEN, MSG_PIN


class InitThisIsAState:
    def update(self, req):

        self.on_entry(req)

        # 入力
        msg = self.on_trigger(req)

        # 分岐
        if msg == MSG_PEN:
            self.on_pen(req)
            return E_PEN

        elif msg == MSG_PIN:
            self.on_pin(req)
            return E_PIN

        else:
            self.on_over(req)
            return E_OVER

    def on_entry(self, req):
        # 現在位置の表示
        state_path_str = "/".join(req.state_path)
        req.c_sock.send(f"[English] State path={state_path_str}".encode())

    def on_trigger(self, req):
        return req.pull_trigger()

    def on_over(self, req):
        pass

    def on_pin(self, req):
        pass

    def on_pen(self, req):
        pass
