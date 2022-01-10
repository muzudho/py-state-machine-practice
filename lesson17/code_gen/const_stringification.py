from lesson17.code_gen.const_conf import ConstConfV17


class ConstStringification:
    @classmethod
    def stringify(clazz, const_conf_py_dict):
        const_conf = ConstConfV17(const_conf_py_dict)

        text = ""

        for key, value in const_conf.data.items():
            text += f"{key} = '{value}'\n"

        return text
