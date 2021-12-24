"""State Generator"""
from lesson18_data.step1n2_auto_const.pen_const import A, INIT, IS, PEN, THIS

# State (Lesson 23)
from lesson23.pen_step2n2_auto_state.init_this_is_a import InitThisIsAState
from lesson23.pen_step2n2_auto_state.init_this_is import InitThisIsState
from lesson23.pen_step2n2_auto_state.init_this import InitThisState
from lesson23.pen_step2n2_auto_state.init import InitState
from lesson23.pen_step2n2_auto_state.pen import PenState

# State wrapper (Lesson 18)
from lesson24.pen_step3_man_state.init import create_init
from lesson24.pen_step3_man_state.init_this import create_init_this
from lesson24.pen_step3_man_state.init_this_is import create_init_this_is
from lesson24.pen_step3_man_state.init_this_is_a import create_init_this_is_a
from lesson24.pen_step3_man_state.pen import create_pen


# ステートを使い回すのではなく、アクセスするたびに ステートの生成を実行しなおせるよう、ラムダ関数を返します
pen_state_gen_v24 = {
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
