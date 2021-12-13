class MethodGen:
    def __init__(self):
        pass

    @classmethod
    def generate(clazz, name, parameters_s):
        text = MethodGen.signature(name=name, parameters_s=parameters_s)
        text = "        pass\n"
        return text

    @classmethod
    def signature(clazz, name, parameters_s):
        return f"""    def {name}({parameters_s}):
"""
