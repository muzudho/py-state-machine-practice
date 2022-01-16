# Lesson18

Lesson17で行ったコードの自動生成を発展させ、  
doc構造でデータ化した定数（`const.py`）を元に、Lesson14と同等のPythonスクリプトのルーチン（状態のスクリプト）を自動生成しましょう  

# Example - House

# Example - Pen

## Set up

実行前に 以下のフォルダーが既に作成されていれば、不要なファイルが残っているかもしれませんので削除してください

- `lesson18_projects/auto_gen`

```shell
python.exe -m lesson18.main_pen_step2 "lesson18_projects/pen/conf.toml"
#                                     ---------------------------------
#                                     設定ファイル
```

## Run

Server start:  

```shell
python.exe -m lesson18.main_pen_step3 "lesson18_projects/pen/conf.toml"
#                                     ---------------------------------
#                                     設定ファイル
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

# Example - Wcsc

```shell
python.exe -m lesson18.state_py_generator_v17 "lesson18_projects/wcsc/conf.toml" "input_const_file" "transition_file" "output_states_dir" "const"
#                                             ---------------------------------- ------------------ ----------------- ------------------- -------
#                                             1.                                 2.                 3.                4.                  5.
# 1. 設定ファイル（TOML形式）
# 2. 定数の読込ファイル（JSON形式）へのパスが書いてあるプロパティのキー
# 3. 状態遷移の読込ファイル（JSON形式）へのパスが書いてあるプロパティのキー
# 4. 書込先ディレクトリーへのパスが書いてあるプロパティのキー
# 5. [import_module]テーブル下の、import文のモジュールへのパスが入ったプロパティの名前
```
