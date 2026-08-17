# Exercício 6 - Hospital (sistema de triagem)

## Sua tarefa

Você recebeu uma função que **funciona**, mas é difícil de ler. Ela faz triagem de pacientes na recepção de um pronto-socorro.

Refatore aplicando o que aprendeu hoje:

1. **Renomeie** tudo que tiver nome ruim (variáveis, função, parâmetros).
2. **Quebre a função grande** em funções menores com Extract Method.
3. **Use F2 no VSCode** pra renomear sem quebrar nada.
4. **Rode o código antes e depois** pra confirmar que continua funcionando.

---

## Código original (`exercicio_6_hospital.py`):

```python
"""
Exercício 6 - Sistema de triagem hospitalar (modelo de Manchester simplificado)

A função tr(p) recebe um paciente:
    {"nome": str, "idade": int, "fc": int (freq. cardíaca),
     "pas": int (pressão sistólica), "temp": float, "sint": list[str]}

Retorna: cor da triagem + tempo máximo de espera (em minutos)
- VERMELHO (emergência): atendimento imediato
- LARANJA (muito urgente): até 10 min
- AMARELO (urgente): até 60 min
- VERDE (pouco urgente): até 120 min
- AZUL (não urgente): até 240 min
"""


def tr(p):
    s = p["sint"]
    fc = p["fc"]
    pas = p["pas"]
    t = p["temp"]
    if "parada_cardiaca" in s or "inconsciente" in s or pas < 60:
        c = "VERMELHO"
        e = 0
    elif "dor_no_peito" in s or "falta_de_ar" in s or fc > 130 or fc < 40 or pas > 180:
        c = "LARANJA"
        e = 10
    elif "febre_alta" in s or t > 39.5 or "vomito_persistente" in s or (p["idade"] > 70 and t > 38):
        c = "AMARELO"
        e = 60
    elif "dor_moderada" in s or t > 37.8 or "tontura" in s:
        c = "VERDE"
        e = 120
    else:
        c = "AZUL"
        e = 240
    return {"nome": p["nome"], "cor": c, "espera_max_min": e}


if __name__ == "__main__":
    pacientes = [
        {"nome": "Ana", "idade": 45, "fc": 75, "pas": 120, "temp": 36.5, "sint": ["dor_de_cabeca_leve"]},
        {"nome": "Bruno", "idade": 60, "fc": 140, "pas": 100, "temp": 37.0, "sint": ["dor_no_peito"]},
        {"nome": "Dona Lúcia", "idade": 78, "fc": 90, "pas": 130, "temp": 38.5, "sint": ["tosse"]},
        {"nome": "Pedro", "idade": 30, "fc": 80, "pas": 50, "temp": 36.0, "sint": ["inconsciente"]},
    ]
    for p in pacientes:
        r = tr(p)
        print(f"{r['nome']}: {r['cor']} (espera máx. {r['espera_max_min']} min)")
```

## Resultado esperado

```
Ana: AZUL (espera máx. 240 min)
Bruno: LARANJA (espera máx. 10 min)
Dona Lúcia: AMARELO (espera máx. 60 min)
Pedro: VERMELHO (espera máx. 0 min)
```

## Critério de "pronto"

- [ ] Nenhuma variável ou função tem nome opaco
- [ ] A função principal está dividida em pelo menos 3 funções menores
- [ ] Magic numbers (60, 130, 40, 180, 39.5, 70, 38, 37.8) viraram constantes nomeadas
- [ ] Tempos de espera (0, 10, 60, 120, 240) viraram constantes
- [ ] Código continua produzindo o mesmo resultado

---
