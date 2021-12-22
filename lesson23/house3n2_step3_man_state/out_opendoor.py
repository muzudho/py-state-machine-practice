def create_out_open_door(state):
    def __on_entry(self, req):
        pass

    # def __on_trigger(self, req):
    #    pass

    def __on_enter(self, req):
        pass

    def __on_failed(self, req):
        pass

    state.on_entry = __on_entry
    # state.on_trigger = __on_trigger
    state.on_enter = __on_enter
    state.on_failed = __on_failed
    return state
