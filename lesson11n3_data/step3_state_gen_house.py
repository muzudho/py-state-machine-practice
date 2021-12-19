"""State Generator"""
from lesson11n3_data.step1_const_house_v2 import MY_ROOM, OUT, STAIRS
from lesson11n3.states.my_room import MyRoomState
from lesson11n3.states.out import OutState
from lesson11n3.states.stairs import StairsState


# ステートを使い回すのではなく、アクセスするたびに ステートの生成を実行しなおせるよう、ラムダ関数を返します
state_gen_house = {
    MY_ROOM: lambda: MyRoomState(),
    OUT: lambda: OutState(),
    STAIRS: lambda: StairsState(),
}
