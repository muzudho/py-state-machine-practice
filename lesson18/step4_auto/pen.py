from lesson18.step2_auto.const import E_OVER
class PenState():
    def update(self, req):

        self.on_entry(req)

        # 入力
        msg = req.pull_trigger()

        # 分岐
        if msg == E_OVER:
            self.on_over()
            return None
            
        else:
            raise ValueError("Unexpected condition")

        pass
        pass
