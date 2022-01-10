"""State Generator"""
from lesson18_projects.pen.data.auto_gen.const import A, INIT, IS, PEN, THIS

# Lesson 18 State wrapper
from lesson18.pen_step3_man_state.init import create_init
from lesson18.pen_step3_man_state.init_this import create_init_this
from lesson18.pen_step3_man_state.init_this_is import create_init_this_is
from lesson18.pen_step3_man_state.init_this_is_a import create_init_this_is_a
from lesson18.pen_step3_man_state.pen import create_pen

# Lesson 23
from lesson23.pen.auto_gen.states.init_this_is_a import InitThisIsAState
from lesson23.pen.auto_gen.states.init_this_is import InitThisIsState
from lesson23.pen.auto_gen.states.init_this import InitThisState
from lesson23.pen.auto_gen.states.init import InitState
from lesson23.pen.auto_gen.states.pen import PenState


# ステートを使い回すのではなく、アクセスするたびに ステートの生成を実行しなおせるよう、ラムダ関数を返します
pen_state_gen_v23 = {
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
