# Exercício 8 - E-commerce (carrinho de compras)

## Sua tarefa

Você recebeu uma função que **funciona**, mas é difícil de ler. Ela calcula o total de um carrinho de compras de uma loja online, aplicando descontos, cupom e frete.

Refatore aplicando o que aprendeu hoje:

1. **Renomeie** tudo que tiver nome ruim (variáveis, função, parâmetros).
2. **Quebre a função grande** em funções menores com Extract Method.
3. **Use F2 no VSCode** pra renomear sem quebrar nada.
4. **Rode o código antes e depois** pra confirmar que continua funcionando.

---

## Código original (`exercicio_8_ecommerce.py`):

```python
"""
Exercício 8 - Cálculo do total de um carrinho de e-commerce

A função calc(itns, cup, freg) recebe:
- itns: lista de itens do carrinho, cada item é tupla (nome, preço, quantidade)
- cup: código de cupom (None, "PROMO10" = 10% off, "PROMO20" = 20% off)
- freg: True se o frete é grátis (cliente premium)

Regras:
- Soma o subtotal de todos os itens (preço * quantidade)
- Se o subtotal passar de 500, aplica 5% de desconto por volume
- Aplica o desconto do cupom, se houver cupom válido
- Calcula o frete conforme o subtotal:
    - frete grátis se freg=True
    - grátis se subtotal > 300
    - R$ 15 se subtotal > 100
    - R$ 30 caso contrário
- Retorna o subtotal (com descontos) somado ao frete
"""


def calc(itns, cup, freg):
    st = 0
    for x in itns:
        st = st + (x[1] * x[2])
    if st > 500:
        st = st - (st * 0.05)
    if cup == "PROMO10":
        st = st - (st * 0.10)
    elif cup == "PROMO20":
        st = st - (st * 0.20)
    if freg == True:
        f = 0
    else:
        if st > 300:
            f = 0
        elif st > 100:
            f = 15
        else:
            f = 30
    return st + f


if __name__ == "__main__":
    carrinho = [
        ("Camiseta", 50.0, 3),
        ("Calça", 120.0, 2),
        ("Meia", 15.0, 4),
    ]
    total = calc(carrinho, "PROMO10", False)
    print(f"Total: R$ {total:.2f}")
```

## Resultado esperado

```
Total: R$ 405.00
```

## Critério de "pronto"

- [ ] Nenhuma variável ou função tem nome opaco
- [ ] A função principal está dividida em pelo menos 2 funções menores
- [ ] Magic numbers (500, 0.05, 0.10, 0.20, 300, 100, 15, 30) viraram constantes nomeadas
- [ ] Comparação `freg == True` foi simplificada para `if freg`
- [ ] Código continua produzindo o mesmo resultado

---
