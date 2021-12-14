from lesson18.step2n2_auto.init_this_is import InitThisIsState

__is_verbose = True


def create_init_this_is_state():
    obj = InitThisIsState()

    def __on_entry(req):
        # 現在位置の表示
        state_path_str = "/".join(req.state_path)
        req.c_sock.send(f"[English] State path={state_path_str}".encode())

    obj.on_entry = __on_entry
    return obj
