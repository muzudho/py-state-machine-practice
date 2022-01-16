# Lesson 17

定数を定義した `const.json` を前もって用意し、 `const.py` を自動出力してみましょう。  
ただし今回はコードを生成するだけで、生成したコードを実行するところまではやりません  

const.json:  

```json
{
    "OUT": "Out",
    "CLOSE_DOOR": "CloseDoor",
    "OPEN_DOOR": "OpenDoor",
    "～以下略～": "",
}
```

const.py:  

```python
house3_const_doc = {
    "OUT": "Out",  # Out/CloseKnob
    "CLOSE_DOOR": "CloseDoor",
    "OPEN_DOOR": "OpenDoor",
    # 以下略
}
```

# const.json コーディング規約

* 1. キーと値は 全単射にしてください
* 2. 大文字と小文字は区別します

## ステート名

```json
    "ステート定数": "ステートマシン図のノード名",
    "OUT": "Out",
```

👆 本レッスンではノード名を PascalCase にします（エッジと被らないように）  

## エッジ名

```json
    "エッジ定数": "ステートマシン図のエッジ名",
    "E_TURNED_KNOB": "turned_knob",
```

👆 本レッスンではエッジ名を snake_case にします（ノード名と被らないように）  
ディクショナリーのキーとして State と被らないように頭に E_ を付けます  

## 任意文字列（メッセージ名）

```json
    "メッセージ定数": "任意の文字列",
    "MSG_TURN_KNOB": "Turn knob",
```

👆 任意の文字列ですが、値が State や Edge と突合するなら、それを使い回してください

# 出力する ～.py

init.py:  

```python
class InitState():

    def update(self, req):

        # 入力
        msg = req.pull_trigger()

        # 分岐
        if True:
            return ['Init', 'Login']

        else:
            raise ValueError(f"Unexpected msg:{msg}")
```

👆 step2 では、 Pythonスクリプトファイルを自動生成します。このとき、定数に置き換えられるところは置き換えます  

# Example - House

## Run

実行前に 以下のフォルダーが既に作成されていれば、削除してください  

* `lesson17_projects/house3/auto_gen`

```shell
# Windows
python.exe -m lesson17.main_house3_step1_const "lesson17_projects/house3/conf.toml"
#                                              ------------------------------------
#                                              設定ファイル (TOML形式)
```

# Example - Pen

## Run

実行前に 以下のフォルダーが既に作成されていれば、削除してください  

* `lesson17_projects/pen/auto_gen`

```shell
# Windows
python.exe -m lesson17.main_pen_step1_const "lesson17_projects/pen/conf.toml"
#                                           ---------------------------------
#                                           設定ファイル (TOML形式)
```

# Example - WCSC

## Run

実行前に 以下のフォルダーが既に作成されていれば、削除してください  

* `lesson17_projects/wcsc/auto_gen`

```shell
python.exe -m lesson17.main_wcsc_step1_const "lesson17_projects/wcsc/conf.toml"
#                                            ----------------------------------
#                                            設定ファイル (TOML形式)

python.exe -m lesson17.main_wcsc_step2 "lesson17_projects/wcsc/conf.toml"
#                                      ----------------------------------
#                                      設定ファイル
```
