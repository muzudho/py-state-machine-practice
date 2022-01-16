from lesson17_projects.wcsc.auto_gen.data.const import E_AGREE, E_REJECT


def create_reply(state):
    def __on_entry(req):
        # 現在位置の表示
        state_path_str = "/".join(req.state_path)
        req.context.c_sock.send(f"[WCSC] State path={state_path_str}".encode())

    def __on_trigger(req):
        return req.pull_trigger()

    def __on_agree(req):
        pass

    def __on_reject(req):
        pass

    state.on_entry = __on_entry
    state.on_trigger = __on_trigger
    state.on_agree = __on_agree
    state.on_reject = __on_reject
    return state
