"""State Generator"""
from lesson14_projects.pen.data.const import A, INIT, IS, PEN, THIS
from lesson14.states.init import InitState
from lesson14.states.init_this import InitThisState
from lesson14.states.init_this_is import InitThisIsState
from lesson14.states.init_this_is_a import InitThisIsAState
from lesson14.states.pen import PenState


# ステートを使い回すのではなく、アクセスするたびに ステートの生成を実行しなおせるよう、ラムダ関数を返します
pen_state_gen_v14 = {
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
