import socket
from threading import Thread

from lesson24.request_v24 import RequestV24
from lesson24.client_context_v24 import ClientContextV24


class ServerV24:
    @classmethod
    def is_verbose(clazz):
        return False

    def __init__(
        self,
        state_machine,
        host="0.0.0.0",
        port=5002,
        message_size=1024,
    ):
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

        self._s_sock = None  # (Server socket) このサーバーのTCPソケットです
        self._c_sock_set = None  # (Client socket set) このサーバーに接続してきたクライアントのソケットの集まりです
        self._state_machine = state_machine  # 状態遷移マシン

    def run(self):
        def client_worker(c_sock):
            """クライアントから送信されてくるバイナリデータに対応します

            Parameters
            ----------
            c_sock : socket
                接続しているクライアントのソケット
            """

            # Serverクラスは使い回すので、Lesson 18 とは限りません
            c_sock.send(
                """Welcome to lesson server !
--------------------------""".encode()
            )

            def __on_pull_trigger():
                """クライアントから受信したバイナリデータをテキストに変換します"""
                message = c_sock.recv(self._message_size).decode()
                return message

            # 外部から与えるオブジェクト
            client_context = ClientContextV24(
                c_sock=c_sock,
                pull_trigger=__on_pull_trigger,
            )

            def __create_req():
                """req変数を生成します"""

                # 開発が進むと Request の引数が増えたり減ったりするでしょう
                req = RequestV24(
                    state_path=self._state_machine.state_path, context=client_context
                )
                return req

            def __on_terminated():
                """ステートマシン終了時に行う処理"""
                # TODO クライアントに quit 命令などを送信する必要があるか？
                print(
                    """[server.py] Next state is None. State machine is finished.
Remove a socket"""
                )
                self._c_sock_set.remove(c_sock)

            # セット
            self._state_machine.create_request = __create_req
            self._state_machine.on_terminated = __on_terminated

            try:
                # ステートマシーンが停止するか、例外を投げるまでブロックします
                self._state_machine.start()

            except Exception as e:
                # client no longer connected
                # remove it from the set
                print(
                    f"""[!] Error: {e}
Remove a socket"""
                )
                self._c_sock_set.remove(c_sock)

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
