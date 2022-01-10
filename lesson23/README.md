# Lesson23

Lesson18 をさらに発展させ、  
Pythonのdict（これはOrderedDictではありません）を経由せず、JSON（OrderedDictを使います）でデータ化した定数（`const_dict.py`）を元に、Lesson14と同等のPythonスクリプトのルーチン（状態のスクリプト）を自動生成しましょう  

# house3n2

Lesson13n2 と同じ動きをするものを作りましょう  

## Set up

```shell
# Example (House)
python.exe -m lesson18n2.const_py_maker "lesson18n2_projects/house3/data/const.json" "lesson23_projects/house3n2/auto_gen/data/const.py"
#                                       -------------------------------------------- ---------------------------------------------------
#                                       入力ファイル (.json)                          出力ファイル (.py)

python.exe -m lesson23.state_py_maker "lesson18n2_projects/house3/data/const.json" "lesson20_projects/house3n2/auto_gen/data/transition3.json" "lesson23_projects.house3n2.auto_gen.data.const" "lesson23_projects/house3n2/auto_gen/code/states"
#                                     -------------------------------------------- ----------------------------------------------------------- ------------------------------------------------ -------------------------------------------------
#                                     定数入力ファイル (.json)                       状態遷移入力ファイル (.py)                                    import文に書く                                    出力ディレクトリー
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
python.exe -m lesson18n2.const_py_maker "lesson18n2_projects/pen/data/const.json" "lesson23_projects/pen/auto_gen/data/const.py"
#                                       ----------------------------------------- ----------------------------------------------
#                                       入力ファイル (.json)                        出力ファイル (.py)

python.exe -m lesson23.state_py_maker "lesson18n2_projects/pen/data/const.json" "lesson20_projects/pen/auto_gen/data/transition.json" "lesson18_projects.pen.auto_gen.data.const" "lesson23_projects/pen/auto_gen/code/states"
#                                     ----------------------------------------- ----------------------------------------------------- ------------------------------------------- --------------------------------------------
#                                     定数入力ファイル (.json)                    状態遷移入力ファイル (.py)                              import文に書く                               出力ディレクトリー
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
python.exe -m lesson18n2.const_py_maker "lesson18n2_projects/wcsc/data/const.json" "lesson23_projects/wcsc/auto_gen/data/const.py"
#                                       ------------------------------------------ -----------------------------------------------
#                                       入力ファイル (.json)                        出力ファイル (.py)

python.exe -m lesson23.state_py_maker "lesson18n2_projects/wcsc/data/const.json" "lesson20_projects/wcsc/auto_gen/data/transition.json" "lesson23_projects.wcsc.auto_gen.data.const" "lesson23_projects/wcsc/auto_gen/code/states"
#                                     ------------------------------------------ ----------------------------------------------------- --------------------------------------------- ---------------------------------------------
#                                     定数入力ファイル (.json)                     状態遷移入力ファイル (.py)                              import文に書く                                 出力ディレクトリー
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
