class TransitionJsonStringification:
    @classmethod
    def n4sp(clazz, indent):
        return "".join(["    "] * indent)  # 4 spaces

    @classmethod
    def stringify(clazz, data):
        indent = 0
        text = f"{{\n"

        if isinstance(data, dict):
            text += f",\n".join(
                TransitionJsonStringification.child_dict(data, indent + 1)
            )
        elif isinstance(data, list):
            text += (
                '["'
                + '","'.join(TransitionJsonStringification.child_list(data, indent + 1))
                + f'"]'
            )
        elif data is None:
            text += "null"
        else:
            text += "<★Error>"

        text += "\n}\n"

        return text

    @classmethod
    def child_dict(clazz, data, indent):
        n4sp = TransitionJsonStringification.n4sp(indent)  # 4 spaces

        list_s = []
        for k, v in data.items():
            text = ""
            text += f'{n4sp}"{k}":'

            # v
            if isinstance(v, dict):
                text += (
                    "{\n"
                    + ",\n".join(
                        TransitionJsonStringification.child_dict(v, indent + 1)
                    )
                    + f"\n{n4sp}}}"
                )
            elif isinstance(v, list):
                text += (
                    '["'
                    + '","'.join(
                        TransitionJsonStringification.child_list(v, indent + 1)
                    )
                    + f'"]'
                )
            elif v is None:
                text += "null"
            else:
                text += "<★Error>"

            list_s.append(text)
        return list_s

    @classmethod
    def child_list(clazz, data, indent):
        item_s = []
        for item in data:
            item_s.append(item)
        return item_s
