import os

from lesson11n80.code_gen.file_io import FileIo


def gen_init_file_v16(output_dir_path):
    # `auto_gen` フォルダーが無ければ作る
    FileIo.makedirs(output_dir_path)

    # `init.py` ファイルを作成します
    file_path = os.path.join(output_dir_path, "init.py")
    text = """class InitState():

    def update(self, req):
        # 何もせず終わります
        return "over"

"""

    FileIo.write(file_path, text)
