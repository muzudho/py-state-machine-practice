from lesson17.const_conf import ConstConf


class ConstStringification:
    @classmethod
    def stringify(clazz, const_conf_data):
        const_conf = ConstConf(const_conf_data)

        text = ""

        for key, value in const_conf.data.items():
            text += f"{key} = '{value}'\n"

        return text
