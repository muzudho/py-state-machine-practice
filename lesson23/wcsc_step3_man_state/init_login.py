from lesson23_projects.wcsc.auto_gen.data.const import E_INCORRECT, E_OK


def create_init_login(state):
    def __on_entry(req):
        # 現在位置の表示
        state_path_str = "/".join(req.state_path)
        req.context.c_sock.send(f"[WCSC] State path={state_path_str}".encode())

    def __on_trigger(req):
        return req.pull_trigger()

    def __on_ok(req):
        pass

    def __on_incorrect(req):
        pass

    state.on_entry = __on_entry
    state.on_trigger = __on_trigger
    state.on_ok = __on_ok
    state.on_incorrect = __on_incorrect
    return state
