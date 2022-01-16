from lesson17.conf_obj.const_v17 import ConstV17


class ConstStringificationV17:
    @classmethod
    def stringify(clazz, const_doc):
        const = ConstV17(const_doc)

        text = ""

        for key, value in const.doc.items():
            text += f"{key} = '{value}'\n"

        return text
