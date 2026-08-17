# Exercício 3 - Sistema de RH (folha de pagamento)

## Sua tarefa

Você recebeu uma função que **funciona**, mas é difícil de ler. Ela calcula o salário líquido de funcionários.

Refatore aplicando o que aprendeu hoje:

1. **Renomeie** tudo que tiver nome ruim (variáveis, função, parâmetros).
2. **Quebre a função grande** em funções menores com Extract Method.
3. **Use F2 no VSCode** pra renomear sem quebrar nada.
4. **Rode o código antes e depois** pra confirmar que continua funcionando.

---

## Código original (`exercicio_3_rh.py`):

```python
"""
Exercício 3 - Cálculo de salário líquido

A função calc(f) recebe um dicionário de funcionário:
    {"nome": str, "s": float (salário bruto), "h_ex": int (horas extras), "d": int (dependentes)}

Regras:
- Valor da hora extra: salário bruto / 220 * 1.5
- INSS: 11% sobre o salário bruto (limite máximo R$ 800)
- IR (após dedução de R$ 189.59 por dependente):
    - até 2259.20: isento
    - 2259.21 a 2826.65: 7.5%
    - 2826.66 a 3751.05: 15%
    - 3751.06 a 4664.68: 22.5%
    - acima: 27.5%
"""


def calc(f):
    s = f["s"]
    h = f["h_ex"]
    d = f["d"]
    vh = (s / 220) * 1.5
    se = s + (vh * h)
    i = se * 0.11
    if i > 800:
        i = 800
    bi = se - i - (d * 189.59)
    if bi <= 2259.20:
        ir = 0
    elif bi <= 2826.65:
        ir = bi * 0.075
    elif bi <= 3751.05:
        ir = bi * 0.15
    elif bi <= 4664.68:
        ir = bi * 0.225
    else:
        ir = bi * 0.275
    liq = se - i - ir
    return {"nome": f["nome"], "salario_bruto": se, "inss": i, "ir": ir, "liquido": liq}


if __name__ == "__main__":
    funcionarios = [
        {"nome": "Ana", "s": 3500, "h_ex": 10, "d": 1},
        {"nome": "Bruno", "s": 1800, "h_ex": 0, "d": 0},
        {"nome": "Carla", "s": 8000, "h_ex": 5, "d": 2},
    ]
    for f in funcionarios:
        r = calc(f)
        print(f"{r['nome']}: bruto R$ {r['salario_bruto']:.2f}, líquido R$ {r['liquido']:.2f}")
```

## Resultado esperado

```
Ana: bruto R$ 3738.64, líquido R$ 2856.72
Bruno: bruto R$ 1800.00, líquido R$ 1602.00
Carla: bruto R$ 8272.73, líquido R$ 5522.00
```

## Critério de "pronto"

- [ ] Nenhuma variável ou função tem nome opaco
- [ ] A função principal está dividida em pelo menos 3 funções menores
- [ ] Magic numbers (220, 1.5, 0.11, 800, 189.59, 2259.20, 0.075...) viraram constantes nomeadas
- [ ] Código continua produzindo o mesmo resultado

---
