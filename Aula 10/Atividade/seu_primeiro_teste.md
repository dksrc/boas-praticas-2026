# Atividade - Escrevendo seus primeiros testes

Você recebeu uma função pronta. Sua missão é escrever **testes** para ela, cobrindo três tipos de caso: **feliz**, **de borda** e **de erro**.

---

## A função a testar

Crie um arquivo `classificador.py` com esta função:

```python
def classificar_idade(idade):
    if idade < 0:
        raise ValueError("Idade não pode ser negativa")
    if idade < 18:
        return "menor"
    elif idade < 60:
        return "adulto"
    else:
        return "idoso"
```

**O que ela faz:**

- Idade abaixo de 0 → levanta um erro (`ValueError`)
- Idade de 0 a 17 → retorna `"menor"`
- Idade de 18 a 59 → retorna `"adulto"`
- Idade de 60 em diante → retorna `"idoso"`

---

## Sua tarefa

Crie o arquivo `tests/test_classificador.py` e escreva testes cobrindo:

### 1. Caso feliz (valores típicos de cada faixa)

Um valor normal de cada categoria. Ex: uma criança deve ser "menor", um adulto deve ser "adulto", um idoso deve ser "idoso".

### 2. Casos de borda (os limites das faixas)

Aqui é onde os bugs se escondem! Teste os **limites exatos**:

- O que acontece **aos 18 anos**? (vira adulto ou ainda é menor?)
- E **aos 17**? E **aos 60**? E **aos 59**?
- E o **zero**?

Pense: cada `<` na função é uma fronteira. Teste os dois lados dela.

### 3. Caso de erro (entrada inválida)

A função deve levantar `ValueError` para idade negativa. Teste que ela **realmente levanta** o erro.

> Dica para testar exceção - use o `pytest.raises`:
>
> ```python
> import pytest
>
> def test_idade_negativa_levanta_erro():
>     with pytest.raises(ValueError):
>         classificar_idade(-5)
> ```

---

## Lembre das regras do bom teste

- **AAA:** arrange, act, assert (mesmo que curto).
- **Assert de verdade:** sem assert, o teste não verifica nada!
- **Nome descritivo:** `test_borda_18_vira_adulto` conta a história; `test_1` não.
- **Isolado:** cada teste roda sozinho.

---

## Como rodar

```bash
pytest -v
```

Todos os seus testes devem aparecer em verde (PASSED).

---

## Critério de conclusão

- [ ] Pelo menos 3 testes de caso feliz (um por faixa)
- [ ] Pelo menos 3 testes de borda (nos limites 18 e 60)
- [ ] Pelo menos 1 teste de erro (idade negativa com `pytest.raises`)
- [ ] Todos os testes têm `assert` (ou `pytest.raises`) de verdade
- [ ] Nomes descritivos
- [ ] `pytest -v` mostra tudo verde

---

## Deu erro? Dúvidas comuns

**"ImportError: cannot import name classificar_idade"**
Confira que o `classificador.py` está na raiz do projeto e que você importou certo no topo do teste: `from classificador import classificar_idade`.

**"O pytest não encontra meus testes"**
Confirme: o arquivo começa com `test_`, as funções começam com `test_`, e você está rodando o `pytest` na pasta do projeto.

**"Como testo que a função levanta um erro?"**
Use o `with pytest.raises(ValueError):` como no exemplo. Ele verifica que o erro **aconteceu** - se a função NÃO levantar o erro, o teste falha.

**"Meu teste de borda passou, mas não sei se testei o certo"**
Pergunte-se: testei os DOIS lados de cada fronteira? Aos 17 (menor) e aos 18 (adulto)? Aos 59 (adulto) e aos 60 (idoso)? É nos limites que os bugs aparecem.

---
