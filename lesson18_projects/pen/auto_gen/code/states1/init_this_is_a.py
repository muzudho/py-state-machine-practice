from lesson17_projects.pen.auto_gen.data.const import E_OVER, E_PEN, E_PIN

class InitThisIsAState():
    def update(self, req):

        self.on_entry(req)

        # 入力
        msg = self.on_trigger(req)

        # 分岐
        if msg == E_OVER:
            self.on_over(req)
            return E_OVER

        elif msg == E_PIN:
            self.on_pin(req)
            return E_PIN

        elif msg == E_PEN:
            self.on_pen(req)
            return E_PEN

        elif msg == None:
            return None

        else:
            raise ValueError(f"Unexpected msg:{msg}")

    def on_entry(self, req):
        pass

    def on_trigger(self, req):
        return req.context.pull_trigger()

    def on_over(self, req):
        pass

    def on_pin(self, req):
        pass

    def on_pen(self, req):
        pass

