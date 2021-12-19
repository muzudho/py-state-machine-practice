"""State Generator"""
from lesson12_data.step1_house3_const import (
    MY_ROOM,
    OUT,
    CLOSE_DOOR,
    OPEN_DOOR,
    STAIRS,
)
from lesson12n3.states.my_room import MyRoomState
from lesson12n3.states.out import OutState
from lesson12n3.states.out_close_door import OutCloseDoorState
from lesson12n3.states.out_open_door import OutOpenDoorState
from lesson12n3.states.stairs import StairsState


# ステートを使い回すのではなく、アクセスするたびに ステートの生成を実行しなおせるよう、ラムダ関数を返します
house3_state_gen = {
    OUT: lambda: OutState(),
    CLOSE_DOOR: lambda: OutCloseDoorState(),
    OPEN_DOOR: lambda: OutOpenDoorState(),
    STAIRS: lambda: StairsState(),
    MY_ROOM: lambda: MyRoomState(),
}
