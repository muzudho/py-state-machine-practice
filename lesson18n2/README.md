# Lesson 18-2

JSONファイルでデータ化した定数の定義（`const.json`）から、定数を定義したPythonスクリプト（`const.py`）を出力しましょう  

# Run

```shell
# Example (House)
python.exe -m lesson18n2.const_py_maker "lesson18n2_data/house3-const.json" "lesson18n2_data/auto_gen/house3_const.py"
#                                       ----------------------------------- ------------------------------------------
#                                       入力ファイル (.json)                  出力ファイル (.py)

# Example (Pen)
python.exe -m lesson18n2.const_py_maker "lesson18n2_data/pen-const.json" "lesson18n2_data/auto_gen/pen_const.py"
#                                       -------------------------------- ---------------------------------------
#                                       入力ファイル                       出力ファイル

# Example (WCSC)
python.exe -m lesson18n2.const_py_maker "lesson18n2_data/wcsc-const.json" "lesson18n2_data/auto_gen/wcsc_const.py"
#                                       --------------------------------- ----------------------------------------
#                                       入力ファイル                        出力ファイル
```
