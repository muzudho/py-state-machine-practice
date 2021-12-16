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
        text = ""

        for item in data:
            text += f"{item}\n"
            pass

        return text
