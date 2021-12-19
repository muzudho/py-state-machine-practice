import os
from lesson16.code_gen.file_io import FileIo

from lesson18.const_conf import ConstConf
from lesson18_data.step1_const_dict_pen import const_pen_py_dict


def const_file_gen(dir_path, file_name):
    conf = ConstConf(const_pen_py_dict)

    text = ""

    for key, value in conf.data.items():
        text += f"{key} = '{value}'\n"

    # フォルダーが無ければ作る
    FileIo.makedirs(dir_path)

    dir_path = f"{dir_path}/{file_name}"
    FileIo.write(dir_path, text)
