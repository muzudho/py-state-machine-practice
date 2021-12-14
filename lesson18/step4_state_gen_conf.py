"""State Generator"""
from lesson18.step1n2_auto.const import A, INIT, IS, PEN, THIS
from lesson18.step3_man.init import create_init_state
from lesson18.step3_man.init_this import create_init_this_state
from lesson18.step3_man.init_this_is import create_init_this_is_state
from lesson18.step3_man.init_this_is_a import create_init_this_is_a_state
from lesson18.step3_man.pen import create_pen_state


# ステートを使い回すのではなく、アクセスするたびに ステートの生成を実行しなおせるよう、ラムダ関数を返します
state_gen = {
    INIT: {
        "": lambda: create_init_state(),
        THIS: {
            "": lambda: create_init_this_state(),
            IS: {
                "": lambda: create_init_this_is_state(),
                A: {
                    "": lambda: create_init_this_is_a_state(),
                },
            },
        },
    },
    PEN: lambda: create_pen_state(),
}
