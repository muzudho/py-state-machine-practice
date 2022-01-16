# Lesson 21

トランジション設定ファイル（JSON形式）から、 `pen_transition.py` ファイルを逆生成してみましょう  

# Example House

## Set up

```shell
# Windows
python.exe -m lesson10021.transition_py_maker_v21 "lesson17_projects/house3/data/const.json" "lesson10019_projects/house3n2/auto_gen/data/transition2.json" "lesson10021_projects/house3n2/auto_gen/data/transition2.py" "lesson17_projects.house3.auto_gen.data.const" "house3n2_transition2_doc"
#                                                 ------------------------------------------ ----------------------------------------------------------- ------------------------------------------------------------ ---------------------------------------------- ------------------------------
#                                                 定数定義入力ファイル (.json)                   状態遷移定義入力ファイル(.json)                                Output (.py)                                              Output (import statement)                     Output (Variable name)
```

# Example: Pen

## Set up

```shell
# Windows
python.exe -m lesson10021.transition_py_maker_v21 "lesson17_projects/pen/data/const.json" "lesson10019_projects/pen/auto_gen/data/transition.json" "lesson10021_projects/pen/auto_gen/data/transition.py" "lesson17_projects.pen.auto_gen.data.const" "pen_transition_doc_v19"
#                                                 --------------------------------------- ----------------------------------------------------- ------------------------------------------------------ ------------------------------------------- ------------------------
#                                                 定数定義入力ファイル (.json)                状態遷移定義入力ファイル(.json)                          Output (.json)                                       Output (import statement)                   Output (Variable name)
```

# Example: Wcsc

## Set up

```shell
# Windows
python.exe -m lesson10021.transition_py_maker_v21 "lesson17_projects/wcsc/data/const.json" "lesson10019_projects/wcsc/auto_gen/data/transition.json" "lesson10021_projects/wcsc/auto_gen/data/transition.py" "lesson17_projects.wcsc.auto_gen.data.const" "wcsc_transition_doc_v19"
#                                                 ---------------------------------------- ------------------------------------------------------ ------------------------------------------------------- -------------------------------------------- -------------------------
#                                                 定数定義入力ファイル (.json)                 状態遷移定義入力ファイル(.json)                           Output (.json)                                       Output (import statement)                   Output (Variable name)
```
