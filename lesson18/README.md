# Lesson18

Lesson17で行ったコードの自動生成を発展させ、  
Pythonのdict（これはOrderedDictではありません）でデータ化した定数（`const_dict.py`）を元に、Lesson14と同等のPythonスクリプトのルーチン（状態のスクリプト）を自動生成しましょう  

# Example - Pen

## Set up

実行前に 以下のフォルダーが既に作成されていれば、不要なファイルが残っているかもしれませんので削除してください

- `lesson18_projects/data/auto_gen`

```shell
python.exe -m lesson18.main_pen_step1
python.exe -m lesson18.main_pen_step2
```

## Run

Server start:  

```shell
python.exe -m lesson18.main_pen_step3
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
