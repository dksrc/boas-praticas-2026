# Exercício 4 - Aprovação de Empréstimo

## Sua tarefa

Você recebeu uma função que **funciona**, mas tem **aninhamento excessivo** (muitos `if` dentro de `if`). Ela avalia e aprova (ou não) um empréstimo. **Contém um `except: pass` - resolva ele também.**

Refatore aplicando o que aprendeu hoje:

1. **Achate o aninhamento** com guard clauses (early return): inverta as condições e trate cada problema cedo, saindo da função.
2. **Deixe o caminho feliz no nível 0** de indentação, no fim.
3. **Trate os erros com intenção**: nada de `except: pass`. Se houver, troque por captura específica ou remova.
4. **Rode o código antes e depois** pra confirmar que o comportamento continua idêntico.

---

## Código original (`exercicio_4_emprestimo.py`):

```python
def aprovar_emprestimo(cliente, valor):
    if cliente is not None:
        if cliente["score"] >= 600:
            if valor > 0:
                try:
                    limite = cliente["renda"] * 10
                    if valor <= limite:
                        return "Empréstimo aprovado"
                    else:
                        return "Valor acima do limite"
                except:
                    pass
            else:
                return "Valor inválido"
        else:
            return "Score insuficiente"
    else:
        return "Cliente inválido"

if __name__ == "__main__":
    print(aprovar_emprestimo({"score": 700, "renda": 3000}, 20000))
    print(aprovar_emprestimo({"score": 700, "renda": 3000}, 50000))
    print(aprovar_emprestimo({"score": 500, "renda": 3000}, 10000))
```

## Critério de "pronto"

- [ ] Nenhum nível de aninhamento desnecessário (o caminho feliz está no nível 0)
- [ ] Cada validação é uma guard clause com early return
- [ ] Os `else` desnecessários foram removidos
- [ ] Mensagens de erro/validação continuam claras
- [ ] O `except` genérico foi trocado por exceção específica (ou o try/except foi removido se não protegia de nada útil)
- [ ] O código produz exatamente o mesmo resultado de antes

---
