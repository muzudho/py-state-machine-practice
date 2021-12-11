"""State Generator"""
from lesson12.keywords import MY_ROOM, OUT, STAIRS
from lesson12.states.my_room import MyRoomState
from lesson12.states.out import OutState
from lesson12.states.stairs import StairsState


# ステートを使い回すのではなく、アクセスするたびに ステートの生成を実行しなおせるよう、ラムダ関数を返します
state_gen = {
    OUT: lambda: OutState(),
    STAIRS: lambda: StairsState(),
    MY_ROOM: lambda: MyRoomState(),
}
