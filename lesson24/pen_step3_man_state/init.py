from lesson18_data.auto_gen.pen_const import E_THIS

__is_verbose = True


def create_init(state):
    def __on_entry(req):
        """現在位置の表示"""
        state_path_str = "/".join(req.state_path)
        req.context.c_sock.send(
            f"""[English] "This" "is" "a" "pen" と１単語を１行ずつ打鍵してください。
State path={state_path_str}""".encode()
        )

    def __on_trigger(req):
        msg = req.context.pull_trigger()

        # Edge名に変換
        if msg == "This":
            return E_THIS

        return msg

    def __on_this(req):
        if __is_verbose:
            req.context.c_sock.send(f"[English] This分岐".encode())

    def __on_that(req):
        if __is_verbose:
            req.context.c_sock.send(f"[English] That分岐".encode())

    def __on_over(req):
        if __is_verbose:
            req.context.c_sock.send(f"[English] Over分岐".encode())

    state.on_entry = __on_entry
    state.on_trigger = __on_trigger
    state.on_this = __on_this
    state.on_that = __on_that
    state.on_over = __on_over
    return state
