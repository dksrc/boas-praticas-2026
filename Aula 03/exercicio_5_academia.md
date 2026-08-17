# Exercício 5 - Academia (geração de planos)

## Sua tarefa

Você recebeu uma função que **funciona**, mas é difícil de ler. Ela gera planos personalizados de academia baseado no perfil do aluno.

Refatore aplicando o que aprendeu hoje:

1. **Renomeie** tudo que tiver nome ruim (variáveis, função, parâmetros).
2. **Quebre a função grande** em funções menores com Extract Method.
3. **Use F2 no VSCode** pra renomear sem quebrar nada.
4. **Rode o código antes e depois** pra confirmar que continua funcionando.

---

## Código original (`exercicio_5_academia.py`):

```python
"""
Exercício 5 - Geração de plano de treino

A função gp(a) recebe um aluno com:
    {"nome": str, "idade": int, "peso": float, "altura": float, "obj": str, "nivel": str}

Obj pode ser: "perder_peso", "ganhar_massa", "manter"
Nível pode ser: "iniciante", "intermediario", "avancado"

Calcula IMC, classifica e gera recomendação de treino + dias por semana.
"""


def gp(a):
    p = a["peso"]
    al = a["altura"]
    imc = p / (al ** 2)
    if imc < 18.5:
        cl = "abaixo_peso"
    elif imc < 25:
        cl = "normal"
    elif imc < 30:
        cl = "sobrepeso"
    else:
        cl = "obesidade"
    if a["obj"] == "perder_peso":
        t = "Cardio + funcional"
        if a["nivel"] == "iniciante":
            d = 3
        elif a["nivel"] == "intermediario":
            d = 4
        else:
            d = 5
    elif a["obj"] == "ganhar_massa":
        t = "Musculação pesada + suplementação"
        if a["nivel"] == "iniciante":
            d = 3
        elif a["nivel"] == "intermediario":
            d = 4
        else:
            d = 6
    else:
        t = "Musculação leve + alongamento"
        if a["nivel"] == "iniciante":
            d = 2
        elif a["nivel"] == "intermediario":
            d = 3
        else:
            d = 4
    if a["idade"] > 60:
        d = max(d - 1, 2)
    return {
        "nome": a["nome"],
        "imc": imc,
        "classificacao": cl,
        "treino": t,
        "dias_semana": d,
    }


if __name__ == "__main__":
    alunos = [
        {"nome": "Ana", "idade": 28, "peso": 65, "altura": 1.65, "obj": "perder_peso", "nivel": "intermediario"},
        {"nome": "Bruno", "idade": 35, "peso": 80, "altura": 1.78, "obj": "ganhar_massa", "nivel": "avancado"},
        {"nome": "Sr. Carlos", "idade": 68, "peso": 75, "altura": 1.70, "obj": "manter", "nivel": "intermediario"},
    ]
    for a in alunos:
        r = gp(a)
        print(f"{r['nome']}: IMC {r['imc']:.2f} ({r['classificacao']}), "
              f"{r['treino']}, {r['dias_semana']} dias/semana")
```

## Resultado esperado

```
Ana: IMC 23.88 (normal), Cardio + funcional, 4 dias/semana
Bruno: IMC 25.25 (sobrepeso), Musculação pesada + suplementação, 6 dias/semana
Sr. Carlos: IMC 25.95 (sobrepeso), Musculação leve + alongamento, 2 dias/semana
```

## Critério de "pronto"

- [ ] Nenhuma variável ou função tem nome opaco
- [ ] A função principal está dividida em pelo menos 3 funções menores
- [ ] Magic numbers (18.5, 25, 30, 60, 2) viraram constantes nomeadas
- [ ] Código continua produzindo o mesmo resultado

---
