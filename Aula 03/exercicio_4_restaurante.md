# Exercício 4 - Restaurante (cálculo de conta)

## Sua tarefa

Você recebeu uma função que **funciona**, mas é difícil de ler. Ela calcula a conta de mesas num restaurante.

Refatore aplicando o que aprendeu hoje:

1. **Renomeie** tudo que tiver nome ruim (variáveis, função, parâmetros).
2. **Quebre a função grande** em funções menores com Extract Method.
3. **Use F2 no VSCode** pra renomear sem quebrar nada.
4. **Rode o código antes e depois** pra confirmar que continua funcionando.

---

## Código original (`exercicio_4_restaurante.py`):

```python
"""
Exercício 4 - Cálculo de conta de restaurante

A função fc(m, p, hg, c) recebe:
- m: lista de itens da mesa, cada item é tupla (nome, preço, qtd)
- p: número de pessoas dividindo a conta
- hg: True se a gorjeta é incluída no rachado
- c: tipo de cupom (None, "ANIVERSARIO" = 10% off, "FIDELIDADE" = 15% off)

Regras:
- Soma o subtotal de todos os itens (preço * quantidade)
- Aplica desconto se houver cupom válido
- Calcula gorjeta de 10% sobre o subtotal com desconto
- Divide pelo número de pessoas (incluindo gorjeta se hg=True)
"""


def fc(m, p, hg, c):
    sb = 0
    for x in m:
        sb = sb + (x[1] * x[2])
    if c == "ANIVERSARIO":
        sb = sb * 0.9
    elif c == "FIDELIDADE":
        sb = sb * 0.85
    g = sb * 0.10
    if hg == True:
        t = sb + g
    else:
        t = sb
    pp = t / p
    return {"subtotal": sb, "gorjeta": g, "total": sb + g, "por_pessoa": pp}


if __name__ == "__main__":
    mesa = [
        ("Pizza Margherita", 65.00, 2),
        ("Refrigerante", 8.00, 4),
        ("Sobremesa", 25.00, 4),
    ]
    resultado = fc(mesa, 4, True, "FIDELIDADE")
    print(f"Subtotal: R$ {resultado['subtotal']:.2f}")
    print(f"Gorjeta: R$ {resultado['gorjeta']:.2f}")
    print(f"Total: R$ {resultado['total']:.2f}")
    print(f"Por pessoa: R$ {resultado['por_pessoa']:.2f}")
```

## Resultado esperado

```
Subtotal: R$ 222.70
Gorjeta: R$ 22.27
Total: R$ 244.97
Por pessoa: R$ 61.24
```

## Critério de "pronto"

- [ ] Nenhuma variável ou função tem nome opaco
- [ ] A função principal está dividida em pelo menos 2 funções menores
- [ ] Magic numbers (0.9, 0.85, 0.10) viraram constantes nomeadas
- [ ] Comparação `hg == True` foi simplificada para `if hg`
- [ ] Código continua produzindo o mesmo resultado

---
