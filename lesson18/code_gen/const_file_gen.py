import os

from lesson18.step1_const_conf_pen import ConstConf


def const_file_gen(dir_path, file_name):
    conf = ConstConf()

    text = ""

    for key, value in conf.data.items():
        text += f"{key} = '{value}'\n"

    try:
        # フォルダーが無ければ作る
        os.makedirs(dir_path)
    except FileExistsError:
        # 既存なら無視
        pass

    with open(f"{dir_path}/{file_name}", "w", encoding="UTF-8") as f:
        f.write(text)
