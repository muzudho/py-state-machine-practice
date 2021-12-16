class CommentGen:
    @classmethod
    def generate(clazz, indent, line_list):
        text = ""

        for line in line_list:
            text += f"{indent}{line}\n"

        return text
