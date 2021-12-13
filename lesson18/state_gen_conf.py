"""State Generator"""
from lesson18.step1n2_auto.const import A, E_THIS, INIT, IS, PEN, THIS
from lesson18.step2n2_auto.init import InitState
from lesson18.step2n2_auto.init_this import InitThisState
from lesson18.step2n2_auto.init_this_is import InitThisIsState
from lesson18.step2n2_auto.init_this_is_a import InitThisIsAState
from lesson18.step2n2_auto.pen import PenState

__is_verbose = True


def __create_init_state():
    obj = InitState()

    def __on_entry(req):
        # 現在位置の表示
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

    def __on_this(req):  # TODO __on_this
        if __is_verbose:
            req.c_sock.send(f"[English] This分岐".encode())

    obj.on_this = __on_this

    def __on_that(req):  # TODO __on_that
        if __is_verbose:
            req.c_sock.send(f"[English] That分岐".encode())

    obj.on_that = __on_that

    def __on_over(req):  # TODO __on_that
        if __is_verbose:
            req.c_sock.send(f"[English] Over分岐".encode())

    obj.on_over = __on_over

    return obj


def __create_init_this_state():
    obj = InitThisState()

    def __on_entry(req):
        # 現在位置の表示
        state_path_str = "/".join(req.state_path)
        req.c_sock.send(f"""State path={state_path_str}""".encode())

    obj.on_entry = __on_entry
    return obj


def __create_init_this_is_state():
    obj = InitThisIsState()

    def __on_entry(req):
        # 現在位置の表示
        state_path_str = "/".join(req.state_path)
        req.c_sock.send(f"[English] State path={state_path_str}".encode())

    obj.on_entry = __on_entry
    return obj


def __create_init_this_is_a_state():
    obj = InitThisIsAState()

    def __on_entry(req):
        # 現在位置の表示
        state_path_str = "/".join(req.state_path)
        req.c_sock.send(f"[English] State path={state_path_str}".encode())

    obj.on_entry = __on_entry
    return obj


def __create_pen_state():
    obj = PenState()

    def __on_entry(req):
        # 現在位置の表示
        state_path_str = "/".join(req.state_path)
        req.c_sock.send(
            f"""[English] State path={state_path_str}
おつかれさまでした""".encode()
        )

    obj.on_entry = __on_entry

    # TODO 入力待機をなしにしたい

    return obj


# ステートを使い回すのではなく、アクセスするたびに ステートの生成を実行しなおせるよう、ラムダ関数を返します
state_gen = {
    INIT: {
        "": lambda: __create_init_state(),
        THIS: {
            "": lambda: __create_init_this_state(),
            IS: {
                "": lambda: __create_init_this_is_state(),
                A: {
                    "": lambda: __create_init_this_is_a_state(),
                },
            },
        },
    },
    PEN: lambda: __create_pen_state(),
}
