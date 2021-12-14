from lesson18.step1n2_auto_const.pen import E_THIS
from lesson18.step2n2_auto_state.init import InitState

__is_verbose = True


def create_init_state():
    obj = InitState()

    def __on_entry(req):
        """現在位置の表示"""
        state_path_str = "/".join(req.state_path)
        req.c_sock.send(
            f"""[English] "This" "is" "a" "pen" と１単語を１行ずつ打鍵してください。
State path={state_path_str}""".encode()
        )

    obj.on_entry = __on_entry

    def __on_trigger(req):
        msg = req.pull_trigger()

        # Edge名に変換
        if msg == "This":
            return E_THIS

        return msg

    obj.on_trigger = __on_trigger

    def __on_this(req):
        if __is_verbose:
            req.c_sock.send(f"[English] This分岐".encode())

    obj.on_this = __on_this

    def __on_that(req):
        if __is_verbose:
            req.c_sock.send(f"[English] That分岐".encode())

    obj.on_that = __on_that

    def __on_over(req):
        if __is_verbose:
            req.c_sock.send(f"[English] Over分岐".encode())

    obj.on_over = __on_over

    return obj
