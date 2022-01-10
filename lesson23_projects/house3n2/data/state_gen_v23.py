"""State Generator"""
from lesson12_projects.house3.data.const import MY_ROOM, CLOSE_DOOR, OPEN_DOOR, OUT, STAIRS

# Lesson 23 State
from lesson23.house3n2.auto_gen.states.myroom import MyroomState
from lesson23.house3n2.auto_gen.states.out_closedoor import OutClosedoorState
from lesson23.house3n2.auto_gen.states.out_opendoor import OutOpendoorState
from lesson23.house3n2.auto_gen.states.out import OutState
from lesson23.house3n2.auto_gen.states.stairs import StairsState

# Lesson 23 State wrapper
from lesson23.house3n2_step3_man_state.myroom import create_myroom
from lesson23.house3n2_step3_man_state.out_closedoor import create_out_closedoor
from lesson23.house3n2_step3_man_state.out_opendoor import create_out_opendoor
from lesson23.house3n2_step3_man_state.out import create_out
from lesson23.house3n2_step3_man_state.stairs import create_stairs


# ステートを使い回すのではなく、アクセスするたびに ステートの生成を実行しなおせるよう、ラムダ関数を返します
house3n2_state_gen_v23 = {
    MY_ROOM: {
        "": lambda: create_myroom(MyroomState()),
    },
    OUT: {
        "": lambda: create_out(OutState()),
        CLOSE_DOOR: lambda: create_out_closedoor(OutClosedoorState()),
        OPEN_DOOR: lambda: create_out_opendoor(OutOpendoorState()),
    },
    STAIRS: lambda: create_stairs(StairsState()),
}
