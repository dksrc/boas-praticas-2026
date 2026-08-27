# Exercício 3 - Matrícula em Curso

## Sua tarefa

Você recebeu uma função que **funciona**, mas tem **aninhamento excessivo** (muitos `if` dentro de `if`). Ela valida e efetua a matrícula de um aluno em um curso.

Refatore aplicando o que aprendeu hoje:

1. **Achate o aninhamento** com guard clauses (early return): inverta as condições e trate cada problema cedo, saindo da função.
2. **Deixe o caminho feliz no nível 0** de indentação, no fim.
3. **Trate os erros com intenção**: nada de `except: pass`. Se houver, troque por captura específica ou remova.
4. **Rode o código antes e depois** pra confirmar que o comportamento continua idêntico.

---

## Código original (`exercicio_3_matricula.py`):

```python
def matricular(aluno, curso):
    if aluno is not None:
        if aluno["adimplente"]:
            if curso["vagas"] > 0:
                if not curso["trancado"]:
                    return "Matrícula efetuada"
                else:
                    return "Curso trancado"
            else:
                return "Sem vagas"
        else:
            return "Aluno inadimplente"
    else:
        return "Aluno inválido"

if __name__ == "__main__":
    print(matricular({"adimplente": True}, {"vagas": 5, "trancado": False}))
    print(matricular({"adimplente": True}, {"vagas": 0, "trancado": False}))
    print(matricular({"adimplente": False}, {"vagas": 5, "trancado": False}))
```

## Critério de "pronto"

- [ ] Nenhum nível de aninhamento desnecessário (o caminho feliz está no nível 0)
- [ ] Cada validação é uma guard clause com early return
- [ ] Os `else` desnecessários foram removidos
- [ ] Mensagens de erro/validação continuam claras
- [ ] O código produz exatamente o mesmo resultado de antes

---
