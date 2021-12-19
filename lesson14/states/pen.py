from lesson14_data.step1_const_pen import E_OVER


class PenState:
    def update(self, req):
        # 現在位置の表示
        state_path_str = "/".join(req.state_path)
        req.c_sock.send(
            f"""[English] State path={state_path_str}
おつかれさまでした""".encode()
        )

        # 入力なし
        # msg = req.pull_trigger()

        # 分岐なし
        return E_OVER
