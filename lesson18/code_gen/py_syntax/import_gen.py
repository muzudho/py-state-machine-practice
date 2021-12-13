class ImportGen:
    @classmethod
    def generate(self, from_s, import_set):
        if len(import_set) < 1:
            return ""

        list_s = ", ".join(import_set)
        return f"from {from_s} import {list_s}\n"
