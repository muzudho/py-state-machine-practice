import os
from lesson16.code_gen.file_io import FileIo

from lesson18.const_conf import ConstConf
from lesson18.step1_const_conf_pen_v2 import const_conf_py_dict


def const_file_gen(dir_path, file_name):
    conf = ConstConf(const_conf_py_dict)

    text = ""

    for key, value in conf.data.items():
        text += f"{key} = '{value}'\n"

    # フォルダーが無ければ作る
    FileIo.makedirs(dir_path)

    dir_path = f"{dir_path}/{file_name}"
    FileIo.write(dir_path, text)
