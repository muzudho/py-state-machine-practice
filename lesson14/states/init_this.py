from lesson14_projects.pen.data.const import E_IS, E_OVER, E_WAS, MSG_IS, MSG_WAS


class InitThisState:
    def update(self, req):

        self.on_entry(req)

        # 入力
        msg = self.on_trigger(req)

        # 分岐
        if msg == MSG_IS:
            self.on_is(req)
            return E_IS

        elif msg == MSG_WAS:
            self.on_was(req)
            return E_WAS

        else:
            self.on_over(req)
            return E_OVER

    def on_entry(self, req):
        # 現在位置の表示
        state_path_str = "/".join(req.state_path)
        req.c_sock.send(f"""State path={state_path_str}""".encode())

    def on_trigger(self, req):
        return req.pull_trigger()

    def on_over(self, req):
        pass

    def on_was(self, req):
        pass

    def on_is(self, req):
        pass
