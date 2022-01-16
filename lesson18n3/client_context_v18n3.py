class ClientContextV18n3:
    def __init__(self, c_sock=None, pull_trigger=None):
        self._c_sock = c_sock
        self._fn_pull_trigger = pull_trigger

    @property
    def c_sock(self):
        """Client socket"""
        return self._c_sock

    def pull_trigger(self):
        """Execte Trigger"""
        return self._fn_pull_trigger()
