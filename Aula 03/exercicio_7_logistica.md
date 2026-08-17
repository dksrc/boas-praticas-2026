# Exercício 7 - Logística (cálculo de frete)

## Sua tarefa

Você recebeu uma função que **funciona**, mas é difícil de ler. Ela calcula o valor e prazo de frete de encomendas.

Refatore aplicando o que aprendeu hoje:

1. **Renomeie** tudo que tiver nome ruim (variáveis, função, parâmetros).
2. **Quebre a função grande** em funções menores com Extract Method.
3. **Use F2 no VSCode** pra renomear sem quebrar nada.
4. **Rode o código antes e depois** pra confirmar que continua funcionando.

---

## Código original (`exercicio_7_logistica.py`):

```python
"""
Exercício 7 - Cálculo de frete de encomendas

A função cf(e) recebe uma encomenda:
    {"peso": float (kg), "dest": str (região: "SE", "S", "CO", "NE", "N"),
     "exp": bool (expresso), "frag": bool (frágil)}

Regras:
- Valor base: R$ 10
- Por kg: R$ 2 (SE), R$ 3 (S), R$ 4 (CO), R$ 5 (NE), R$ 6 (N)
- Expresso: dobra o valor e reduz prazo pela metade
- Frágil: +R$ 8 e +1 dia
- Prazo base (dias): 2 (SE), 3 (S), 4 (CO), 5 (NE), 7 (N)
"""


def cf(e):
    vb = 10
    p = e["peso"]
    d = e["dest"]
    if d == "SE":
        vk = 2
        pr = 2
    elif d == "S":
        vk = 3
        pr = 3
    elif d == "CO":
        vk = 4
        pr = 4
    elif d == "NE":
        vk = 5
        pr = 5
    else:
        vk = 6
        pr = 7
    v = vb + (p * vk)
    if e["exp"] == True:
        v = v * 2
        pr = pr / 2
    if e["frag"] == True:
        v = v + 8
        pr = pr + 1
    return {"valor": v, "prazo_dias": pr}


if __name__ == "__main__":
    encomendas = [
        {"peso": 2.5, "dest": "SE", "exp": False, "frag": False},
        {"peso": 5.0, "dest": "N", "exp": True, "frag": True},
        {"peso": 1.0, "dest": "NE", "exp": False, "frag": True},
        {"peso": 10.0, "dest": "S", "exp": True, "frag": False},
    ]
    for e in encomendas:
        r = cf(e)
        print(f"{e['peso']}kg para {e['dest']}: R$ {r['valor']:.2f} em {r['prazo_dias']} dias")
```

## Resultado esperado

```
2.5kg para SE: R$ 15.00 em 2 dias
5.0kg para N: R$ 88.00 em 4.5 dias
1.0kg para NE: R$ 23.00 em 6 dias
10.0kg para S: R$ 80.00 em 1.5 dias
```

## Critério de "pronto"

- [ ] Nenhuma variável ou função tem nome opaco
- [ ] A função principal está dividida em pelo menos 2 funções menores
- [ ] Magic numbers (10, 2, 3, 4, 5, 6, 7, 8) viraram constantes nomeadas
- [ ] Comparações `== True` foram simplificadas
- [ ] Código continua produzindo o mesmo resultado

---
