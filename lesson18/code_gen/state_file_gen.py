from lesson18.code_gen.py_syntax.class_gen import ClassGen
from lesson18.code_gen.py_syntax.import_gen import ImportGen
from lesson18.code_gen.py_syntax.method_gen import MethodGen
from lesson18.code_gen.py_syntax.switch_gen import SwitchGen
from lesson18.step2_transition_conf import Transition


class StateFileGen:
    @classmethod
    def generate(clazz, dir_path, const_conf, transition, node_path):
        file_stem = node_path.replace("/", "_").lower()
        class_name = node_path.replace("/", "")
        # print(f"[Render] node_path={node_path} ----> {file_stem}")

        # `init.py` ファイルを作成します
        # 'x' - ファイルが存在しない場合のみの上書き
        path = f"{dir_path}/{file_stem}.py"

        # エッジの分岐部分
        directed_edge_list = Transition.create_edge_list_by_node_path(
            transition.data, node_path.split("/")
        )

        # 必要な定数を調査
        used_const = set()
        for edge in directed_edge_list:
            if edge.name != "":
                edge_const = const_conf.rev_data[edge.name]
                used_const.add(edge_const)

        text = ""

        # 定数をインポートします
        if 0 < len(used_const):
            text += ImportGen.generate(
                from_s="lesson18.step1n2_auto.const", import_list=used_const
            )

        text += ClassGen.generate(name=f"{class_name}State")
        text += MethodGen.signature(name="update", parameters_s="self, req")
        text += """
        self.on_entry(req)

        # 入力
        msg = req.pull_trigger()

        # 分岐
"""

        # エッジ分岐部
        edge_switch_list = StateFileGen.__edge_switch_list(
            const_conf=const_conf, directed_edge_list=directed_edge_list
        )
        text += SwitchGen.generate("        ", block_list=edge_switch_list)
        text += "\n"

        # ハンドラ自動生成
        text += MethodGen.generate(name="on_entry", parameters_s="self, req")
        for edge in directed_edge_list:
            if edge.name != "":
                text += MethodGen.generate(
                    name=f"on_{edge.name}", parameters_s="self, req"
                )

        try:
            with open(path, "x", encoding="UTF-8") as f:
                f.write(text)

        except FileExistsError as e:
            print(f"[Ignore] {e}")

    @classmethod
    def __edge_switch_list(clazz, const_conf, directed_edge_list):
        branch_list = []
        for edge in directed_edge_list:
            # 条件式
            if edge.name == "":
                cond = "True"  # 恒真
            elif edge.name in const_conf.rev_data:
                cond = f"msg == {const_conf.rev_data[edge.name]}"  # 定数
            else:
                cond = f'msg == "{edge.name}"'  # 文字列

            # if～elif文
            body_sequence = [
                f"self.on_{edge.name}()",  # イベントハンドラ呼出し
                f"return {edge.dst}",  # TODO 遷移先の名前を定数で書きたい
            ]

            # else文
            else_sequence = ['raise ValueError(f"Unexpected msg={msg}")']

            branch_list.append([cond, body_sequence, else_sequence])

        return branch_list
