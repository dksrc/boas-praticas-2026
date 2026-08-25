# Exercício 2 - Folha de Pagamento

## Sua tarefa

### Nome: ALEX SANDRO RODRIGUES NOBRE JUNIOR e ANTONIO ANDRADE GOMES JÚNIOR

Você recebeu uma função que **funciona**, mas tem **vários problemas misturados**. Processa a folha de pagamento de um funcionário (horas extras, INSS, IRRF).

Este código junta tudo que vimos hoje. Você vai precisar:

1. **Configurar um logger** e trocar todos os `print` por chamadas de logger.
2. **Escolher o nível certo** de cada mensagem (DEBUG / INFO / WARNING / ERROR / CRITICAL) - pense na gravidade de cada uma, não troque no automático.
3. **Proteger os dados sensíveis**: tem dado pessoal sendo logado (procure com atenção - nem tudo está óbvio). Mascare, troque por um identificador, ou não logue.
4. **Eliminar a duplicação** (DRY): há lógica repetida em mais de um lugar. Encontre e centralize.

> **Atenção:** os problemas não estão sinalizados no código. Faz parte do exercício **identificar** onde cada um está. Leia com cuidado.

---

## Código original (`exercicio_2_folha.py`):

```python
def processar_folha(funcionario):
    print("Processando folha de " + funcionario["nome"] + " - conta " + funcionario["conta_bancaria"])
    salario = funcionario["salario_base"]

    if funcionario["horas_extras"] > 0:
        valor_hora = salario / 220
        salario = salario + (funcionario["horas_extras"] * valor_hora * 1.5)
    print("Salario com horas extras: " + str(salario))

    inss = salario * 0.11
    salario_liquido = salario - inss
    print("INSS descontado: " + str(inss))

    if salario > 5000:
        irrf = salario * 0.275
        salario_liquido = salario_liquido - irrf
    print("Salario liquido de " + funcionario["nome"] + ": " + str(salario_liquido))
    return salario_liquido

if __name__ == "__main__":
    f = {"nome": "Bruno", "conta_bancaria": "12345-6", "salario_base": 6000, "horas_extras": 10}
    print("Resultado:", round(processar_folha(f), 2))
```

## Critério de "pronto"

- [ ] Nenhum `print` sobrou - tudo é logger
- [ ] Cada mensagem está num nível coerente com sua gravidade
- [ ] Nenhum dado sensível (CPF, cartão, email, telefone, conta, endereço, diagnóstico...) aparece cru no log
- [ ] A lógica duplicada foi centralizada num único lugar
- [ ] O resultado retornado pela função continua **idêntico** ao original (rode antes e depois pra confirmar)

---
