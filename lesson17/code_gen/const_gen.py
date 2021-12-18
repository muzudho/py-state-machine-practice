from lesson16.code_gen.file_io import FileIo

from lesson17.const_conf import ConstConf
from lesson17.step1_const_conf_wcsc_v2 import const_conf_data


def const_file_gen(dir_path, file_name):
    const_conf = ConstConf(const_conf_data)

    text = ""

    for key, value in const_conf.data.items():
        text += f"{key} = '{value}'\n"

    # フォルダーが無ければ作る
    FileIo.makedirs(dir_path)

    file_path = f"{dir_path}/{file_name}"
    FileIo.write(file_path, text)
