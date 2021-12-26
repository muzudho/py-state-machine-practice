from lesson23_data.step1n2_auto_const.wcsc_const import E_COMPLETED


def create_lobby_logout(state):
    def __on_entry(req):
        # 現在位置の表示
        state_path_str = "/".join(req.state_path)
        req.context.c_sock.send(f"[WCSC] State path={state_path_str}".encode())

    def __on_trigger(req):
        return req.pull_trigger()

    def __on_completed(req):
        pass

    state.on_entry = __on_entry
    state.on_trigger = __on_trigger
    state.on_completed = __on_completed
    return state
