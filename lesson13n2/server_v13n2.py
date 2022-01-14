import socket
from threading import Thread

from lesson13n2.request import Request
from lesson13.state_machine_helper_v13 import StateMachineHelperV13
from lesson12_projects.house3.data.const import OUT
from lesson13n2_projects.house3n2.data.transition2 import house3n2_transition2_doc
from lesson13n2_projects.house3n2.data.state_gen_conf import house3n2_state_gen


class ServerV13n2:
    def __init__(self, host="0.0.0.0", port=5002, message_size=1024):
        """初期化

        Parameters
        ----------
        host : str
            サーバーのIPアドレス。 規定値 "0.0.0.0"

        port : int
            サーバー側のポート番号。 規定値 5002

        message_size : int
            １回の通信で送れるバイト長。 規定値 1024
        """
        self._host = host
        self._port = port
        self._message_size = message_size

        # '_s_sock' - (Server socket) このサーバーのTCPソケットです
        self._s_sock = None

        # '_c_sock_set' - (Client socket set) このサーバーに接続してきたクライアントのソケットの集まりです
        self._c_sock_set = None

    def run(self):
        def client_worker(c_sock):
            """クライアントから送信されてくるバイナリデータに対応します

            Parameters
            ----------
            c_sock : socket
                接続しているクライアントのソケット
            """

            c_sock.send(
                """Welcome to Lesson 13-2 !
------------------------""".encode()
            )

            # 最初は外に居ます
            state_path = [OUT]
            # state_gen_conf.py を見て state_path から state を生成します
            state = StateMachineHelperV13.create_state_v13(
                house3n2_state_gen, state_path
            )

            while True:
                try:

                    def __on_pull_trigger():
                        # クライアントから受信したバイナリデータをテキストに変換します
                        message = c_sock.recv(self._message_size).decode()
                        return message

                    # 開発が進むと Request の引数が増えたり減ったりするでしょう
                    req = Request(
                        c_sock=c_sock, pull_trigger=__on_pull_trigger)

                    # メッセージに応じたアクションを行ったあと、Edge名を返します
                    edge_name = state.update(req)
                    print(f"[server.py] edge_name={edge_name}")

                    # transition_conf_data.py を見て state_path を得ます
                    state_path = StateMachineHelperV13.lookup_next_state_path_v13(
                        house3n2_transition2_doc, state_path, edge_name
                    )

                    if state_path is None:
                        # ステートマシンは終了しました
                        print("[server.py] State machine is finished")
                        print("Remove a socket")
                        self._c_sock_set.remove(c_sock)
                        break

                    # state_gen_conf.py を見て state_path から state を生成します
                    state = StateMachineHelperV13.create_state_v13(
                        house3n2_state_gen, state_path
                    )

                except Exception as e:
                    # client no longer connected
                    # remove it from the set
                    print(f"[!] Error: {e}")

                    print(f"Remove a socket")
                    self._c_sock_set.remove(c_sock)
                    break

        self._c_sock_set = set()  # 初期化

        s_sock = socket.socket()  # このサーバーのTCPソケットの設定を行っていきます

        # make the port as reusable port
        s_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # ホストとポート番号を設定します
        s_sock.bind((self._host, self._port))

        # クライアントの同時接続数上限
        s_sock.listen(5)
        self._s_sock = s_sock

        print(f"[*] Listening as {self._host}:{self._port}")

        # クライアントからの接続を待ち続けるループです
        while True:
            print(f"Wait a connection")
            # クライアントからの接続があるまで、ここでブロックします
            # 'c_sock' - Client socket
            # 'c_addr' - Client address
            c_sock, c_addr = self._s_sock.accept()
            print(f"[+] {c_addr} connected.")

            # クライアントの接続を覚えておきます
            self._c_sock_set.add(c_sock)

            # 別スレッドを開始します
            thr = Thread(target=client_worker, args=(c_sock,))

            # make the thread daemon so it ends whenever the main thread ends
            thr.daemon = True

            # start the thread
            thr.start()

    def clean_up(self):
        # クライアントのソケットを閉じます
        print("Clean up")
        if not (self._c_sock_set is None):
            for c_sock in self._c_sock_set:
                c_sock.close()

        # サーバーのソケットも閉じます
        if not (self._s_sock is None):
            self._s_sock.close()
