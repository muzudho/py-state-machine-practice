from lesson18.step2_auto.const import E_A, E_AN, E_OVER
class InitThisIsState():
    def update(self, req):

        self.on_entry(req)

        # 入力
        msg = req.pull_trigger()

        # 分岐
        if msg == E_OVER:
            self.on_over()
            return ['Init']
            
        elif msg == E_AN:
            self.on_an()
            return ['Init']
            
        elif msg == E_A:
            self.on_a()
            return ['Init', 'This', 'Is', 'A']
            
        else:
            raise ValueError("Unexpected condition")

    def on_entry(self, req):
        pass

    def over(self, req):
        pass

    def an(self, req):
        pass

    def a(self, req):
        pass

