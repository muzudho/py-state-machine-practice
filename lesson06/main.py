import random
from lesson04_data.prefecture_graph_v04 import prefecture_graph_v04
from lesson06_data.prefecture_graph_v06 import convert_prefecture_v04_to_v06


if __name__ == "__main__":

    # Lesson 04 で作ったデータを、 Lesson 05 用にアップデートします
    prefecture_graph_v06 = convert_prefecture_v04_to_v06(prefecture_graph_v04)

    message = ""

    # ランダムに県を１つ選びます
    node_name = random.choice(list(prefecture_graph_v06.keys()))
    node = prefecture_graph_v06[node_name]
    message = node.create_message_v06(message)
    print(f"1.{node_name} {message}")

    for i in range(2, 21):
        # 次に行ける県の中から、ランダムに１つ選びます
        node_name = random.choice(node.next_name_list)
        node = prefecture_graph_v06[node_name]
        message = node.create_message_v06(message)
        print(f"{i}.{node_name} {message}")
