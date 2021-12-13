class SwitchGen:
    @classmethod
    def generate(clazz, indent, block_list):
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
            body = block[1]

            if is_first:
                is_first = False
                text += f"{indent}if {cond}:\n"
            else:
                text += f"{indent}elif {cond}:\n"

            lines = body.split("\n")
            for line in lines:
                text += f"{indent}    {line}\n"

        text += f"""{indent}else:
{indent}    raise ValueError("Unexpected condition")
"""

        return text
