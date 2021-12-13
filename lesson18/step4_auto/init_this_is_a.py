from lesson18.step2_auto.const import E_OVER, E_PIN, E_PEN
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

        pass
        pass
        pass
        pass
