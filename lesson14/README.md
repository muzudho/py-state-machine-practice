# Lesson14

状態遷移定義ファイルを作ってみましょう。サブサブサブステートマシンを作ってみましょう  

lesson14_projects/pen/data/transition.json:  

```python
{
    "title": "This is a pen",
    "entry_state": "Init",
    "data": {
        "Init": {
            "over": ["Init"],
            "that": ["Init"],
            "this": ["Init", "This"],
            "This": {
                "over": ["Init"],
                "was": ["Init"],
                "is": ["Init", "This", "Is"],
                "Is": {
                    "over": ["Init"],
                    "an": ["Init"],
                    "a": ["Init", "This", "Is", "A"],
                    "A": {
                        "over": ["Init"],
                        "pin": ["Init"],
                        "pen": ["Pen"]
                    }
                }
            }
        },
        "Pen": {
            "over": null
        }
    }
}
```

👆 キーボードから `This`, `is`, `a` と入力することで サブサブサブステートマシンまで下ります。  
`pen` と入力すると `Init` の次の状態の `Pen` へ遷移します  

## Run

Server start:  

```shell
python.exe -m lesson14.main "lesson14_projects/pen/conf.toml"
#                           ---------------------------------
#                           設定ファイル
```

Client start:  

```shell
python.exe -m lesson09.main
```

Input:  

```shell
This
is
a
pen
q
```
