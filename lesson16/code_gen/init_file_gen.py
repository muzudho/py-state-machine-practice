import os

from lesson16.code_gen.file_io import FileIo


def gen_init_file():
    # `auto_gen` フォルダーが無ければ作る
    dir_path = "lesson16/auto_gen"
    FileIo.makedirs(dir_path)

    # `init.py` ファイルを作成します
    # TODO import文を変数にしたい
    file_path = "lesson16/auto_gen/init.py"
    text = """from lesson15_projects.wcsc.data.const import E_OVER

class InitState():

    def update(self, req):
        # 何もせず終わります
        return E_OVER

"""

    FileIo.write(file_path, text)
