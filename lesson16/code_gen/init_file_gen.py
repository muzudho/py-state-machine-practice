import os

from lesson16.code_gen.file_io import FileIo


def gen_init_file():
    # `step2n2_auto` フォルダーが無ければ作る
    dir_path = "lesson16/step2n2_auto"
    FileIo.makedirs(dir_path)

    # `init.py` ファイルを作成します
    file_path = "lesson16/step2n2_auto/init.py"
    text = """from lesson15.step1_const_conf_wcsc_v1 import E_OVER

class InitState():

    def update(self, req):
        # 何もせず終わります
        return E_OVER

"""

    FileIo.write(file_path, text)
