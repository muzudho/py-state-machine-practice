def create_init(state):
    def __on_entry(req):
        pass

    def __on_trigger(req):
        return req.pull_trigger()

    def __on_login(req):
        pass

    state.on_entry = __on_entry
    state.on_trigger = __on_trigger
    state.on_login = __on_login
    return state
