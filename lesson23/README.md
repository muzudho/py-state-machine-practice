# Lesson23

Lesson18 をさらに発展させ、  
Pythonのdict（これはOrderedDictではありません）を経由せず、JSON（OrderedDictを使います）でデータ化した定数（`const_dict.py`）を元に、Lesson14と同等のPythonスクリプトのルーチン（状態のスクリプト）を自動生成しましょう  

# house3n2

Lesson13n2 と同じ動きをするものを作りましょう  

## Set up

```shell
# Example (House)
python.exe -m lesson22.const_py_maker "lesson22_data/step1-house3-const.json" "lesson23_data/auto_gen/house3n2_const.py"
#                                     --------------------------------------- ----------------------------------------------------
#                                     入力ファイル (.json)                      出力ファイル (.py)

python.exe -m lesson23.state_py_maker "lesson22_data/step1-house3-const.json" "lesson20_data/auto_gen/house3n2-transition3.json" "lesson23_data.auto_gen.house3n2_const" "lesson23/house3n2/auto_gen/states"
```

## Run

Server start:  

```shell
python.exe -m lesson23.main_house3n2_server
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

# Pen

## Set up

```shell
# Example (Pen)
python.exe -m lesson22.const_py_maker "lesson22_data/step1-pen-const.json" "lesson23_data/auto_gen/pen_const.py"
#                                     ------------------------------------ -----------------------------------------------
#                                     入力ファイル (.json)                   出力ファイル (.py)

python.exe -m lesson23.state_py_maker "lesson22_data/step1-pen-const.json" "lesson20_data/auto_gen/pen-transition.json" "lesson18_data.auto_gen.pen_const" "lesson23/pen/auto_gen/states"
```

## Run

Server start:  

```shell
python.exe -m lesson23.main_pen_server
```

Client start:  

```shell
python.exe -m lesson09.main
```

Input:  

```shell
This
is
a
pen
q
```

# wcsc
## Set up

```shell
# Example (WCSC)
python.exe -m lesson22.const_py_maker "lesson22_data/step1-wcsc-const.json" "lesson23_data/auto_gen/wcsc_const.py"
#                                     ------------------------------------- ------------------------------------------------
#                                     入力ファイル (.json)                    出力ファイル (.py)

python.exe -m lesson23.state_py_maker "lesson22_data/step1-wcsc-const.json" "lesson20_data/auto_gen/wcsc-transition.json" "lesson23_data.auto_gen.wcsc_const" "lesson23/wcsc/auto_gen/states"
```

## Run

Server start:  

```shell
python.exe -m lesson23.main_wcsc_server
```

Client start:  

```shell
python.exe -m lesson09.main
```

Input:  

```plain
login
incorrect

login
ok
logout
completed

login
ok
game_summary
reject
reject

game_summary
agree
start
move
move_echo
game_over_floodgate

login
q
```
