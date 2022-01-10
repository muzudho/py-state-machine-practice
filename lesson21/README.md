# Lesson 21

トランジション設定ファイル（JSON形式）から、 `pen_transition.py` ファイルを逆生成してみましょう  

# Example House

## Set up

```shell
# Windows
python.exe -m lesson21.transition_py_maker_v21 "lesson18n2_projects/house3/data/const.json" "lesson19_projects/house3n2/auto_gen/data/transition2.json" "lesson21_projects/house3n2/auto_gen/data/transition2.py" "lesson18_projects.house3.auto_gen.data.const" "house3n2_transition2_py_dict"
#                                              -------------------------------------------- ----------------------------------------------------------- --------------------------------------------------------- ---------------------------------------------- ------------------------------
#                                              定数定義入力ファイル (.json)                   状態遷移定義入力ファイル(.json)                                Output (.json)                                            Output (import statement)                     Output (Variable name)
```

# Example: Pen

## Set up

```shell
# Windows
python.exe -m lesson21.transition_py_maker_v21 "lesson18n2_projects/pen/data/const.json" "lesson19_projects/pen/auto_gen/data/transition.json" "lesson21_projects/pen/auto_gen/data/transition.py" "lesson18_projects.pen.auto_gen.data.const" "pen_transition_py_dict"
#                                              ----------------------------------------- ----------------------------------------------------- --------------------------------------------------- ------------------------------------------- ------------------------
#                                              定数定義入力ファイル (.json)                状態遷移定義入力ファイル(.json)                          Output (.json)                                       Output (import statement)                   Output (Variable name)
```

# Example: Wcsc

## Set up

```shell
# Windows
python.exe -m lesson21.transition_py_maker_v21 "lesson18n2_projects/wcsc/data/const.json" "lesson19_projects/wcsc/auto_gen/data/transition.json" "lesson21_projects/wcsc/auto_gen/data/transition.py" "lesson18_projects.wcsc.auto_gen.data.const" "wcsc_transition_py_dict"
#                                              ------------------------------------------ ------------------------------------------------------ ---------------------------------------------------- -------------------------------------------- -------------------------
#                                              定数定義入力ファイル (.json)                 状態遷移定義入力ファイル(.json)                           Output (.json)                                       Output (import statement)                   Output (Variable name)
```
