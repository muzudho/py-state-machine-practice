"""State Generator"""
from lesson11n203_projects.house2.data.const import MY_ROOM, OUT, STAIRS
from lesson11n203.states.myroom import MyroomState
from lesson11n203.states.out import OutState
from lesson11n203.states.stairs import StairsState


# ステートを使い回すのではなく、アクセスするたびに ステートの生成を実行しなおせるよう、ラムダ関数を返します
house2_state_gen = {
    MY_ROOM: lambda: MyroomState(),
    OUT: lambda: OutState(),
    STAIRS: lambda: StairsState(),
}
