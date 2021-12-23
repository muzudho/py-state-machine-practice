from lesson23_data.step1n2_auto_const.wcsc_const import E_INCORRECT, E_OK


def create_init_login(state):
    def __on_entry(req):
        pass

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
