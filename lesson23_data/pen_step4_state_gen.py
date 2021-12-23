"""State Generator"""
from lesson18_data.step1n2_auto_const.pen_const import A, INIT, IS, PEN, THIS

# Lesson 18 State wrapper
from lesson18.pen_step3_man_state.init import create_init_state
from lesson18.pen_step3_man_state.init_this import create_init_this_state
from lesson18.pen_step3_man_state.init_this_is import create_init_this_is_state
from lesson18.pen_step3_man_state.init_this_is_a import create_init_this_is_a_state
from lesson18.pen_step3_man_state.pen import create_pen_state

# Lesson 23
from lesson23.pen_step2n2_auto_state.init_this_is_a import InitThisIsAState
from lesson23.pen_step2n2_auto_state.init_this_is import InitThisIsState
from lesson23.pen_step2n2_auto_state.init_this import InitThisState
from lesson23.pen_step2n2_auto_state.init import InitState
from lesson23.pen_step2n2_auto_state.pen import PenState


# ステートを使い回すのではなく、アクセスするたびに ステートの生成を実行しなおせるよう、ラムダ関数を返します
pen_state_gen_v23 = {
    INIT: {
        "": lambda: create_init_state(InitState()),
        THIS: {
            "": lambda: create_init_this_state(InitThisState()),
            IS: {
                "": lambda: create_init_this_is_state(InitThisIsState()),
                A: {
                    "": lambda: create_init_this_is_a_state(InitThisIsAState()),
                },
            },
        },
    },
    PEN: lambda: create_pen_state(PenState()),
}
