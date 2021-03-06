# (1) キーと値は 全単射にしてください
# (2) 大文字と小文字は区別します
house3_const_doc = {
    # States
    # ------
    #
    # "ステート定数": "ステートマシン図のノード名"
    # 本レッスンではノード名を PascalCase にします（エッジと被らないように）
    "OUT": "Out",  # Out/CloseKnob
    "CLOSE_DOOR": "CloseDoor",
    "OPEN_DOOR": "OpenDoor",
    "STAIRS": "Stairs",
    "MY_ROOM": "MyRoom",
    # Edges
    # -----
    #
    # "エッジ定数": "ステートマシン図のエッジ名"
    # 本レッスンではエッジ名を snake_case にします（ノード名と被らないように）
    # ディクショナリーのキーとして State と被らないように頭に E_ を付けます
    "E_TURNED_KNOB": "turned_knob",
    "E_PULLED_KNOB": "pulled_knob",
    "E_ENTER": "enter",
    "E_UP": "up",
    "E_SITTING_DOWN": "sitting_down",
    "E_FAILED": "failed",
    # Actions
    # -------
    #
    # 任意の文字列ですが、値が State や Edge と突合するなら、それを使い回してください
    "MSG_TURN_KNOB": "Turn knob",
    "MSG_PULL_KNOB": "Pull knob",
    "MSG_ENTER": "Enter",
    "MSG_UP": "Up",
    "MSG_SIT_DOWN": "Sit down",
}
