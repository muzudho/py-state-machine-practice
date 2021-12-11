# Lesson13

前回の Lesson12 のサンプルでは、  

transigion_conf.py:  

```python
transition = {
    OUT: {
        E_TURNED_KNOB: OUT_CLOSE_DOOR,
        E_FAILED: OUT,
    },
    OUT_CLOSE_DOOR: {
        E_PULLED_KNOB: OUT_OPEN_DOOR,
        E_FAILED: OUT,
    },
    OUT_OPEN_DOOR: {
        E_ENTER: STAIRS,
        E_FAILED: OUT,
    },
    STAIRS: {
        E_UP: MY_ROOM,
        E_FAILED: OUT,
    },
    MY_ROOM: {
        E_SITTING_DOWN: MY_ROOM,
        E_FAILED: OUT,
    }
}
```

👆 上図のようにフラットに設定しましたが、  

transigion_conf.py:

```python
transition = {
    OUT: {
        '': {
            E_TURNED_KNOB: [OUT, CLOSE_DOOR],
            E_FAILED: [OUT],
        },
        CLOSE_DOOR: {
            E_PULLED_KNOB: [OUT, OPEN_DOOR],
            E_FAILED: [OUT],
        },
        OPEN_DOOR: {
            E_ENTER: [STAIRS],
            E_FAILED: [OUT],
        },
    },
    STAIRS: {
        E_UP: [MY_ROOM],
        E_FAILED: [OUT],
    },
    MY_ROOM: {
        E_SITTING_DOWN: [MY_ROOM],
        E_FAILED: [OUT],
    }
}
```

👆 ステート（State）とサブステート（Sub-state）を分けて 大きな状態遷移、小さな状態遷移といった　強調を  
付けた方が 人間の目の検索能力の負担を軽くできるかもしれません。  

また、フラットなものを階層化した影響として、`OUT_CLOSE_DOOR` ではなく `[OUT, CLOSE_DOOR]` とリストで書く変更が出ます  

state_gen_conf.py:  

```python
state_gen = {
    OUT: {
        '': lambda: OutState(),
        CLOSE_DOOR: lambda: OutCloseDoorState(),
        OPEN_DOOR: lambda: OutOpenDoorState(),
    },
    STAIRS: lambda: StairsState(),
    MY_ROOM: lambda: MyRoomState(),
}
```

👆 state_gen にも変更が及びます  

## Run

Server start:  

```shell
python.exe -m lesson13.main
```

Client start:  

```shell
python.exe -m lesson09.main
```
