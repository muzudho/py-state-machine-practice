"""細かな処理"""
from lesson13.transition_conf import transition
from lesson13.state_gen_conf import state_gen


class StateMachineHelper():
    def __init__(self):
        pass

    @classmethod
    def lookup_next_state_path(clazz, state_path, edge_name):
        # transition設定ファイルの階層を下りていきましょう
        print(
            f"[lookup_next_state 12] state_path={state_path}")
        curr_dict = transition
        for state_node in state_path:
            print(
                f"[lookup_next_state 14] drop state_node={state_node}")
            curr_dict = curr_dict[state_node]

        # サブステートに無名状態があれば規定値ですので最下層まで下りていきましょう
        while '' in curr_dict:
            curr_dict = curr_dict['']

        # ステートは階層化しますが、Edge名は階層化しませんので１階層だけです。
        # Edge名から、次の state名のパス に変えます
        print(
            f"[lookup_next_state 24] state_path={edge_name}")
        state_path = curr_dict[edge_name]
        print(
            f"[lookup_next_state 27] new state_path={state_path}")

        return state_path

    @classmethod
    def create_state(clazz, state_path):
        # ステート名パスをたどって、state_gen設定ファイルの階層を下りていきましょう
        print(
            f"[create_state 39] state_path={state_path}")
        curr_dict = state_gen
        for state_node in state_path:
            print(
                f"[create_state 43] drop state_node={state_node}")
            curr_dict = curr_dict[state_node]

        # サブステートに無名状態があれば規定値ですので最下層まで下りていきましょう
        if curr_dict is dict:  # 文字列型で '' を検索してしまうことを避けます
            while '' in curr_dict:
                curr_dict = curr_dict['']

        # 葉要素を実行してオブジェクトを生成します
        state_generator = curr_dict
        state = state_generator()
        return state
