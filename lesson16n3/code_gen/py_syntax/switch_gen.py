class SwitchGen:
    @classmethod
    def generate(clazz, indent, block_list):
        """分岐構造を記述します
        TODO Lesson18から改良版を持ってきたい？

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
            if is_first:
                is_first = False
                text += f"""{indent}if {block[0]}:
{indent}    {block[1]}
"""
            else:
                text += f"""{indent}elif {block[0]}:
{indent}    {block[1]}
"""

        text += f"""{indent}else:
{indent}    raise ValueError("Unexpected condition")
"""

        return text
