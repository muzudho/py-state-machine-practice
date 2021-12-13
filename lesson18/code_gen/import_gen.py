class ImportGen:
    def __init__(self):
        pass

    @classmethod
    def generate(self, from_s, import_list):
        text = f"from {from_s} import "

        is_skip_comma = True

        for import_s in import_list:
            if is_skip_comma:
                is_skip_comma = False
            else:
                text += ", "

            text += import_s

        return f"{text}\n"
