class MethodGen:
    def __init__(self):
        pass

    @classmethod
    def generate(clazz, name, parameters_s):
        signature = MethodGen.signature(name=name, parameters_s=parameters_s)
        body = "        pass\n\n"
        return "".join([signature, body])

    @classmethod
    def signature(clazz, name, parameters_s):
        return f"    def {name}({parameters_s}):\n"
