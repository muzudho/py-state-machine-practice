"""State Generator"""
from lesson11_data.step1_house_v1_const import MY_ROOM, OUT, STAIRS
from lesson11n2.states.my_room import MyRoomState
from lesson11n2.states.out import OutState
from lesson11n2.states.stairs import StairsState


# ステートを使い回すのではなく、アクセスするたびに ステートの生成を実行しなおせるよう、ラムダ関数を返します
house_state_gen = {
    MY_ROOM: lambda: MyRoomState(),
    OUT: lambda: OutState(),
    STAIRS: lambda: StairsState(),
}
