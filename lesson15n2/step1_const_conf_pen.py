# States
# ------
#
# ディクショナリーのキーとして Edge と被らないように PascalCase にします

INIT = "Init"
if INIT:
    THIS = "This"
    if THIS:  # インデントを付けてるだけ
        IS = "Is"
        if IS:
            A = "A"

PEN = "Pen"

# Actions
# -------

MSG_THAT = "That"
MSG_THIS = "This"
MSG_WAS = "was"
MSG_IS = "is"
MSG_AN = "an"
MSG_A = "a"
MSG_PIN = "pin"
MSG_PEN = "pen"

# Edges
# -----
#
# ディクショナリーのキーとして State と被らないように頭に snake_case にします

E_THAT = "that"
E_THIS = "this"
E_WAS = "was"
E_IS = "is"
E_AN = "an"
E_A = "a"
E_PIN = "pin"
E_PEN = "pen"
E_OVER = "over"  # 以上
