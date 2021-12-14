from lesson18.step2n2_auto_state.init_this_is_a import InitThisIsAState

__is_verbose = True


def create_init_this_is_a_state():
    obj = InitThisIsAState()

    def __on_entry(req):
        # 現在位置の表示
        state_path_str = "/".join(req.state_path)
        req.c_sock.send(f"[English] State path={state_path_str}".encode())

    obj.on_entry = __on_entry
    return obj
