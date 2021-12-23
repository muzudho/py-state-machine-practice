from lesson14_data.step1_pen_const import E_OVER


class PenState:
    def update(self, req):

        self.on_entry(req)

        # 入力
        msg = self.on_trigger(req)

        # 分岐なし
        self.on_over(req)
        return E_OVER

    def on_entry(self, req):
        # 現在位置の表示
        state_path_str = "/".join(req.state_path)
        req.c_sock.send(
            f"""[English] State path={state_path_str}
おつかれさまでした""".encode()
        )

    def on_trigger(self, req):
        # 入力なし
        return None

    def on_over(self, req):
        pass
