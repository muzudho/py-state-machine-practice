from lesson17_projects.pen.auto_gen.data.const import E_OVER

__is_verbose = True


def create_pen(state):
    def __on_entry(req):
        # 現在位置の表示
        state_path_str = "/".join(req.state_path)
        req.context.c_sock.send(
            f"""[English] State path={state_path_str}
おつかれさまでした""".encode()
        )

    def __on_trigger(req):
        """入力待機を無しにしてそのまま抜けます"""
        return E_OVER

    def __on_over(req):
        """クライアントを終了させます"""
        req.context.c_sock.send("quit".encode())

    state.on_entry = __on_entry
    state.on_trigger = __on_trigger
    state.on_over = __on_over
    return state
