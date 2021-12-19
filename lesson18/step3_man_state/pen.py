from lesson18_data.step1n2_auto_const.pen_const import E_OVER
from lesson18.step2n2_auto_state.pen import PenState

__is_verbose = True


def create_pen_state():
    obj = PenState()

    def __on_entry(req):
        # 現在位置の表示
        state_path_str = "/".join(req.state_path)
        req.c_sock.send(
            f"""[English] State path={state_path_str}
おつかれさまでした""".encode()
        )

    obj.on_entry = __on_entry

    def __on_trigger(req):
        """入力待機を無しにしてそのまま抜けます"""

        return E_OVER

    obj.on_trigger = __on_trigger

    def __on_over(req):
        """クライアントを終了させます"""
        req.c_sock.send("quit".encode())

    obj.on_over = __on_over

    return obj
