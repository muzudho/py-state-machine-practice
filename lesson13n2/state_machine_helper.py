"""細かな処理"""


class StateMachineHelper:
    def __init__(self):
        pass

    @classmethod
    def lookup_next_state_path(clazz, transition_conf, state_path, edge_name):
        # transition設定ファイルの階層を下りていきましょう
        # print(
        #    f"[lookup_next_state 12] state_path={state_path}")
        curr_dict = transition_conf
        for state_node in state_path:
            # print(
            #    f"[lookup_next_state 14] drop state_node={state_node}")
            curr_dict = curr_dict[state_node]

        # サブステートに無名状態があれば規定値ですので最下層まで下りていきましょう
        while "" in curr_dict:
            curr_dict = curr_dict[""]

        # ステートは階層化しますが、Edge名は階層化しませんので１階層だけです。
        # Edge名から、次の state名のパス に変えます
        # print(
        #    f"[lookup_next_state 24] edge_name={edge_name}")
        state_path = curr_dict[edge_name]
        # print(
        #    f"[lookup_next_state 27] new state_path={state_path}")

        return state_path

    @classmethod
    def create_state(clazz, state_gen, state_path):
        # ステート名パスをたどって、state_gen設定ファイルの階層を下りていきましょう
        # print(
        #    f"[create_state 39] state_path={state_path}")
        curr_dict = state_gen
        for state_node in state_path:
            # print(
            #    f"[create_state 43] drop state_node={state_node}")
            curr_dict = curr_dict[state_node]

        # print(
        #    f"[create_state] curr_dict={curr_dict}")

        # サブステートに無名状態があれば規定値ですので最下層まで下りていきましょう
        while True:
            if isinstance(curr_dict, dict) and (
                "" in curr_dict
            ):  # 文字列型で '' を含むか誤判定してしまうことを避けます
                # print(
                #    f"[create_state] drop ''")
                curr_dict = curr_dict[""]
            else:
                break

        # 葉要素を実行してオブジェクトを生成します
        state_generator = curr_dict
        # print(
        #    f"[create_state] state_generator={state_generator}")
        state = state_generator()
        return state
