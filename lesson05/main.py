import random
from lesson05.hyogo_behavior import HyogoBehavior
from lesson05.kyoto_behavior import KyotoBehavior
from lesson05.mie_behavior import MieBehavior
from lesson05.nara_behavior import NaraBehavior
from lesson05.node import Node
from lesson05.osaka_behavior import OsakaBehavior
from lesson05.wakayama_behavior import WakayamaBehavior


if __name__ == "__main__":
    nodes = {
        "Osaka": Node("Osaka", ["Kyoto", "Hyogo", "Nara", "Wakayama"], OsakaBehavior()),
        "Kyoto": Node("Kyoto", ["Hyogo", "Osaka", "Nara", "Mie"], KyotoBehavior()),
        "Hyogo": Node("Hyogo", ["Kyoto", "Osaka"], HyogoBehavior()),
        "Nara": Node("Nara", ["Osaka", "Kyoto", "Wakayama", "Mie"], NaraBehavior()),
        "Wakayama": Node("Wakayama", ["Osaka", "Nara", "Mie"], WakayamaBehavior()),
        "Mie": Node("Mie", ["Kyoto", "Nara", "Wakayama"], MieBehavior())
    }

    node_name = random.choice(list(nodes.keys()))
    node = nodes[node_name]
    print(f"1.{node_name} ", end="", flush=True)
    node.print()

    for i in range(2, 21):
        node_name = random.choice(node.next_name_list)
        node = nodes[node_name]
        print(f"{i}.{node_name} ", end="", flush=True)
        node.print()
