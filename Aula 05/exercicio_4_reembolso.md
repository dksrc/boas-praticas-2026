# Exercício 4 - Cálculo de Reembolso

## Sua tarefa

### Nome: GUILHERME VICENTE DOS SANTOS

Você recebeu uma função que **funciona**, mas tem **vários problemas misturados**. Calcula o reembolso de uma compra conforme prazo, categoria e status do cliente.

Este código junta tudo que vimos hoje. Você vai precisar:

1. **Configurar um logger** e trocar todos os `print` por chamadas de logger.
2. **Escolher o nível certo** de cada mensagem (DEBUG / INFO / WARNING / ERROR / CRITICAL) - pense na gravidade de cada uma, não troque no automático.
3. **Proteger os dados sensíveis**: tem dado pessoal sendo logado (procure com atenção - nem tudo está óbvio). Mascare, troque por um identificador, ou não logue.
4. **Eliminar a duplicação** (DRY): há lógica repetida em mais de um lugar. Encontre e centralize.

> **Atenção:** os problemas não estão sinalizados no código. Faz parte do exercício **identificar** onde cada um está. Leia com cuidado.

---

## Código original (`exercicio_4_reembolso.py`):

```python
def calcular_reembolso(compra, cliente):
    print("Reembolso para " + cliente["nome"] + " cartao " + cliente["numero_cartao"])
    valor = compra["valor"]
    if compra["dias_desde_compra"] > 30:
        print("Fora do prazo")
        return 0

    if compra["categoria"] == "eletronico":
        taxa = valor * 0.10
        reembolso = valor - taxa
    elif compra["categoria"] == "vestuario":
        taxa = valor * 0.10
        reembolso = valor - taxa
    else:
        reembolso = valor

    if cliente["premium"]:
        reembolso = valor
    print("Reembolso de " + str(reembolso) + " para cartao " + cliente["numero_cartao"])
    return reembolso

if __name__ == "__main__":
    compra = {"valor": 1000, "dias_desde_compra": 10, "categoria": "eletronico"}
    cliente = {"nome": "Duda", "numero_cartao": "9999888877776666", "premium": False}
    print("Resultado:", calcular_reembolso(compra, cliente))
```

## Critério de "pronto"

- [ ] Nenhum `print` sobrou - tudo é logger
- [ ] Cada mensagem está num nível coerente com sua gravidade
- [ ] Nenhum dado sensível (CPF, cartão, email, telefone, conta, endereço, diagnóstico...) aparece cru no log
- [ ] A lógica duplicada foi centralizada num único lugar
- [ ] O resultado retornado pela função continua **idêntico** ao original (rode antes e depois pra confirmar)

---
