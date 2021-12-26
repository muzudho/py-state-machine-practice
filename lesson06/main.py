import random
from lesson06.hyogo_behavior import HyogoBehavior
from lesson06.kyoto_behavior import KyotoBehavior
from lesson06.mie_behavior import MieBehavior
from lesson06.nara_behavior import NaraBehavior
from lesson06.node import Node
from lesson06.osaka_behavior import OsakaBehavior
from lesson06.wakayama_behavior import WakayamaBehavior


if __name__ == "__main__":
    nodes = {
        "Osaka": Node("Osaka", ["Kyoto", "Hyogo", "Nara", "Wakayama"], OsakaBehavior()),
        "Kyoto": Node("Kyoto", ["Hyogo", "Osaka", "Nara", "Mie"], KyotoBehavior()),
        "Hyogo": Node("Hyogo", ["Kyoto", "Osaka"], HyogoBehavior()),
        "Nara": Node("Nara", ["Osaka", "Kyoto", "Wakayama", "Mie"], NaraBehavior()),
        "Wakayama": Node("Wakayama", ["Osaka", "Nara", "Mie"], WakayamaBehavior()),
        "Mie": Node("Mie", ["Kyoto", "Nara", "Wakayama"], MieBehavior()),
    }

    message = ""

    # ランダムに県を１つ選びます
    node_name = random.choice(list(nodes.keys()))
    node = nodes[node_name]
    message = node.create_message_v06(message)
    print(f"1.{node_name} {message}")

    for i in range(2, 21):
        # 次に行ける県の中から、ランダムに１つ選びます
        node_name = random.choice(node.next_name_list)
        node = nodes[node_name]
        message = node.create_message_v06(message)
        print(f"{i}.{node_name} {message}")
