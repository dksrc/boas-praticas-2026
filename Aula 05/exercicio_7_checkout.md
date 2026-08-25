# Exercício 7 - Checkout de E-commerce

## Sua tarefa

### Nome: CARLOS HENRIQUE BATISTA DE ANICETO

Você recebeu uma função que **funciona**, mas tem **vários problemas misturados**. Finaliza uma compra: subtotal, desconto, frete e cobrança no cartão.

Este código junta tudo que vimos hoje. Você vai precisar:

1. **Configurar um logger** e trocar todos os `print` por chamadas de logger.
2. **Escolher o nível certo** de cada mensagem (DEBUG / INFO / WARNING / ERROR / CRITICAL) - pense na gravidade de cada uma, não troque no automático.
3. **Proteger os dados sensíveis**: tem dado pessoal sendo logado (procure com atenção - nem tudo está óbvio). Mascare, troque por um identificador, ou não logue.
4. **Eliminar a duplicação** (DRY): há lógica repetida em mais de um lugar. Encontre e centralize.

> **Atenção:** os problemas não estão sinalizados no código. Faz parte do exercício **identificar** onde cada um está. Leia com cuidado.

---

## Código original (`exercicio_7_checkout.py`):

```python
def finalizar_compra(carrinho, cliente):
    print("Checkout de " + cliente["email"] + " endereco " + cliente["endereco_completo"])
    subtotal = 0
    for item in carrinho["itens"]:
        subtotal = subtotal + item["preco"]
    print("Subtotal: " + str(subtotal))
    if cliente["primeira_compra"]:
        subtotal = subtotal - (subtotal * 0.15)
    if carrinho["cupom"] == "FRETE":
        frete = 0
    else:
        frete = 25
    total = subtotal + frete
    print("Cobrando cartao " + cliente["cartao"] + " valor " + str(total))
    if total > cliente["limite"]:
        print("Limite insuficiente no cartao " + cliente["cartao"])
        return None
    print("Compra finalizada para " + cliente["email"])
    return total

if __name__ == "__main__":
    carrinho = {"itens": [{"preco": 300}, {"preco": 200}], "cupom": "FRETE"}
    cliente = {"email": "f@x.com", "endereco_completo": "Rua X 123", "cartao": "4444333322221111", "primeira_compra": True, "limite": 5000}
    print("Resultado:", finalizar_compra(carrinho, cliente))
```

## Critério de "pronto"

- [ ] Nenhum `print` sobrou - tudo é logger
- [ ] Cada mensagem está num nível coerente com sua gravidade
- [ ] Nenhum dado sensível (CPF, cartão, email, telefone, conta, endereço, diagnóstico...) aparece cru no log
- [ ] A lógica duplicada foi centralizada num único lugar
- [ ] O resultado retornado pela função continua **idêntico** ao original (rode antes e depois pra confirmar)

---
