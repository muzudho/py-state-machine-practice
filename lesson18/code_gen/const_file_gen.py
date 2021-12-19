import os
from lesson16.code_gen.file_io import FileIo

from lesson18.const_conf import ConstConf
from lesson18_data.step1_const_dict_pen import const_pen_py_dict


def const_file_gen(file_path):
    conf = ConstConf(const_pen_py_dict)

    text = ""

    for key, value in conf.data.items():
        text += f"{key} = '{value}'\n"

    # フォルダーが無ければ作る
    FileIo.makedirs(os.path.dirname(file_path))

    FileIo.write(file_path, text)
