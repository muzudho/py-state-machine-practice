class CommentGen:
    @classmethod
    def generate(clazz, indent, line_list):
        text = f"\n{indent}".join(line_list)
        return f"{indent}{text}\n"
