from lesson18.code_gen.states_gen import state_files_gen


class Render:
    @classmethod
    def is_verbose(clazz):
        return True

    def __init__(self):
        pass

    def run(self):
        state_files_gen("lesson18/step4_auto")

    def clean_up(self):
        pass
