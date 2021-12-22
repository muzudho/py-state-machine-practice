# Lesson 17

前回の Lesson16n3 ではコードの自動生成まで進みましたが、定数を使っていないのはイケていません。  
定数の定義も自動生成するようにしましょう  

ただし今回はコードを生成するだけで、生成したコードを実行するところまではやりません  

wcsc_const.py:  

```python
INIT = 'Init'
LOGIN = 'Login'
LOBBY = 'Lobby'
LOGOUT = 'Logout'
REPLY = 'Reply'
# 以下略
```

👆 step1 では、 Pythonのdict（これはOrderedDictではありません）でデータ化した定数（`const_dict.py`）を元に、定数を定義した Pythonスクリプトを自動生成します  

init.py:  

```python
class InitState():

    def update(self, req):

        # 入力
        msg = req.pull_trigger()

        # 分岐
        if True:
            return ['Init', 'Login']

        else:
            raise ValueError(f"Unexpected msg:{msg}")
```

👆 step2 では、 Pythonスクリプトファイルを自動生成します。このとき、定数に置き換えられるところは置き換えます  


# Run

実行前に 以下のフォルダーが既に作成されていれば、削除してください  

* `lesson17/step1n2_auto_const`
* `lesson17/step2n2_auto_state`


```shell
python.exe -m lesson17.main_house3_step1_const
python.exe -m lesson17.main_pen_step1_const
python.exe -m lesson17.main_wcsc_step1_const

python.exe -m lesson17.main_wcsc_step2
```
