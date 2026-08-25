# Exercício 8 - Registro de Consulta Médica

## Sua tarefa

### Nome: ANTONIO CARLOS MELO XAVIER

Você recebeu uma função que **funciona**, mas tem **vários problemas misturados**. Registra uma consulta médica e calcula o valor conforme convênio.

Este código junta tudo que vimos hoje. Você vai precisar:

1. **Configurar um logger** e trocar todos os `print` por chamadas de logger.
2. **Escolher o nível certo** de cada mensagem (DEBUG / INFO / WARNING / ERROR / CRITICAL) - pense na gravidade de cada uma, não troque no automático.
3. **Proteger os dados sensíveis**: tem dado pessoal sendo logado (procure com atenção - nem tudo está óbvio). Mascare, troque por um identificador, ou não logue.
4. **Eliminar a duplicação** (DRY): há lógica repetida em mais de um lugar. Encontre e centralize.

> **Atenção:** os problemas não estão sinalizados no código. Faz parte do exercício **identificar** onde cada um está. Leia com cuidado.

---

## Código original (`exercicio_8_consulta.py`):

```python
def registrar_consulta(paciente, consulta):
    print("Consulta de " + paciente["nome"] + " CPF " + paciente["cpf"] + " diagnostico: " + consulta["diagnostico"])
    valor = consulta["valor_base"]
    if paciente["tem_convenio"]:
        if paciente["tipo_convenio"] == "basico":
            valor = valor - (valor * 0.3)
        elif paciente["tipo_convenio"] == "premium":
            valor = valor - (valor * 0.3)
            valor = valor - (valor * 0.2)
    if consulta["retorno"]:
        valor = 0
    print("Valor da consulta de " + paciente["nome"] + ": " + str(valor))
    return valor

if __name__ == "__main__":
    p = {"nome": "Gil", "cpf": "99988877766", "tem_convenio": True, "tipo_convenio": "basico"}
    c = {"valor_base": 200, "diagnostico": "gripe", "retorno": False}
    print("Resultado:", registrar_consulta(p, c))
```

## Critério de "pronto"

- [ ] Nenhum `print` sobrou - tudo é logger
- [ ] Cada mensagem está num nível coerente com sua gravidade
- [ ] Nenhum dado sensível (CPF, cartão, email, telefone, conta, endereço, diagnóstico...) aparece cru no log
- [ ] A lógica duplicada foi centralizada num único lugar
- [ ] O resultado retornado pela função continua **idêntico** ao original (rode antes e depois pra confirmar)

---
