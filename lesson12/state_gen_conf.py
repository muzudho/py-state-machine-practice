"""State Generator"""
from lesson12.step1_const_conf_house import (
    MY_ROOM,
    OUT,
    OUT_CLOSE_DOOR,
    OUT_OPEN_DOOR,
    STAIRS,
)
from lesson12.states.my_room import MyRoomState
from lesson12.states.out import OutState
from lesson12.states.out_close_door import OutCloseDoorState
from lesson12.states.out_open_door import OutOpenDoorState
from lesson12.states.stairs import StairsState


# ステートを使い回すのではなく、アクセスするたびに ステートの生成を実行しなおせるよう、ラムダ関数を返します
state_gen = {
    OUT: lambda: OutState(),
    OUT_CLOSE_DOOR: lambda: OutCloseDoorState(),
    OUT_OPEN_DOOR: lambda: OutOpenDoorState(),
    STAIRS: lambda: StairsState(),
    MY_ROOM: lambda: MyRoomState(),
}
