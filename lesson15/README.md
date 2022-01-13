# Lesson15

`transition_conf_data.py` だけあれば、状態遷移がちゃんとつながっているか検証できるはずです。  
graphviz を使って可視化しましょう  

# Set up

📖 　[Graphviz Download](https://graphviz.org/download/)

```shell
pip install graphviz
```

# Run

```shell
python.exe -m lesson15.main "lesson15_projects/house3/conf.toml"
#                           ------------------------------------
#                           設定ファイル
```

Output:  

`lesson15-graphs.png`  

# Documents

📖 [graphviz](https://graphviz.readthedocs.io/en/stable/index.html)  
