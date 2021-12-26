import random
from lesson04_data.prefecture_graph_v04 import prefecture_graph_v04


if __name__ == "__main__":

    # ランダムに県を１つ選びます
    prefeucture_name = random.choice(list(prefecture_graph_v04.keys()))
    print(f"1.{prefeucture_name}", end="", flush=True)

    for i in range(2, 21):
        prefecture = prefecture_graph_v04[prefeucture_name]
        # 次に行ける県の中から、ランダムに１つ選びます
        prefeucture_name = random.choice(prefecture.next_name_list)
        print(f"-->{i}.{prefeucture_name}", end="", flush=True)
