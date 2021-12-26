from lesson04.node_v04 import NodeV04
from lesson05.prefecture.hyogo_behavior import HyogoBehavior
from lesson05.prefecture.kyoto_behavior import KyotoBehavior
from lesson05.prefecture.mie_behavior import MieBehavior
from lesson05.prefecture.nara_behavior import NaraBehavior
from lesson05.prefecture.osaka_behavior import OsakaBehavior
from lesson05.prefecture.wakayama_behavior import WakayamaBehavior
from lesson05.node_v05 import NodeV05


def convert_prefecture_v04_to_v05(prefecture_graph_v04):
    prefecture_graph_v05 = {}

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
            prefecture_graph_v05[name] = NodeV05(
                name=node.name,
                next_name_list=node.next_name_list,
                behavior=__behaviors[name],
            )
        else:
            raise ValueError(f"Unexpected name={name}")

    return prefecture_graph_v05
