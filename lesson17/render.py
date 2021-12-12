from lesson17.code_gen.const_gen import const_file_gen
from lesson17.code_gen.states_gen import state_files_gen


class Render:
    @classmethod
    def is_verbose(clazz):
        return True

    def __init__(self):
        pass

    def run(self):
        # 定数は transition_conf.py を作るために必要なので、先に作っておいてほしい
        const_file_gen("lesson17/auto_gen1", "const.py")

        state_files_gen("lesson17/auto_gen2")

    def clean_up(self):
        pass
