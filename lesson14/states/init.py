from lesson14_data.step1_pen_const import E_OVER, E_THAT, E_THIS, MSG_THAT, MSG_THIS


class InitState:
    @classmethod
    def is_verbose(clazz):
        return True

    def update(self, req):

        self.on_entry(req)

        # 入力
        msg = self.on_trigger(req)

        if InitState.is_verbose():
            req.c_sock.send(f"[English] msg={msg}".encode())

        # 分岐
        if msg == MSG_THIS:

            if InitState.is_verbose():
                req.c_sock.send(f"[English] This分岐".encode())

            self.on_this(req)
            return E_THIS

        elif msg == MSG_THAT:

            if InitState.is_verbose():
                req.c_sock.send(f"[English] That分岐".encode())

            self.on_that(req)
            return E_THAT

        else:

            if InitState.is_verbose():
                req.c_sock.send(f"[English] Over分岐".encode())

            self.on_over(req)
            return E_OVER

    def on_entry(self, req):
        # 現在位置の表示
        state_path_str = "/".join(req.state_path)
        req.c_sock.send(
            f"""[English] "This" "is" "a" "pen" と１単語を１行ずつ打鍵してください。
State path={state_path_str}""".encode()
        )

    def on_trigger(self, req):
        return req.pull_trigger()

    def on_over(self, req):
        pass

    def on_that(self, req):
        pass

    def on_this(self, req):
        pass
