# Lesson14

サブサブサブステートマシンを作ってみましょう  

```python
transition_conf_data = {
    INIT: {
        E_OVER: [INIT],
        E_THAT: [INIT],
        E_THIS: [INIT, THIS],
        THIS: {
            E_OVER: [INIT],
            E_WAS: [INIT],
            E_IS: [INIT, THIS, IS],
            IS: {
                E_OVER: [INIT],
                E_AN: [INIT],
                E_A: [INIT, THIS, IS, A],
                A: {
                    E_OVER: [INIT],
                    E_PIN: [INIT],
                    E_PEN: [PEN],
                },
            },
        }
    },
    PEN: {
        E_OVER: None,
    }
}
```

👆 キーボードから `This`, `is`, `a` と入力することで サブサブサブステートマシンまで下ります。  
`pen` と入力すると `Init` の次の状態の `Pen` へ遷移します  

## Run

Server start:  

```shell
python.exe -m lesson14.main
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
```
