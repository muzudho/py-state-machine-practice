class CodeGen:
    def __init__(self):
        pass

    @classmethod
    def create_comment_block(clazz, indent, line_list):
        text = ""

        for line in line_list:
            text += f"{indent}{line}\n"

        return text
