import os

from lesson17.step1_const_conf_wcsc import ConstConf


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

    try:
        with open(f"{dir_path}/{file_name}", "x", encoding="UTF-8") as f:
            f.write(text)

    except FileExistsError as e:
        print(f"[Ignore] {e}")
