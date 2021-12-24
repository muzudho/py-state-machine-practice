__is_verbose = True


def create_init_this_is_a(state):
    def __on_entry(req):
        # 現在位置の表示
        state_path_str = "/".join(req.state_path)
        req.context.c_sock.send(f"[English] State path={state_path_str}".encode())

    def __on_trigger(req):
        msg = req.context.pull_trigger()
        return msg

    state.on_entry = __on_entry
    state.on_trigger = __on_trigger
    return state
