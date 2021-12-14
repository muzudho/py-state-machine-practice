# States
# ------
#
# "ステート定数": "ステートマシン図のノード名"
# 本レッスンではノード名を PascalCase にします（エッジと被らないように）

OUT = "Out"  # Out/CloseKnob
if OUT:  # インデントを付けてるだけ
    CLOSE_DOOR = "CloseDoor"
    OPEN_DOOR = "OpenDoor"
STAIRS = "Stairs"
MY_ROOM = "My room"

# Edges
# -----
#
# "エッジ定数": "ステートマシン図のエッジ名"
# 本レッスンではエッジ名を snake_case にします（ノード名と被らないように）
# ディクショナリーのキーとして State と被らないように頭に E_ を付けます

E_TURNED_KNOB = "TurnedKnob"
E_PULLED_KNOB = "PulledKnob"
E_ENTER = "Enter"
E_UP = "Up"
E_SITTING_DOWN = "Sitting down"
E_FAILED = "Failed"

# Actions
# -------
#
# 任意の文字列ですが、値が State や Edge と突合するなら、それを使い回してください

MSG_TURN_KNOB = "Turn knob"
MSG_PULL_KNOB = "Pull knob"
MSG_ENTER = "Enter"
MSG_UP = "Up"
MSG_SIT_DOWN = "Sit down"
