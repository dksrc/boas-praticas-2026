# Exercício 2 - Sistema Escolar

## Sua tarefa

Você recebeu uma função que **funciona**, mas é difícil de ler. Ela calcula a situação final de alunos numa escola.

Refatore aplicando o que aprendeu hoje:

1. **Renomeie** tudo que tiver nome ruim (variáveis, função, parâmetros).
2. **Quebre a função grande** em funções menores com Extract Method.
3. **Use F2 no VSCode** pra renomear sem quebrar nada.
4. **Rode o código antes e depois** pra confirmar que continua funcionando.

---

## Código original (`exercicio_2_escola.py`):

```python
"""
Exercício 2 - Situação final de alunos

A função processa(a) recebe uma lista de alunos. Cada aluno é um dicionário:
    {"nome": str, "n": [nota1, nota2, nota3, nota4], "f": int_faltas}

Regras:
- Média >= 7.0 e faltas <= 15: APROVADO
- Média >= 5.0 e faltas <= 15: RECUPERAÇÃO
- Faltas > 15: REPROVADO POR FALTA (independente da média)
- Média < 5.0 e faltas <= 15: REPROVADO POR NOTA
"""


def processa(a):
    r = []
    for x in a:
        s = 0
        for n in x["n"]:
            s = s + n
        med = s / 4
        if x["f"] > 15:
            sit = "REPROVADO POR FALTA"
        else:
            if med >= 7.0:
                sit = "APROVADO"
            elif med >= 5.0:
                sit = "RECUPERACAO"
            else:
                sit = "REPROVADO POR NOTA"
        r.append({"nome": x["nome"], "media": med, "situacao": sit})
    return r


if __name__ == "__main__":
    alunos = [
        {"nome": "Ana", "n": [8.5, 9.0, 7.5, 8.0], "f": 5},
        {"nome": "Bruno", "n": [6.0, 5.5, 6.5, 5.0], "f": 10},
        {"nome": "Carla", "n": [9.0, 8.5, 9.5, 9.0], "f": 20},
        {"nome": "Diego", "n": [4.0, 3.5, 4.5, 5.0], "f": 8},
    ]
    resultado = processa(alunos)
    for r in resultado:
        print(f"{r['nome']}: média {r['media']:.2f} - {r['situacao']}")
```

## Resultado esperado

```
Ana: média 8.25 - APROVADO
Bruno: média 5.75 - RECUPERACAO
Carla: média 9.00 - REPROVADO POR FALTA
Diego: média 4.25 - REPROVADO POR NOTA
```

## Critério de "pronto"

- [ ] Nenhuma variável ou função tem nome opaco
- [ ] A função principal está dividida em pelo menos 2 funções menores
- [ ] Magic numbers (7.0, 5.0, 15, 4) viraram constantes nomeadas
- [ ] Código continua produzindo o mesmo resultado

---
