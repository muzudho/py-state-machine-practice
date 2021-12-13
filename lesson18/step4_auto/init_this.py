from lesson18.step2_auto.const import E_WAS, E_IS, E_OVER
class InitThisState():
    def update(self, req):

        self.on_entry(req)

        # 入力
        msg = req.pull_trigger()

        # 分岐
        if msg == E_OVER:
            self.on_over()
            return ['Init']
            
        elif msg == E_WAS:
            self.on_was()
            return ['Init']
            
        elif msg == E_IS:
            self.on_is()
            return ['Init', 'This', 'Is']
            
        else:
            raise ValueError("Unexpected condition")

    def on_entry(self, req):
        pass

    def over(self, req):
        pass

    def was(self, req):
        pass

    def is(self, req):
        pass

