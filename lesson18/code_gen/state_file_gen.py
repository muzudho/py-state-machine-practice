from lesson18.code_gen.py_syntax.class_gen import ClassGen
from lesson18.code_gen.py_syntax.import_gen import ImportGen
from lesson18.code_gen.py_syntax.method_gen import MethodGen
from lesson18.code_gen.py_syntax.switch_gen import SwitchGen
from lesson18.step2_transition_conf import TransitionConf


class StateFileGen:
    @classmethod
    def generate(clazz, dir_path, const_conf, transition_conf, node_path):
        file_stem = node_path.replace("/", "_").lower()
        class_name = node_path.replace("/", "")
        # print(f"[Render] node_path={node_path} ----> {file_stem}")

        # `init.py` ファイルを作成します
        # 'x' - ファイルが存在しない場合のみの上書き
        path = f"{dir_path}/{file_stem}.py"

        # エッジの分岐部分
        directed_edge_list = TransitionConf.create_edge_list_by_node_path(
            transition_conf.data, node_path.split("/")
        )

        # 使った定数を調査
        used_const_set = set()
        for edge in directed_edge_list:
            const_conf.pickup_from_item(edge.name, used_const_set)

        text = ""
        text += ClassGen.generate(name=f"{class_name}State")
        text += MethodGen.signature(name="update", parameters_s="self, req")
        text += """
        self.on_entry(req)

        # 入力
        msg = self.on_trigger(req)

        # 分岐
"""

        # エッジ分岐部
        used_const_set = set()  # 使った定数
        switch_model = StateFileGen.__edge_switch_model(
            const_conf=const_conf,
            directed_edge_list=directed_edge_list,
            used_const_set=used_const_set,
        )
        text += SwitchGen.generate("        ", switch_model=switch_model)
        text += "\n"

        # ハンドラ生成
        text += MethodGen.generate(name="on_entry", parameters_s="self, req")
        text += MethodGen.generate(
            name="on_trigger",
            parameters_s="self, req",
            body_sequence=["return req.pull_trigger()"],
        )
        # ハンドラ自動生成
        for edge in directed_edge_list:
            if edge.name != "":
                text += MethodGen.generate(
                    name=f"on_{edge.name}", parameters_s="self, req"
                )

        # 定数のインポートをファイルの冒頭に付けます
        if 0 < len(used_const_set):
            statement = ImportGen.generate(
                from_s="lesson18.step1n2_auto.const", import_set=used_const_set
            )
            text = f"{statement}\n{text}"

        with open(path, "w", encoding="UTF-8") as f:
            f.write(text)

    @classmethod
    def __edge_switch_model(clazz, const_conf, directed_edge_list, used_const_set):

        if_else_list = []
        # if～elif文
        for edge in directed_edge_list:
            # 条件式
            if edge.name == "":
                cond = "True"  # 恒真
            else:
                operand = const_conf.replace_item(edge.name, '"')  # 定数、でなければ "文字列"
                # この練習プログラムでは E_XXX のような定数になってるはず
                const_conf.pickup_from_item(operand, used_const_set)
                cond = f"msg == {operand}"

            # シーケンス
            body_sequence = []
            body_sequence.append(f"self.on_{edge.name}()")  # イベントハンドラ呼出し
            if edge.dst:
                item_list = const_conf.replace_list(
                    edge.dst, '"'
                )  # リストの要素をなるべく定数に置換、でなければ "文字列" に置換
                const_conf.pickup_from_list(item_list, used_const_set)
                csv = ", ".join(item_list)
                body_sequence.append(f"return [{csv}]")
            else:
                body_sequence.append("return None")

            if_else_list.append([cond, body_sequence])

        # else文
        else_sequence = ['raise ValueError(f"Unexpected msg:{msg}")']

        switch_model = [if_else_list, else_sequence]
        return switch_model
