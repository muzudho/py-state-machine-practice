from lesson18.code_gen.const_file_gen import const_file_gen


class Render:
    @classmethod
    def is_verbose(clazz):
        return True

    def __init__(self):
        pass

    def run(self):
        # 定数は transition_conf.py を作るために必要なので、先に作っておいてほしい
        const_file_gen("lesson18/step1n2_auto_const", "pen.py")

    def clean_up(self):
        pass
