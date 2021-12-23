from lesson14_data.step1_pen_const import E_A, E_AN, E_OVER, MSG_A, MSG_AN


class InitThisIsState:
    def update(self, req):

        self.on_entry(req)

        # 入力
        msg = self.on_trigger(req)

        # 分岐
        if msg == MSG_A:
            self.on_a(req)
            return E_A

        elif msg == MSG_AN:
            self.on_an(req)
            return E_AN

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

    def on_an(self, req):
        pass

    def on_a(self, req):
        pass
