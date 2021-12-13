import os
from lesson18.code_gen.class_gen import ClassGen
from lesson18.code_gen.import_gen import ImportGen
from lesson18.code_gen.method_gen import MethodGen
from lesson18.code_gen.py_gen import CodeGen
from lesson18.step1_const_conf import ConstConf
from lesson18.step3_transition_conf import Transition


def state_files_gen(dir_path):
    transition = Transition()
    const_conf = ConstConf()

    # エッジの一覧
    edge_list = transition.create_edge_list()
    for edge in edge_list:
        print(f"[Render] edge={edge}")

    try:
        # フォルダーが無ければ作る
        os.makedirs(dir_path)
    except FileExistsError:
        # 既存なら無視
        pass

    # ノードの一覧
    node_path_set = Transition.extract_node_path_set(edge_list)
    for node_path in node_path_set:
        if node_path is None:
            continue

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
                from_s="lesson18.step2_auto.const", import_list=used_const
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
        edge_branch_list = __edge_branch_list(
            const_conf=const_conf, directed_edge_list=directed_edge_list
        )
        text += CodeGen.create_switch_block("        ", block_list=edge_branch_list)
        text += "\n"

        # ハンドラ自動生成
        text += MethodGen.generate(name="on_entry", parameters_s="self, req")
        for edge in directed_edge_list:
            if edge.name != "":
                text += MethodGen.generate(name=edge.name, parameters_s="self, req")

        try:
            with open(path, "x", encoding="UTF-8") as f:
                f.write(text)

        except FileExistsError as e:
            print(f"[Ignore] {e}")


def __edge_branch_list(const_conf, directed_edge_list):
    branch_list = []
    for edge in directed_edge_list:
        # 条件式
        if edge.name == "":
            cond = "True"  # 恒真
        elif edge.name in const_conf.rev_data:
            cond = f"msg == {const_conf.rev_data[edge.name]}"  # 定数
        else:
            cond = f'msg == "{edge.name}"'  # 文字列

        # 本文
        body = ""
        body += f"self.on_{edge.name}()\n"  # イベントハンドラ呼出し
        body += f"return {edge.dst}\n"  # TODO 遷移先の名前を定数で書きたい

        branch_list.append([cond, body])

    return branch_list
