from lesson18.step2_auto.const import E_THAT, E_THIS, E_OVER
class InitState():
    def update(self, req):

        self.on_entry(req)

        # 入力
        msg = req.pull_trigger()

        # 分岐
        if msg == E_OVER:
            self.on_over()
            return ['Init']
            
        elif msg == E_THAT:
            self.on_that()
            return ['Init']
            
        elif msg == E_THIS:
            self.on_this()
            return ['Init', 'This']
            
        else:
            raise ValueError("Unexpected condition")

    def on_entry(self, req):
        pass

    def over(self, req):
        pass

    def that(self, req):
        pass

    def this(self, req):
        pass

