import socket
import random
from threading import Thread
from datetime import datetime
from colorama import Fore, init, Back


class Client():
    def __init__(self, server_host="127.0.0.1", server_port=5002, message_size=1024):
        """クライアントです。

        Parameters
        ----------
        server_host : str
            接続先サーバーのホスト名、またはIPアドレスです。 規定値 "127.0.0.1"

        server_port : int
            接続先サーバーのポート番号です。 規定値 5002

        message_size : int
            １回の通信で送れるバイト長。 規定値 1024
        """
        self._s_host = server_host
        self._s_port = server_port
        self._message_size = message_size

        # '_s_sock' - (Server socket) 接続先サーバーのソケットです
        self._s_sock = None

        # '_s_thr' - (Server thread) サーバーからのメッセージを受信するスレッド
        self._s_thr = None

    def clean_up(self):
        # サーバーのソケットを閉じます
        self._s_sock.close()

        # 実行中のスレッドがあれば終了するまで待機するのがクリーンです
        if not(self._s_thr is None) and self._s_thr.is_alive():
            print("[CleanUp] Before join")
            self._s_thr.join()
            print("[CleanUp] After join")
            self._s_thr = None

    def run(self):

        def server_worker():
            while True:
                try:
                    message = self._s_sock.recv(self._message_size).decode()
                    print("\n" + message)
                except Exception as e:
                    # client no longer connected
                    # remove it from the set
                    print(f"[!] Error: {e}")

                    print(f"Terminate this thread")
                    return

        # init colors
        init()

        # set the available colors
        colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX,
                  Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX,
                  Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX,
                  Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW
                  ]

        # choose a random color for the client
        client_color = random.choice(colors)

        # initialize TCP socket
        self._s_sock = socket.socket()
        # connect to the server
        print(f"[*] Connecting to {self._s_host}:{self._s_port}...")
        self._s_sock.connect((self._s_host, self._s_port))
        print("[+] Connected.")

        # prompt the client for a name
        name = input("Enter your name: ")

        # make a thread that listens for messages to this client & print them
        self._s_thr = Thread(target=server_worker)
        # make the thread daemon so it ends whenever the main thread ends
        self._s_thr.daemon = True
        # start the thread
        self._s_thr.start()

        while True:
            # input message we want to send to the server
            to_send = input()
            # a way to exit the program
            if to_send.lower() == 'q':
                break
            # add the datetime, name & the color of the sender
            date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            to_send = f"{client_color}[{date_now}] {name} {to_send}{Fore.RESET}"
            # finally, send the message
            self._s_sock.send(to_send.encode())
