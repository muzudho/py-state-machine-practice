from lesson14.step1_const_conf_pen_v1 import E_OVER, E_THAT, E_THIS, MSG_THAT, MSG_THIS


class InitState:
    @classmethod
    def is_verbose(clazz):
        return False

    def update(self, req):
        # 現在位置の表示
        state_path_str = "/".join(req.state_path)
        req.c_sock.send(
            f"""[English] "This" "is" "a" "pen" と１単語を１行ずつ打鍵してください。
State path={state_path_str}""".encode()
        )

        # 入力
        msg = req.pull_trigger()

        if InitState.is_verbose():
            req.c_sock.send(f"[English] msg={msg}".encode())

        # 分岐
        if msg == MSG_THIS:

            if InitState.is_verbose():
                req.c_sock.send(f"[English] This分岐".encode())

            return E_THIS

        elif msg == MSG_THAT:

            if InitState.is_verbose():
                req.c_sock.send(f"[English] That分岐".encode())

            return E_THAT

        else:

            if InitState.is_verbose():
                req.c_sock.send(f"[English] Over分岐".encode())

            return E_OVER
