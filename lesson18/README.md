# Lesson18

Lesson17で行ったコードの自動生成を発展させ、Lesson14と同等のPythonスクリプトのルーチン（定型処理）を自動生成しましょう  

## Build

実行前に 以下のフォルダーが既に作成されていれば、不要なファイルが残っているかもしれませんので削除してください

- `lesson18/step1n2_auto_const`
- `lesson18/step2n2_auto_state`

```shell
python.exe -m lesson18.code_gen.main_step1
python.exe -m lesson18.code_gen.main_step2
```

## Run

Server start:  

```shell
python.exe -m lesson18.main
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
```
