import random
from lesson04_data.prefecture_graph_v04 import prefecture_graph_v04
from lesson05_data.prefecture_graph_v05 import convert_prefecture_v04_to_v05


if __name__ == "__main__":

    # Lesson 04 で作ったデータを、 Lesson 05 用にアップデートします
    prefecture_graph_v05 = convert_prefecture_v04_to_v05(prefecture_graph_v04)

    # ランダムに県を１つ選びます
    prefecture_name = random.choice(list(prefecture_graph_v05.keys()))
    node = prefecture_graph_v05[prefecture_name]
    print(f"1.{prefecture_name} ", end="", flush=True)
    node.print()

    for i in range(2, 21):
        prefecture_name = random.choice(node.next_name_list)
        # 次に行ける県の中から、ランダムに１つ選びます
        node = prefecture_graph_v05[prefecture_name]
        print(f"{i}.{prefecture_name} ", end="", flush=True)
        node.print()
