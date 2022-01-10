# Lesson 21

トランジション設定ファイル（JSON形式）から、 `pen_transition.py` ファイルを逆生成してみましょう  

# Example House

## Set up

```shell
# Windows
python.exe -m lesson21.transition_py_maker_v21 "lesson19_projects/house3n2/data/auto_gen/transition2.json" "lesson21_projects/house3n2/data/auto_gen/transition2.py" "lesson18_projects.house3.data.auto_gen.const" "house3n2_transition2_py_dict"
#                                              ----------------------------------------------------------- --------------------------------------------------------- ---------------------------------------------- ------------------------------
#                                              Input (.json)                                                Output (.json)                                            Output (import statement)                     Output (Variable name)
```

# Example: Pen

## Set up

```shell
# Windows
python.exe -m lesson21.transition_py_maker_v21 "lesson19_projects/pen/data/auto_gen/transition.json" "lesson21_projects/pen/data/auto_gen/transition.py" "lesson18_projects.pen.data.auto_gen.const" "pen_transition_py_dict"
#                                              ----------------------------------------------------- --------------------------------------------------- ------------------------------------------- ------------------------
#                                              Input (.json)                                         Output (.json)                                       Output (import statement)                   Output (Variable name)
```

# Example: Wcsc

## Set up

```shell
# Windows
python.exe -m lesson21.transition_py_maker_v21 "lesson19_projects/wcsc/data/auto_gen/transition.json" "lesson21_projects/wcsc/data/auto_gen/transition.py" "lesson18_projects.wcsc.data.auto_gen.const" "wcsc_transition_py_dict"
#                                              ------------------------------------------------------ ---------------------------------------------------- -------------------------------------------- -------------------------
#                                              Input (.json)                                           Output (.json)                                       Output (import statement)                   Output (Variable name)
```
