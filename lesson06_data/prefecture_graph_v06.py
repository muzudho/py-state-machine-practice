from lesson04.node_v04 import NodeV04

# Lesson 06
from lesson06.prefecture.hyogo_behavior import HyogoBehavior
from lesson06.prefecture.kyoto_behavior import KyotoBehavior
from lesson06.prefecture.mie_behavior import MieBehavior
from lesson06.prefecture.nara_behavior import NaraBehavior
from lesson06.prefecture.osaka_behavior import OsakaBehavior
from lesson06.prefecture.wakayama_behavior import WakayamaBehavior
from lesson06.node_v06 import NodeV06


def convert_prefecture_v04_to_v06(prefecture_graph_v04):
    prefecture_graph_v06 = {}

    __behaviors = {
        "Osaka": OsakaBehavior(),
        "Kyoto": KyotoBehavior(),
        "Hyogo": HyogoBehavior(),
        "Nara": NaraBehavior(),
        "Wakayama": WakayamaBehavior(),
        "Mie": MieBehavior(),
    }

    for name, node in prefecture_graph_v04.items():

        if name in __behaviors.keys():
            # データのコピー
            prefecture_graph_v06[name] = NodeV06(
                name=node.name,
                next_name_list=node.next_name_list,
                behavior=__behaviors[name],
            )
        else:
            raise ValueError(f"Unexpected name={name}")

    return prefecture_graph_v06
