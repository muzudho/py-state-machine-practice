"""State Generator"""
from lesson12_data.step1_house3_const import MY_ROOM, CLOSE_DOOR, OPEN_DOOR, OUT, STAIRS

# Lesson 23 State
from lesson23.house3n2_step2n2_auto_state.myroom import MyRoomState
from lesson23.house3n2_step2n2_auto_state.out_closedoor import OutCloseDoorState
from lesson23.house3n2_step2n2_auto_state.out_opendoor import OutOpenDoorState
from lesson23.house3n2_step2n2_auto_state.out import OutState
from lesson23.house3n2_step2n2_auto_state.stairs import StairsState

# Lesson 23 State wrapper
from lesson23.house3n2_step3_man_state.myroom import create_my_room
from lesson23.house3n2_step3_man_state.out_closedoor import create_out_close_door
from lesson23.house3n2_step3_man_state.out_opendoor import create_out_open_door
from lesson23.house3n2_step3_man_state.out import create_out
from lesson23.house3n2_step3_man_state.stairs import create_stairs


# ステートを使い回すのではなく、アクセスするたびに ステートの生成を実行しなおせるよう、ラムダ関数を返します
house3n2_state_gen = {
    MY_ROOM: {
        "": lambda: create_my_room(MyRoomState()),
        CLOSE_DOOR: lambda: create_out_close_door(OutCloseDoorState),
        OPEN_DOOR: lambda: create_out_open_door(OutOpenDoorState),
    },
    OUT: lambda: create_out(OutState()),
    STAIRS: lambda: create_stairs(StairsState()),
}
