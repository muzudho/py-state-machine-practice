from lesson18.step2_auto.const import E_OVER, E_THIS, E_THAT
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

        pass
        pass
        pass
        pass
