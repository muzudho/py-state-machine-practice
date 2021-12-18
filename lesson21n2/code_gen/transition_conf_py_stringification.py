class TransitionConfPyStringification:
    @classmethod
    def n4sp(clazz, indent):
        return "".join(["    "] * indent)  # 4 spaces

    @classmethod
    def stringify(clazz, ordered_dict_data):
        """
        Parameters
        ----------
        data :
            OrderedDict を使った構造
        """

        indent = 0
        n4sp = TransitionConfPyStringification.n4sp(indent)  # 4 spaces
        title = ordered_dict_data["title"]  # TODO ダブルクォーテーションのエスケープ
        entry_node = (
            f'"{ordered_dict_data["entry_node"]}"'  # TODO ダブルクォーテーションの取り扱い or 定数
        )

        text = f"""transition_conf_data = {{
    "title": "{title}",
    "entry_node": {entry_node},
    "data": {{
"""
        indent += 2
        n4sp = TransitionConfPyStringification.n4sp(indent)  # 4 spaces

        block_list = []
        for key, value in ordered_dict_data["data"].items():
            if isinstance(value, dict):
                block_list.append(
                    f'{n4sp}"{key}":{{\n'
                    + f",\n".join(
                        TransitionConfPyStringification.child_dict(value, indent + 1)
                    )
                    + f"\n{n4sp}}}"
                )
            elif isinstance(value, list):
                block_list.append(
                    f'{n4sp}"{key}":["'
                    + '","'.join(
                        TransitionConfPyStringification.child_list(value, indent + 1)
                    )
                    + f'"]'
                )
            elif value is None:
                block_list.append(f'{n4sp}"{key}":null')
            else:
                block_list.append(f"<★Error key={key} value={value}>")

        text += ",\n".join(block_list)

        text += """
    }
}
"""

        return text

    @classmethod
    def child_dict(clazz, ordered_dict_data, indent):
        n4sp = TransitionConfPyStringification.n4sp(indent)  # 4 spaces

        block_list = []
        for k, v in ordered_dict_data.items():
            text = ""
            text += f'{n4sp}"{k}":'

            # v
            if isinstance(v, dict):
                text += (
                    "{\n"
                    + ",\n".join(
                        TransitionConfPyStringification.child_dict(v, indent + 1)
                    )
                    + f"\n{n4sp}}}"
                )
            elif isinstance(v, list):
                text += (
                    '["'
                    + '","'.join(
                        TransitionConfPyStringification.child_list(v, indent + 1)
                    )
                    + f'"]'
                )
            elif v is None:
                text += "None"
            else:
                text += "<★Error>"

            block_list.append(text)
        return block_list

    @classmethod
    def child_list(clazz, data, indent):
        item_s = []
        for item in data:
            item_s.append(item)
        return item_s
