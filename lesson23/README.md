# Lesson23

Lesson18 で作ったファイルを動かしましょう  

# house3n2

## Run

Server start:  

```shell
python.exe -m lesson23.main_house3n2_server "lesson23_projects/house3n2/conf.toml"
#                                           --------------------------------------
#                                           設定ファイル
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

## Run

Server start:  

```shell
python.exe -m lesson23.main_pen_server "lesson23_projects/pen/conf.toml"
#                                      ---------------------------------
#                                      設定ファイル
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

## Run

Server start:  

```shell
python.exe -m lesson23.main_wcsc_server "lesson23_projects/house3n2/conf.toml"
#                                       --------------------------------------
#                                       設定ファイル
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
