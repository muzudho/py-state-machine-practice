"""State Generator"""
from lesson18.keywords import A, INIT, IS, PEN, THIS
from lesson18.states.init import InitState
from lesson18.states.init_this import InitThisState
from lesson18.states.init_this_is import InitThisIsState
from lesson18.states.init_this_is_a import InitThisIsAState
from lesson18.states.pen import PenState


# ステートを使い回すのではなく、アクセスするたびに ステートの生成を実行しなおせるよう、ラムダ関数を返します
state_gen = {
    INIT: {
        "": lambda: InitState(),
        THIS: {
            "": lambda: InitThisState(),
            IS: {
                "": lambda: InitThisIsState(),
                A: {
                    "": lambda: InitThisIsAState(),
                },
            },
        },
    },
    PEN: lambda: PenState(),
}
