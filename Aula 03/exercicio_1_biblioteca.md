# Exercício 1 - Sistema de Biblioteca

## Sua tarefa

Você recebeu uma função que **funciona**, mas é difícil de ler. Ela calcula multas de livros atrasados numa biblioteca.

Refatore aplicando o que aprendeu hoje:

1. **Renomeie** tudo que tiver nome ruim (variáveis, função, parâmetros).
2. **Quebre a função grande** em funções menores com Extract Method.
3. **Use F2 no VSCode** pra renomear sem quebrar nada.
4. **Rode o código antes e depois** pra confirmar que continua funcionando.

---

## Código original (`exercicio_1_biblioteca.py`):

```python
"""
Exercício 1 - Sistema de multas de biblioteca

A função calcular(l, h) recebe uma lista de livros emprestados e a data de hoje, e retorna o valor total de multas dos livros atrasados.

Cada livro é uma tupla: (titulo, data_devolucao, tipo)
Tipos: "normal", "raro", "didatico"

Multa: R$ 2 por dia para normal, R$ 5 para raro, R$ 1 para didático.
Acima de 30 dias de atraso: multa dobra.
"""

from datetime import date


def calcular(l, h):
    m = 0
    for i in l:
        d = (h - i[1]).days
        if d > 0:
            if i[2] == "normal":
                v = d * 2
            elif i[2] == "raro":
                v = d * 5
            elif i[2] == "didatico":
                v = d * 1
            else:
                v = 0
            if d > 30:
                v = v * 2
            m = m + v
    return m


if __name__ == "__main__":
    livros = [
        ("Dom Casmurro", date(2025, 1, 10), "normal"),
        ("Manuscrito Raro", date(2024, 11, 5), "raro"),
        ("Cálculo Vol 1", date(2025, 2, 20), "didatico"),
        ("Livro em Dia", date(2025, 5, 15), "normal"),
    ]
    hoje = date(2025, 5, 1)
    total = calcular(livros, hoje)
    print(f"Multa total: R$ {total:.2f}")
```

## Resultado esperado

```
Multa total: R$ 2354.00
```

## Critério de "pronto"

- [ ] Nenhuma variável ou função tem nome opaco
- [ ] A função principal está dividida em pelo menos 2 funções menores
- [ ] Magic numbers (2, 5, 1, 30) viraram constantes nomeadas
- [ ] Código continua produzindo o mesmo resultado

---
