# Exercício 5 - Envio de Notificações

## Sua tarefa

### Nome: ALUIZIO ANTÔNIO ALVES MENEZES

Você recebeu uma função que **funciona**, mas tem **vários problemas misturados**. Envia uma notificação por SMS ou WhatsApp, calculando o custo.

Este código junta tudo que vimos hoje. Você vai precisar:

1. **Configurar um logger** e trocar todos os `print` por chamadas de logger.
2. **Escolher o nível certo** de cada mensagem (DEBUG / INFO / WARNING / ERROR / CRITICAL) - pense na gravidade de cada uma, não troque no automático.
3. **Proteger os dados sensíveis**: tem dado pessoal sendo logado (procure com atenção - nem tudo está óbvio). Mascare, troque por um identificador, ou não logue.
4. **Eliminar a duplicação** (DRY): há lógica repetida em mais de um lugar. Encontre e centralize.

> **Atenção:** os problemas não estão sinalizados no código. Faz parte do exercício **identificar** onde cada um está. Leia com cuidado.

---

## Código original (`exercicio_5_notificacao.py`):

```python
def enviar_notificacao(usuario, mensagem):
    print("Enviando para " + usuario["telefone"] + ": " + mensagem)
    if usuario["canal"] == "sms":
        custo = 0.10
        if len(mensagem) > 160:
            custo = custo * 2
    elif usuario["canal"] == "whatsapp":
        custo = 0.05
        if len(mensagem) > 160:
            custo = custo * 2
    else:
        print("Canal desconhecido")
        return None
    if not usuario["ativo"]:
        print("Usuario inativo, nao enviado")
        return None
    print("Notificacao enviada para " + usuario["telefone"] + " custo " + str(custo))
    return custo

if __name__ == "__main__":
    u = {"telefone": "82999998888", "canal": "sms", "ativo": True}
    print("Resultado:", enviar_notificacao(u, "Ola"))
```

## Critério de "pronto"

- [ ] Nenhum `print` sobrou - tudo é logger
- [ ] Cada mensagem está num nível coerente com sua gravidade
- [ ] Nenhum dado sensível (CPF, cartão, email, telefone, conta, endereço, diagnóstico...) aparece cru no log
- [ ] A lógica duplicada foi centralizada num único lugar
- [ ] O resultado retornado pela função continua **idêntico** ao original (rode antes e depois pra confirmar)

---
