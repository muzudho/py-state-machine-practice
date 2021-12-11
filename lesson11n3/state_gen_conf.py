"""State Generator"""
from lesson11n3.keywords import MY_ROOM, OUT, STAIRS
from lesson11n3.states.my_room import MyRoomState
from lesson11n3.states.out import OutState
from lesson11n3.states.stairs import StairsState


# ステートを使い回すのではなく、アクセスするたびに ステートの生成を実行しなおせるよう、ラムダ関数を返します
state_gen = {
    MY_ROOM: lambda: MyRoomState(),
    OUT: lambda: OutState(),
    STAIRS: lambda: StairsState(),
}