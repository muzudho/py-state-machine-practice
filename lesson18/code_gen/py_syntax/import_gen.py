class ImportGen:
    @classmethod
    def generate(self, from_s, import_list):
        list_s = ", ".join(import_list)
        return f"from {from_s} import {list_s}\n"
