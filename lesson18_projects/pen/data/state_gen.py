"""State Generator"""
from lesson18_projects.pen.auto_gen.data.const import A, INIT, IS, PEN, THIS

# State wrapper
from lesson18_projects.pen.code.states.init import create_init
from lesson18_projects.pen.code.states.init_this import create_init_this
from lesson18_projects.pen.code.states.init_this_is import create_init_this_is
from lesson18_projects.pen.code.states.init_this_is_a import create_init_this_is_a
from lesson18_projects.pen.code.states.pen import create_pen

# State
from lesson18_projects.pen.auto_gen.code.states.init_this_is_a import InitThisIsAState
from lesson18_projects.pen.auto_gen.code.states.init_this_is import InitThisIsState
from lesson18_projects.pen.auto_gen.code.states.init_this import InitThisState
from lesson18_projects.pen.auto_gen.code.states.init import InitState
from lesson18_projects.pen.auto_gen.code.states.pen import PenState


# ステートを使い回すのではなく、アクセスするたびに ステートの生成を実行しなおせるよう、ラムダ関数を返します
pen_state_gen_v18 = {
    INIT: {
        "": lambda: create_init(InitState()),
        THIS: {
            "": lambda: create_init_this(InitThisState()),
            IS: {
                "": lambda: create_init_this_is(InitThisIsState()),
                A: {
                    "": lambda: create_init_this_is_a(InitThisIsAState()),
                },
            },
        },
    },
    PEN: lambda: create_pen(PenState()),
}
