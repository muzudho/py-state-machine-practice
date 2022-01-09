# Lesson 22

JSONファイルでデータ化した定数の定義（`const.json`）から、定数を定義したPythonスクリプト（`const.py`）を出力しましょう  

TODO JSONをdict等へ変換

# Run

```shell
python.exe -m lesson22.main_pen_step1_const
python.exe -m lesson22.main_wcsc_step1_const

# Example (House)
python.exe -m lesson22.const_py_maker "lesson22_data/step1-house3-const.json" "lesson22_data/step1n2_auto_const/house3_const.py"
#                                     --------------------------------------- --------------------------------------------------
#                                     入力ファイル                              出力ファイル

# Example (Pen)
python.exe -m lesson22.const_py_maker "lesson22_data/step1-pen-const.json" "lesson22_data/step1n2_auto_const/pen_const.py"
#                                     ------------------------------------ --------------------------------------------------
#                                     入力ファイル                           出力ファイル
```
