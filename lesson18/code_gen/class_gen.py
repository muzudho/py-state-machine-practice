class ClassGen:
    def __init__(self):
        pass

    @classmethod
    def generate(self, name, super_class_name=""):
        return f"""class {name}({super_class_name}):
"""
