from lesson18.code_gen.const_gen import const_file_gen
from lesson18.code_gen.states_gen import state_files_gen


class Render:
    @classmethod
    def is_verbose(clazz):
        return True

    def __init__(self):
        pass

    def run(self):
        # 定数は transition_conf.py を作るために必要なので、先に作っておいてほしい
        const_file_gen("lesson18/step2_auto", "const.py")

        state_files_gen("lesson18/step4_auto")

    def clean_up(self):
        pass