# Lesson 21

トランジション設定ファイル（JSON形式）から、 `pen_transition.py` ファイルを逆生成してみましょう  

# Example House

## Set up

```shell
# Windows
python.exe -m lesson21.transition_py_maker_v21 "lesson19_data/auto_gen/house3n2-transition2.json" "lesson21_data/auto_gen/step2_house3n2_transition2.py" "lesson18_data.auto_gen.house3_const" "house3n2_transition2_py_dict"
#                                          -------------------------------------------------- ------------------------------------------------------ ------------------------------------- ------------------------------
#                                          Input (.json)                                      Output (.json)                                          Output (import statement)               Output (Variable name)
```

## Run

```shell
python.exe -m lesson21.main_house3n2_step2_transition2
```

# Example: Pen

## Set up

```shell
# Windows
python.exe -m lesson21.transition_py_maker_v21 "lesson19_data/auto_gen/pen-transition.json" "lesson21_data/auto_gen/step2_pen_transition.py" "lesson18_data.auto_gen.pen_const" "pen_transition_py_dict"
#                                          -------------------------------------------- ------------------------------------------------ ---------------------------------- ------------------------
#                                          Input (.json)                                 Output (.json)                                   Output (import statement)          Output (Variable name)
```

## Run

```shell
python.exe -m lesson21.main_pen_step2_transition
```

# Example: Wcsc

## Set up

```shell
# Windows
python.exe -m lesson21.transition_py_maker_v21 "lesson19_data/auto_gen/wcsc-transition.json" "lesson21_data/auto_gen/step2_wcsc_transition.py" "lesson18_data.auto_gen.wcsc_const" "wcsc_transition_py_dict"
#                                          --------------------------------------------- ------------------------------------------------- ----------------------------------- -------------------------
#                                          Input (.json)                                 Output (.json)                                    Output (import statement)           Output (Variable name)
```

## Run

```shell
python.exe -m lesson21.main_wcsc_step2_transition
```
