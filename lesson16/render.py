import os


class Render:
    @classmethod
    def is_verbose(clazz):
        return True

    def __init__(self):
        pass

    def run(self):
        try:
            # `step2n2_auto` フォルダーが無ければ作る
            os.makedirs("lesson16/step2n2_auto")
        except FileExistsError:
            # 既存なら無視
            pass

        # `init.py` ファイルを作成します
        # 'x' - ファイルが存在しない場合のみの上書き
        path = "lesson16/step2n2_auto/init.py"
        try:
            with open(path, "x") as f:
                f.write(
                    """from lesson15.step1_const_conf_wcsc_v1 import E_OVER

class InitState():

    def update(self, req):
        # 何もせず終わります
        return E_OVER

"""
                )
        except FileExistsError as e:
            print(f"[Ignore] {e}")

    def clean_up(self):
        pass
