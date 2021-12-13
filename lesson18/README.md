# Lesson18

Lesson14のコードをベースに、Lesson17の実行ファイルを使ってコードを自動生成し差し替えていきましょう  

## Build

実行前に 以下のフォルダーが既に作成されていれば、削除してください

- `lesson18/step1n2_auto`
- `lesson18/step2n2_auto`

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
