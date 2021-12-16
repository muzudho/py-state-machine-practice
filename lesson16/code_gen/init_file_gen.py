import os


def gen_init_file():
    try:
        # `step2n2_auto` フォルダーが無ければ作る
        os.makedirs("lesson16/step2n2_auto")
    except FileExistsError:
        # 既存なら無視
        pass

    # `init.py` ファイルを作成します
    path = "lesson16/step2n2_auto/init.py"
    with open(path, "w") as f:
        f.write(
            """from lesson15.step1_const_conf_wcsc_v1 import E_OVER

class InitState():

    def update(self, req):
        # 何もせず終わります
        return E_OVER

"""
        )
