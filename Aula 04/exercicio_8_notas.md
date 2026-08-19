# Exercício 8 - Média de Notas (entrada do usuário)

## Sua tarefa

Você recebeu uma função que **funciona**, mas tem **aninhamento excessivo** (muitos `if` dentro de `if`). Ela calcula a média de uma lista de notas digitadas. **O foco aqui é o tratamento de erro: troque o `except` genérico por um específico.**

Refatore aplicando o que aprendeu hoje:

1. **Achate o aninhamento** com guard clauses (early return): inverta as condições e trate cada problema cedo, saindo da função.
2. **Deixe o caminho feliz no nível 0** de indentação, no fim.
3. **Trate os erros com intenção**: nada de `except: pass`. Se houver, troque por captura específica ou remova.
4. **Rode o código antes e depois** pra confirmar que o comportamento continua idêntico.

---

## Código original (`exercicio_8_notas.py`):

```python
def calcular_media_notas(entradas):
    if entradas is not None:
        if len(entradas) > 0:
            soma = 0
            for e in entradas:
                try:
                    soma = soma + float(e)
                except:
                    pass
            return soma / len(entradas)
        else:
            return "Lista vazia"
    else:
        return "Entrada inválida"

if __name__ == "__main__":
    print(calcular_media_notas(["8.0", "6.0", "10.0"]))
    print(calcular_media_notas([]))
    print(calcular_media_notas(None))
```

## Critério de "pronto"

- [ ] Nenhum nível de aninhamento desnecessário (o caminho feliz está no nível 0)
- [ ] Cada validação é uma guard clause com early return
- [ ] Os `else` desnecessários foram removidos
- [ ] Mensagens de erro/validação continuam claras
- [ ] O `except` genérico foi trocado por exceção específica (ou o try/except foi removido se não protegia de nada útil)
- [ ] O código produz exatamente o mesmo resultado de antes

---
