"""State Generator"""
from lesson12_projects.house3.data.const import MY_ROOM, CLOSE_DOOR, OPEN_DOOR, OUT, STAIRS

# State
from lesson18_projects.house3.auto_gen.code.states1.myroom import MyroomState
from lesson18_projects.house3.auto_gen.code.states1.out_closedoor import OutClosedoorState
from lesson18_projects.house3.auto_gen.code.states1.out_opendoor import OutOpendoorState
from lesson18_projects.house3.auto_gen.code.states1.out import OutState
from lesson18_projects.house3.auto_gen.code.states1.stairs import StairsState

# State wrapper
from lesson23_projects.house3n2.code.states2.myroom import create_myroom
from lesson23_projects.house3n2.code.states2.out_closedoor import create_out_closedoor
from lesson23_projects.house3n2.code.states2.out_opendoor import create_out_opendoor
from lesson23_projects.house3n2.code.states2.out import create_out
from lesson23_projects.house3n2.code.states2.stairs import create_stairs


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
