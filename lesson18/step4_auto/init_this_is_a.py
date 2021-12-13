from lesson18.step2_auto.const import E_PEN, E_PIN, E_OVER
class InitThisIsAState():
    def update(self, req):

        self.on_entry(req)

        # 入力
        msg = req.pull_trigger()

        # 分岐
        if msg == E_OVER:
            self.on_over()
            return ['Init']
            
        elif msg == E_PIN:
            self.on_pin()
            return ['Init']
            
        elif msg == E_PEN:
            self.on_pen()
            return ['Pen']
            
        else:
            raise ValueError("Unexpected condition")

    def on_entry(self, req):
        pass

    def over(self, req):
        pass

    def pin(self, req):
        pass

    def pen(self, req):
        pass

