# Lesson 20

Lesson 19 で作った `transition-pen.json` ファイルを読み取ってみましょう  

# Example - House

## Set up

```shell
# Windows
python.exe -m lesson20.transition_py_maker_v20 "lesson19_data/auto_gen/house3n2-transition2.json" "lesson20_data/auto_gen/house3n2-transition3.json" --output_default_format "lesson20_data/auto_gen/house3n2-transition3-default-fomat.json"
#                                              -------------------------------------------------- --------------------------------------------------
#                                              Input (.json)                                      Output (.json)
```

# Example - Pen

## Set up

```shell
# Windows
python.exe -m lesson20.transition_py_maker_v20 "lesson19_data/auto_gen/pen-transition.json" "lesson20_data/auto_gen/pen-transition.json" --output_default_format "lesson20_data/auto_gen/pen-transition-default-fomat.json"
#                                              -------------------------------------------- --------------------------------------------
#                                              Input (.json)                                 Output (.json)
```

# Example - WCSC

## Set up

```shell
# Windows
python.exe -m lesson20.transition_py_maker_v20 "lesson19_data/auto_gen/wcsc-transition.json" "lesson20_data/auto_gen/wcsc-transition.json" --output_default_format "lesson20_data/auto_gen/wcsc-transition-default-fomat.json"
#                                              --------------------------------------------- ---------------------------------------------
#                                              Input (.json)                                  Output (.json)
```

## Run

```shell
python.exe -m lesson20.main_house3n2_step2_transition3
python.exe -m lesson20.main_pen_step2_transition
python.exe -m lesson20.main_wcsc_step2_transition
```
