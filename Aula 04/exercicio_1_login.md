# Exercício 1 - Sistema de Login

## Sua tarefa

Você recebeu uma função que **funciona**, mas tem **aninhamento excessivo** (muitos `if` dentro de `if`). Ela autentica um usuário verificando existência, status e senha.

Refatore aplicando o que aprendeu hoje:

1. **Achate o aninhamento** com guard clauses (early return): inverta as condições e trate cada problema cedo, saindo da função.
2. **Deixe o caminho feliz no nível 0** de indentação, no fim.
3. **Trate os erros com intenção**: nada de `except: pass`. Se houver, troque por captura específica ou remova.
4. **Rode o código antes e depois** pra confirmar que o comportamento continua idêntico.

---

## Código original (`exercicio_1_login.py`):

```python
def autenticar(usuario, senha):
    if usuario is not None:
        if usuario in BANCO:
            if BANCO[usuario]["ativo"]:
                if BANCO[usuario]["senha"] == senha:
                    return "Login OK"
                else:
                    return "Senha incorreta"
            else:
                return "Usuário bloqueado"
        else:
            return "Usuário não existe"
    else:
        return "Usuário nulo"

BANCO = {"ana": {"senha": "123", "ativo": True}, "bruno": {"senha": "abc", "ativo": False}}
if __name__ == "__main__":
    print(autenticar("ana", "123"))
    print(autenticar("bruno", "abc"))
    print(autenticar("carla", "x"))
```

## Critério de "pronto"

- [ ] Nenhum nível de aninhamento desnecessário (o caminho feliz está no nível 0)
- [ ] Cada validação é uma guard clause com early return
- [ ] Os `else` desnecessários foram removidos
- [ ] Mensagens de erro/validação continuam claras
- [ ] O código produz exatamente o mesmo resultado de antes

---
