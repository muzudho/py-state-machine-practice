import os

from lesson11n80.code_gen.file_io_v11n80 import FileIoV11n80


def gen_init_file_v16(output_dir_path):
    # `auto_gen` フォルダーが無ければ作る
    FileIoV11n80.makedirs(output_dir_path)

    # `init.py` ファイルを作成します
    file_path = os.path.join(output_dir_path, "init.py")
    text = """class InitState():

    def update(self, req):
        # 何もせず終わります
        return "over"

"""

    FileIoV11n80.write(file_path, text)
