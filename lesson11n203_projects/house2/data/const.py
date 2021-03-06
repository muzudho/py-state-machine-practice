# States
# ------
#
# "ステート定数": "ステートマシン図のノード名"
# 本レッスンではノード名を PascalCase にします（エッジと被らないように）

OUT = "Out"
STAIRS = "Stairs"
MY_ROOM = "MyRoom"

# Edges
# -----
#
# "エッジ定数": "ステートマシン図のエッジ名"
# 本レッスンではエッジ名を snake_case にします（ノード名と被らないように）
# ディクショナリーのキーとして State と被らないように頭に E_ を付けます

E_OPENED = "Opened"
E_UP = "Up"
E_SITTING_DOWN = "Sitting down"
E_FAILED = "Failed"

# Actions
# -------
#
# 任意の文字列ですが、値が State や Edge と突合するなら、それを使い回してください

MSG_OPEN = "Open"
MSG_UP = "Up"
MSG_SIT_DOWN = "Sit down"
