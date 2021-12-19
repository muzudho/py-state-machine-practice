from lesson14_data.step1_pen_const import E_PEN, E_PIN, E_OVER, MSG_PEN, MSG_PIN


class InitThisIsAState:
    def update(self, req):
        # 現在位置の表示
        state_path_str = "/".join(req.state_path)
        req.c_sock.send(f"[English] State path={state_path_str}".encode())

        # 入力
        msg = req.pull_trigger()

        # 分岐
        if msg == MSG_PEN:
            return E_PEN

        elif msg == MSG_PIN:
            return E_PIN

        else:
            return E_OVER
