import random
from lesson04.node import Node


if __name__ == "__main__":
    # 大阪は、京都、兵庫、奈良、和歌山へつながっています
    osaka = Node("Osaka", ["Kyoto", "Hyogo", "Nara", "Wakayama"])

    # 京都は 兵庫、大阪、奈良、三重へつながっています
    kyoto = Node("Kyoto", ["Hyogo", "Osaka", "Nara", "Mie"])

    # 兵庫は 京都、大阪へつながっています
    hyogo = Node("Hyogo", ["Kyoto", "Osaka"])

    # 奈良は 大阪、京都、和歌山、三重へつながっています
    nara = Node("Nara", ["Osaka", "Kyoto", "Wakayama", "Mie"])

    # 和歌山は 大阪、奈良、三重へつながっています
    wakayama = Node("Wakayama", ["Osaka", "Nara", "Mie"])

    # 三重は 京都、奈良、和歌山へつながっています
    mie = Node("Mie", ["Kyoto", "Nara", "Wakayama"])

    # １つのディクショナリーにまとめましょう。これをグラフと呼ぶとします
    graph = {
        "Osaka": osaka,
        "Kyoto": kyoto,
        "Hyogo": hyogo,
        "Nara": nara,
        "Wakayama": wakayama,
        "Mie": mie,
    }

    # ランダムに県を１つ選びます
    prefeucture_name = random.choice(list(graph.keys()))
    print(f"1.{prefeucture_name}", end="", flush=True)

    for i in range(2, 21):
        prefecture = graph[prefeucture_name]
        # 次に行ける県の中から、ランダムに１つ選びます
        prefeucture_name = random.choice(prefecture.next_name_list)
        print(f"-->{i}.{prefeucture_name}", end="", flush=True)
