# Exercício 7 - Envio de Encomenda

## Sua tarefa

Você recebeu uma função que **funciona**, mas tem **aninhamento excessivo** (muitos `if` dentro de `if`). Ela valida e calcula o envio de uma encomenda.

Refatore aplicando o que aprendeu hoje:

1. **Achate o aninhamento** com guard clauses (early return): inverta as condições e trate cada problema cedo, saindo da função.
2. **Deixe o caminho feliz no nível 0** de indentação, no fim.
3. **Trate os erros com intenção**: nada de `except: pass`. Se houver, troque por captura específica ou remova.
4. **Rode o código antes e depois** pra confirmar que o comportamento continua idêntico.

---

## Código original (`exercicio_7_correios.py`):

```python
def enviar_encomenda(pacote, endereco):
    if pacote is not None:
        if endereco is not None:
            if pacote["peso"] <= 30:
                if endereco["cep"] != "":
                    frete = pacote["peso"] * 2.5
                    return f"Envio OK: R$ {frete:.2f}"
                else:
                    return "CEP inválido"
            else:
                return "Peso acima do limite"
        else:
            return "Endereço inválido"
    else:
        return "Pacote inválido"

if __name__ == "__main__":
    print(enviar_encomenda({"peso": 10}, {"cep": "57000000"}))
    print(enviar_encomenda({"peso": 50}, {"cep": "57000000"}))
    print(enviar_encomenda({"peso": 10}, {"cep": ""}))
```

## Critério de "pronto"

- [ ] Nenhum nível de aninhamento desnecessário (o caminho feliz está no nível 0)
- [ ] Cada validação é uma guard clause com early return
- [ ] Os `else` desnecessários foram removidos
- [ ] Mensagens de erro/validação continuam claras
- [ ] O código produz exatamente o mesmo resultado de antes

---
