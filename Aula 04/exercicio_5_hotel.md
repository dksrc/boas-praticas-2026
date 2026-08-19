# Exercício 5 - Reserva de Hotel

## Sua tarefa

Você recebeu uma função que **funciona**, mas tem **aninhamento excessivo** (muitos `if` dentro de `if`). Ela valida e efetua a reserva de um quarto de hotel.

Refatore aplicando o que aprendeu hoje:

1. **Achate o aninhamento** com guard clauses (early return): inverta as condições e trate cada problema cedo, saindo da função.
2. **Deixe o caminho feliz no nível 0** de indentação, no fim.
3. **Trate os erros com intenção**: nada de `except: pass`. Se houver, troque por captura específica ou remova.
4. **Rode o código antes e depois** pra confirmar que o comportamento continua idêntico.

---

## Código original (`exercicio_5_hotel.py`):

```python
def reservar(hospede, quarto, noites):
    if hospede is not None:
        if quarto["disponivel"]:
            if noites > 0:
                if noites <= 30:
                    total = quarto["diaria"] * noites
                    return f"Reserva OK: R$ {total:.2f}"
                else:
                    return "Máximo de 30 noites"
            else:
                return "Noites inválidas"
        else:
            return "Quarto ocupado"
    else:
        return "Hóspede inválido"

if __name__ == "__main__":
    print(reservar({"nome": "Ana"}, {"disponivel": True, "diaria": 200}, 3))
    print(reservar({"nome": "Ana"}, {"disponivel": True, "diaria": 200}, 40))
    print(reservar({"nome": "Ana"}, {"disponivel": False, "diaria": 200}, 3))
```

## Critério de "pronto"

- [ ] Nenhum nível de aninhamento desnecessário (o caminho feliz está no nível 0)
- [ ] Cada validação é uma guard clause com early return
- [ ] Os `else` desnecessários foram removidos
- [ ] Mensagens de erro/validação continuam claras
- [ ] O código produz exatamente o mesmo resultado de antes

---
