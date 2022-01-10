"""State Generator"""
from lesson12_projects.house3.data.const import (
    MY_ROOM,
    OUT,
    CLOSE_DOOR,
    OPEN_DOOR,
    STAIRS,
)
from lesson12n3.states.myroom import MyroomState
from lesson12n3.states.out import OutState
from lesson12n3.states.out_closedoor import OutClosedoorState
from lesson12n3.states.out_opendoor import OutOpendoorState
from lesson12n3.states.stairs import StairsState


# ステートを使い回すのではなく、アクセスするたびに ステートの生成を実行しなおせるよう、ラムダ関数を返します
house3_state_gen = {
    OUT: lambda: OutState(),
    CLOSE_DOOR: lambda: OutClosedoorState(),
    OPEN_DOOR: lambda: OutOpendoorState(),
    STAIRS: lambda: StairsState(),
    MY_ROOM: lambda: MyroomState(),
}
