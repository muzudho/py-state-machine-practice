# Lesson15-2

サブステートを可視化できるように、 graphviz のクラスタリングを使いましょう  

# Set up

📖 　[Graphviz Download](https://graphviz.org/download/)

```shell
pip install graphviz
```

# Run

```shell
python.exe -m lesson15n2.graph_generator "lesson15n2_projects/pen/conf.toml" "transition_file" "output_graph_text_file"
#                                        ----------------------------------- ----------------- ------------------------
#                                        1.                                2.                3.
# 1. 設定ファイル（TOML形式）
# 2. 入力ファイル（JSON形式）を指すプロパティの名前
# 3. 出力ファイル（テキストファイル形式）を指すプロパティの名前
```

Output:  

`lesson15n2-graphs.png`  

# Documents

📖 [graphviz](https://graphviz.readthedocs.io/en/stable/index.html)  
