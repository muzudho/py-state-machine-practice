import os


class JsonWriter:
    @classmethod
    def n4sp(clazz, indent):
        return "".join(["    "] * indent)  # 4 spaces

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
        indent = 1
        n4sp = JsonWriter.n4sp(indent)  # 4 spaces

        text = f"{{\n"

        text += f",\n".join(JsonWriter.child_2(data, indent + 1))

        text += "\n}\n"

        return text

    @classmethod
    def child_2(clazz, data, indent):
        n4sp = JsonWriter.n4sp(indent)  # 4 spaces

        if isinstance(data, dict):
            list_s = []
            for k, v in data.items():
                text = ""
                text += f'{n4sp}"{k}":{{\n'

                # v
                text += f",\n".join(JsonWriter.child_2(v, indent + 1))

                text += f"\n{n4sp}}}"
                list_s.append(text)
            return list_s

        else:
            return ""
