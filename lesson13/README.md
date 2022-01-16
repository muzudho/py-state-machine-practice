# Lesson13

前回の Lesson12 のサンプルでは、  

transigion.json:  

```json
        "Out": {
            "turned_knob": "CloseDoor",
            "failed": "Out"
        },
        "CloseDoor": {
            "pulled_knob": "OpenDoor",
            "failed": "Out"
        },
        "OpenDoor": {
            "enter": "Stairs",
            "failed": "Out"
        },
        "Stairs": {
            "up": "MyRoom",
            "failed": "Out"
        },
        "MyRoom": {
            "sitting_down": "MyRoom",
            "failed": "Out"
        }
```

👆 上図のようにフラットに設定しましたが、  

transigion.json:

```json
        "Out": {
            "turned_knob": ["Out", "CloseDoor"],
            "failed": ["Out"],
            "CloseDoor": {
                "pulled_knob": ["Out", "OpenDoor"],
                "failed": ["Out"]
            },
            "OpenDoor": {
                "enter": ["stairs"],
                "failed": ["Out"]
            }
        },
        "stairs": {
            "up": ["MyRoom"],
            "failed": ["Out"]
        },
        "MyRoom": {
            "sitting_down": ["MyRoom"],
            "failed": ["Out"]
        }
```

👆 ステート（State）とサブステート（Sub-state）を分けて 大きな状態遷移、小さな状態遷移といった　強調を  
付けた方が 人間の目の検索能力の負担を軽くできるかもしれません。  

また、フラットなものを階層化した影響として、`CLOSE_DOOR` ではなく `[OUT, CLOSE_DOOR]` とリストで書く変更が出ます  

state_gen_conf.py:  

```python
house3_state_gen = {
    OUT: {
        '': lambda: OutState(),
        CLOSE_DOOR: lambda: OutClosedoorState(),
        OPEN_DOOR: lambda: OutOpendoorState(),
    },
    STAIRS: lambda: StairsState(),
    MY_ROOM: lambda: MyroomState(),
}
```

👆 state_gen にも変更が及びます  

## Run

Server start:  

```shell
python.exe -m lesson13.main "lesson13_projects/house3/conf.toml"
#                           ------------------------------------
#                           設定ファイル
```

Client start:  

```shell
python.exe -m lesson09.main
```

Input:  

```plain
Turn knob
Pull knob
Enter
Up
Sit down
q
```
