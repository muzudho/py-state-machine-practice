# Lesson13

`transigion_conf.py` に、ステートマシンを終了させる出口を指定できるようにしましょう  

```python
transition_conf_data = {
    OUT: {
        E_TURNED_KNOB: [OUT, CLOSE_DOOR],
        E_FAILED: [OUT],
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
        E_SITTING_DOWN: None,
        E_FAILED: [OUT],
    }
}
```

👆 OUT の MY_ROOM の E_SITTING_DOWN に紐づく値を None にしました。  
次の状態パスが None のとき、ステートマシンを終了するものとします  

最後で `input()` は必ずブロックして止まっているので、自動的には終了しません。  

## Run

Server start:  

```shell
python.exe -m lesson13n2.main
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
