# States
# ------
#
# "ステート定数": "ステートマシン図のノード名"
# 本レッスンではノード名を PascalCase にします（エッジと被らないように）

INIT = "Init"
THIS = "This"
IS = "Is"
A = "A"
PEN = "Pen"

# Edges
# -----
#
# "エッジ定数": "ステートマシン図のエッジ名"
# 本レッスンではエッジ名を snake_case にします（ノード名と被らないように）
# ディクショナリーのキーとして State と被らないように頭に E_ を付けます

E_THAT = "that"
E_THIS = "this"
E_WAS = "was"
E_IS = "is"
E_AN = "an"
E_A = "a"
E_PIN = "pin"
E_PEN = "pen"
E_OVER = "over"  # 以上

# Actions
# -------
#
# 任意の文字列ですが、値が State や Edge と突合するなら、それを使い回してください

MSG_THAT = "That"
MSG_THIS = "This"
MSG_WAS = "was"
MSG_IS = "is"
MSG_AN = "an"
MSG_A = "a"
MSG_PIN = "pin"
MSG_PEN = "pen"
