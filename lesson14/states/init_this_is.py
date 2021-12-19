from lesson14_data.step1_const_pen import E_A, E_AN, E_OVER, MSG_A, MSG_AN


class InitThisIsState:
    def update(self, req):
        # 現在位置の表示
        state_path_str = "/".join(req.state_path)
        req.c_sock.send(f"[English] State path={state_path_str}".encode())

        # 入力
        msg = req.pull_trigger()

        # 分岐
        if msg == MSG_A:
            return E_A

        elif msg == MSG_AN:
            return E_AN

        else:
            return E_OVER
