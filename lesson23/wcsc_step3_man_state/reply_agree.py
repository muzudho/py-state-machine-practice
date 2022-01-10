from lesson23_projects.wcsc.data.auto_gen.const import E_START


def create_reply_agree(state):
    def __on_entry(req):
        # 現在位置の表示
        state_path_str = "/".join(req.state_path)
        req.context.c_sock.send(f"[WCSC] State path={state_path_str}".encode())

    def __on_trigger(req):
        return req.pull_trigger()

    def __on_start(req):
        pass

    state.on_entry = __on_entry
    state.on_trigger = __on_trigger
    state.on_start = __on_start
    return state
