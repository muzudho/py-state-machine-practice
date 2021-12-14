from lesson18.step2n2_auto_state.init_this import InitThisState

__is_verbose = True


def create_init_this_state():
    obj = InitThisState()

    def __on_entry(req):
        # 現在位置の表示
        state_path_str = "/".join(req.state_path)
        req.c_sock.send(
            f"""[English] 次は "is" と打鍵してください。
State path={state_path_str}""".encode()
        )

    obj.on_entry = __on_entry

    def __on_is(req):
        if __is_verbose:
            req.c_sock.send(f"[English] is分岐".encode())

    obj.on_is = __on_is

    return obj
