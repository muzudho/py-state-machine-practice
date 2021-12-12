from lesson18.keywords import E_IS, E_OVER, E_WAS, MSG_IS, MSG_WAS


class InitThisState:
    def update(self, req):
        # 現在位置の表示
        state_path_str = "/".join(req.state_path)
        req.c_sock.send(f"""State path={state_path_str}""".encode())

        # 入力
        msg = req.pull_trigger()

        # 分岐
        if msg == MSG_IS:
            return E_IS

        elif msg == MSG_WAS:
            return E_WAS

        else:
            return E_OVER
