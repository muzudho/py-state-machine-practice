from lesson17.const_conf import ConstConf


def const_file_gen(path):
    conf = ConstConf()

    text = ""

    for key, value in conf.data.items():
        text += f"{key} = '{value}'\n"

    try:
        with open(path, "x", encoding="UTF-8") as f:
            f.write(text)

    except FileExistsError as e:
        print(f"[Ignore] {e}")
