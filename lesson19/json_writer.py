import os


class JsonWriter:
    @classmethod
    def write(clazz, file_path, data):

        try:
            # フォルダーが無ければ作る
            os.makedirs(os.path.dirname(file_path))
        except FileExistsError:
            # 既存なら無視
            pass

        text = JsonWriter.stringify(data)

        with open(f"{file_path}", "w", encoding="UTF-8") as f:
            f.write(text)

    @classmethod
    def stringify(clazz, data):
        n4sp = "    "  # 4 spaces
        text = ""

        list_s = []

        for k, v in data.items():
            list_s.append(f'"{k}":{{\n{n4sp}}}')

        text += f"{{\n{n4sp}" + f",\n{n4sp}".join(list_s) + "\n}\n"

        return text
