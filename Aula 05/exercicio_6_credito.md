# Exercício 6 - Análise de Crédito

## Sua tarefa

### Nome: ALAN PEDRO DIAS

Você recebeu uma função que **funciona**, mas tem **vários problemas misturados**. Analisa crédito de um cliente conforme score, renda e tipo.

Este código junta tudo que vimos hoje. Você vai precisar:

1. **Configurar um logger** e trocar todos os `print` por chamadas de logger.
2. **Escolher o nível certo** de cada mensagem (DEBUG / INFO / WARNING / ERROR / CRITICAL) - pense na gravidade de cada uma, não troque no automático.
3. **Proteger os dados sensíveis**: tem dado pessoal sendo logado (procure com atenção - nem tudo está óbvio). Mascare, troque por um identificador, ou não logue.
4. **Eliminar a duplicação** (DRY): há lógica repetida em mais de um lugar. Encontre e centralize.

> **Atenção:** os problemas não estão sinalizados no código. Faz parte do exercício **identificar** onde cada um está. Leia com cuidado.

---

## Código original (`exercicio_6_credito.py`):

```python
def analisar_credito(cliente, valor_solicitado):
    print("Analise de credito: " + cliente["nome"] + " CPF " + cliente["cpf"] + " renda " + str(cliente["renda"]))
    score = cliente["score"]
    if score < 300:
        print("Score muito baixo: " + str(score))
        return "negado"
    limite = cliente["renda"] * 5
    if cliente["tipo"] == "assalariado":
        limite = limite + (limite * 0.2)
    elif cliente["tipo"] == "autonomo":
        limite = limite + (limite * 0.2)
        limite = limite - (limite * 0.1)
    if valor_solicitado > limite:
        print("Valor " + str(valor_solicitado) + " acima do limite " + str(limite) + " para CPF " + cliente["cpf"])
        return "negado"
    print("Credito aprovado para " + cliente["nome"])
    return "aprovado"

if __name__ == "__main__":
    c = {"nome": "Edu", "cpf": "55566677788", "renda": 3000, "score": 700, "tipo": "assalariado"}
    print("Resultado:", analisar_credito(c, 10000))
```

## Critério de "pronto"

- [ ] Nenhum `print` sobrou - tudo é logger
- [ ] Cada mensagem está num nível coerente com sua gravidade
- [ ] Nenhum dado sensível (CPF, cartão, email, telefone, conta, endereço, diagnóstico...) aparece cru no log
- [ ] A lógica duplicada foi centralizada num único lugar
- [ ] O resultado retornado pela função continua **idêntico** ao original (rode antes e depois pra confirmar)

---
