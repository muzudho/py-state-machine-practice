from lesson11_data.step1_house_v1_const import MY_ROOM, OUT, MSG_SIT_DOWN


class MyroomState:
    def __init__(self):
        pass

    def update(self, message, c_sock):
        # 'Sit down' とメッセージを送ってくるのが正解です
        if message == MSG_SIT_DOWN:
            c_sock.send(
                """Clear!
Please push q key to quit.""".encode()
            )
            return MY_ROOM

        else:
            c_sock.send("You can see the house.".encode())
            return OUT
