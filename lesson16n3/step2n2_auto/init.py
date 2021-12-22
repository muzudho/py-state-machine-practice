class InitState():

    def update(self, req):

        # TODO 入力
        msg = ""

        # 分岐
        if msg == '':
            return ['Init', 'Login']

        else:
            raise ValueError("Unexpected condition")
