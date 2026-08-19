# Exercício 6 - Processamento de Pagamento

## Sua tarefa

Você recebeu uma função que **funciona**, mas tem **aninhamento excessivo** (muitos `if` dentro de `if`). Ela valida e processa um pagamento com cartão. **Contém um `except: pass` - resolva ele também.**

Refatore aplicando o que aprendeu hoje:

1. **Achate o aninhamento** com guard clauses (early return): inverta as condições e trate cada problema cedo, saindo da função.
2. **Deixe o caminho feliz no nível 0** de indentação, no fim.
3. **Trate os erros com intenção**: nada de `except: pass`. Se houver, troque por captura específica ou remova.
4. **Rode o código antes e depois** pra confirmar que o comportamento continua idêntico.

---

## Código original (`exercicio_6_pagamento.py`):

```python
def processar_pagamento(pedido, cartao):
    if pedido is not None:
        if cartao is not None:
            if not cartao["vencido"]:
                if cartao["limite"] >= pedido["valor"]:
                    try:
                        cartao["limite"] = cartao["limite"] - pedido["valor"]
                        return "Pagamento aprovado"
                    except:
                        pass
                else:
                    return "Limite insuficiente"
            else:
                return "Cartão vencido"
        else:
            return "Cartão inválido"
    else:
        return "Pedido inválido"

if __name__ == "__main__":
    print(processar_pagamento({"valor": 100}, {"vencido": False, "limite": 500}))
    print(processar_pagamento({"valor": 100}, {"vencido": True, "limite": 500}))
    print(processar_pagamento({"valor": 1000}, {"vencido": False, "limite": 500}))
```

## Critério de "pronto"

- [ ] Nenhum nível de aninhamento desnecessário (o caminho feliz está no nível 0)
- [ ] Cada validação é uma guard clause com early return
- [ ] Os `else` desnecessários foram removidos
- [ ] Mensagens de erro/validação continuam claras
- [ ] O `except` genérico foi trocado por exceção específica (ou o try/except foi removido se não protegia de nada útil)
- [ ] O código produz exatamente o mesmo resultado de antes

---
