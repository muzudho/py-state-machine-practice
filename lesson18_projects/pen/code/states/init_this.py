__is_verbose = True


def create_init_this(state):
    def __on_entry(req):
        # 現在位置の表示
        state_path_str = "/".join(req.state_path)
        req.context.c_sock.send(
            f"""[English] 次は "is" と打鍵してください。
State path={state_path_str}""".encode()
        )

    def __on_is(req):
        if __is_verbose:
            req.context.c_sock.send(f"[English] is分岐".encode())

    state.on_entry = __on_entry
    state.on_is = __on_is
    return state
