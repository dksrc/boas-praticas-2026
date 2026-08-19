# Exercício 2 - Rede Social (publicar post)

## Sua tarefa

Você recebeu uma função que **funciona**, mas tem **aninhamento excessivo** (muitos `if` dentro de `if`). Ela valida e publica um post numa rede social.

Refatore aplicando o que aprendeu hoje:

1. **Achate o aninhamento** com guard clauses (early return): inverta as condições e trate cada problema cedo, saindo da função.
2. **Deixe o caminho feliz no nível 0** de indentação, no fim.
3. **Trate os erros com intenção**: nada de `except: pass`. Se houver, troque por captura específica ou remova.
4. **Rode o código antes e depois** pra confirmar que o comportamento continua idêntico.

---

## Código original (`exercicio_2_rede_social.py`):

```python
def publicar(post, autor):
    if autor is not None:
        if autor["verificado"]:
            if post != "":
                if len(post) <= 280:
                    return "Post publicado"
                else:
                    return "Post muito longo"
            else:
                return "Post vazio"
        else:
            return "Autor não verificado"
    else:
        return "Autor inválido"

if __name__ == "__main__":
    print(publicar("Olá mundo", {"verificado": True}))
    print(publicar("x"*300, {"verificado": True}))
    print(publicar("", {"verificado": True}))
```

## Critério de "pronto"

- [ ] Nenhum nível de aninhamento desnecessário (o caminho feliz está no nível 0)
- [ ] Cada validação é uma guard clause com early return
- [ ] Os `else` desnecessários foram removidos
- [ ] Mensagens de erro/validação continuam claras
- [ ] O código produz exatamente o mesmo resultado de antes

---
