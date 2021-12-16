import os

from lesson17.const_conf import ConstConf
from lesson17.step1_const_conf_wcsc_v2 import const_conf_data


def const_file_gen(dir_path, file_name):
    const_conf = ConstConf(const_conf_data)

    text = ""

    for key, value in const_conf.data.items():
        text += f"{key} = '{value}'\n"

    try:
        # フォルダーが無ければ作る
        os.makedirs(dir_path)
    except FileExistsError:
        # 既存なら無視
        pass

    with open(f"{dir_path}/{file_name}", "w", encoding="UTF-8") as f:
        f.write(text)
