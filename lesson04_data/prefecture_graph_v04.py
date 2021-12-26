from lesson04.node_v04 import NodeV04

# 大阪は、京都、兵庫、奈良、和歌山へつながっています
osaka = NodeV04("Osaka", ["Kyoto", "Hyogo", "Nara", "Wakayama"])

# 京都は 兵庫、大阪、奈良、三重へつながっています
kyoto = NodeV04("Kyoto", ["Hyogo", "Osaka", "Nara", "Mie"])

# 兵庫は 京都、大阪へつながっています
hyogo = NodeV04("Hyogo", ["Kyoto", "Osaka"])

# 奈良は 大阪、京都、和歌山、三重へつながっています
nara = NodeV04("Nara", ["Osaka", "Kyoto", "Wakayama", "Mie"])

# 和歌山は 大阪、奈良、三重へつながっています
wakayama = NodeV04("Wakayama", ["Osaka", "Nara", "Mie"])

# 三重は 京都、奈良、和歌山へつながっています
mie = NodeV04("Mie", ["Kyoto", "Nara", "Wakayama"])

# １つのディクショナリーにまとめましょう。これをグラフと呼ぶとします
prefecture_graph_v04 = {
    "Osaka": osaka,
    "Kyoto": kyoto,
    "Hyogo": hyogo,
    "Nara": nara,
    "Wakayama": wakayama,
    "Mie": mie,
}
