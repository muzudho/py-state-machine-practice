class Request():
    def __init__(self, state_path, c_sock=None, pull_trigger=None):
        self._state_path = state_path
        self._c_sock = c_sock
        self._fn_pull_trigger = pull_trigger

    @property
    def state_path(self):
        """list"""
        return self._state_path

    @property
    def c_sock(self):
        """Client socket"""
        return self._c_sock

    def pull_trigger(self):
        """Execte Trigger"""
        return self._fn_pull_trigger()
