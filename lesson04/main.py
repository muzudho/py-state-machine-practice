import random
from lesson04.node import Node


if __name__ == "__main__":
    nodes = {
        "Osaka": Node("Osaka", ["Kyoto", "Hyogo", "Nara", "Wakayama"]),
        "Kyoto": Node("Kyoto", ["Hyogo", "Osaka", "Nara", "Mie"]),
        "Hyogo": Node("Hyogo", ["Kyoto", "Osaka"]),
        "Nara": Node("Nara", ["Osaka", "Kyoto", "Wakayama", "Mie"]),
        "Wakayama": Node("Wakayama", ["Osaka", "Nara", "Mie"]),
        "Mie": Node("Mie", ["Kyoto", "Nara", "Wakayama"])
    }

    node_name = random.choice(list(nodes.keys()))
    print(f"1.{node_name}", end="", flush=True)

    for i in range(2, 21):
        node = nodes[node_name]
        node_name = random.choice(node.next_name_list)
        print(f"-->{i}.{node_name}", end="", flush=True)
