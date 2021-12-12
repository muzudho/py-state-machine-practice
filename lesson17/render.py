from lesson17.code_gen.const_gen import const_file_gen
from lesson17.code_gen.states_gen import state_files_gen


class Render:
    @classmethod
    def is_verbose(clazz):
        return True

    def __init__(self):
        pass

    def run(self):
        const_file_gen("lesson17/auto_gen/const.py")
        state_files_gen("lesson16n3/auto_gen")

    def clean_up(self):
        pass
