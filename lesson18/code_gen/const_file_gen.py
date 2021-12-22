import os
from lesson16.code_gen.file_io import FileIo

from lesson18.const_conf import ConstConf
from lesson18_data.pen_step1_const_dict import pen_const_py_dict


def const_file_gen(file_path):
    conf = ConstConf(pen_const_py_dict)

    text = ""

    for key, value in conf.data.items():
        text += f"{key} = '{value}'\n"

    # 出力
    FileIo.makedirs(os.path.dirname(file_path))
    FileIo.write(file_path, text)
