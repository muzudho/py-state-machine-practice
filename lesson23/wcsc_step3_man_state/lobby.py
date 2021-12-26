from lesson23_data.step1n2_auto_const.wcsc_const import E_GAME_SUMMARY, E_LOGOUT


def create_lobby(state):
    def __on_entry(req):
        # 現在位置の表示
        state_path_str = "/".join(req.state_path)
        req.context.c_sock.send(f"[WCSC] State path={state_path_str}".encode())

    def __on_trigger(req):
        return req.pull_trigger()

    def __on_game_summary(req):
        pass

    def __on_logout(req):
        pass

    state.on_entry = __on_entry
    state.on_trigger = __on_trigger
    state.on_game_summary = __on_game_summary
    state.on_logout = __on_logout
    return state
