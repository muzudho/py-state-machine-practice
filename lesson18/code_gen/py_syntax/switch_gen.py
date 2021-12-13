class SwitchGen:
    @classmethod
    def generate(clazz, indent, block_list, else_sequence=None):
        """TODO 分岐構造を記述します

        Examples
        --------
        if 1.expression: # a == b
            return 1.destination

        elif 2.expression: # a == b
            return 2.destination

        else:
            raise ValueError("Unexpected condition")
        """

        # if が1回、 elif がn回繰り返し、 raise が1回

        text = ""

        is_first = True

        for block in block_list:
            cond = block[0]
            if is_first:
                is_first = False
                text += f"{indent}if {cond}:\n"
            else:
                text += f"{indent}elif {cond}:\n"

            body_sequence = block[1]
            for line in body_sequence:
                text += f"{indent}    {line}\n"

            text += "\n"

        if else_sequence:
            text += f"{indent}else:\n"
            for line in body_sequence:
                text += f"{indent}    {line}\n"

        return text
