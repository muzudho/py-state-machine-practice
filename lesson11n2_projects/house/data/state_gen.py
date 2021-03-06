"""State Generator"""
from lesson11_projects.house.data.const import MY_ROOM, OUT, STAIRS
from lesson11n2.states.myroom import MyroomState
from lesson11n2.states.out import OutState
from lesson11n2.states.stairs import StairsState


# ステートを使い回すのではなく、アクセスするたびに ステートの生成を実行しなおせるよう、ラムダ関数を返します
# TODO Lesson23 の pen_step4_state_gen を参考に、変更したい
house_state_gen = {
    MY_ROOM: lambda: MyroomState(),
    OUT: lambda: OutState(),
    STAIRS: lambda: StairsState(),
}
