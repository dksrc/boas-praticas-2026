# Exercício 1 - Sistema de Matrícula

## Sua tarefa

### Nome: DÉDALO ARAÚJO DE AMORIM

Você recebeu uma função que **funciona**, mas tem **vários problemas misturados**. Matricula um aluno num curso, com descontos e formas de pagamento.

Este código junta tudo que vimos hoje. Você vai precisar:

1. **Configurar um logger** e trocar todos os `print` por chamadas de logger.
2. **Escolher o nível certo** de cada mensagem (DEBUG / INFO / WARNING / ERROR / CRITICAL) - pense na gravidade de cada uma, não troque no automático.
3. **Proteger os dados sensíveis**: tem dado pessoal sendo logado (procure com atenção - nem tudo está óbvio). Mascare, troque por um identificador, ou não logue.
4. **Eliminar a duplicação** (DRY): há lógica repetida em mais de um lugar. Encontre e centralize.

> **Atenção:** os problemas não estão sinalizados no código. Faz parte do exercício **identificar** onde cada um está. Leia com cuidado.

---

## Código original (`exercicio_1_matricula.py`):

```python
def matricular_aluno(aluno, curso):
    print("Matriculando " + aluno["nome"] + " (CPF " + aluno["cpf"] + ") no curso " + curso["nome"])

    valor = curso["valor_base"]
    if aluno["tipo"] == "bolsista":
        valor = valor - (valor * 0.5)
    print("Valor com desconto bolsista: " + str(valor))

    if aluno["pagamento"] == "avista":
        desconto = valor * 0.05
        valor_final = valor - desconto
    elif aluno["pagamento"] == "parcelado":
        desconto = valor * 0.05
        valor_final = valor - desconto
        valor_final = valor_final + (valor_final * 0.02)
    else:
        print("Forma de pagamento invalida")
        return None

    print("Aluno " + aluno["nome"] + " matriculado. Email de confirmacao enviado para " + aluno["email"])
    print("Valor final: " + str(valor_final))
    return valor_final

if __name__ == "__main__":
    aluno1 = {"nome": "Ana", "cpf": "11122233344", "email": "ana@x.com", "tipo": "bolsista", "pagamento": "avista"}
    curso1 = {"nome": "Python", "valor_base": 1000}
    print("Resultado:", matricular_aluno(aluno1, curso1))
```

## Critério de "pronto"

- [ ] Nenhum `print` sobrou - tudo é logger
- [ ] Cada mensagem está num nível coerente com sua gravidade
- [ ] Nenhum dado sensível (CPF, cartão, email, telefone, conta, endereço, diagnóstico...) aparece cru no log
- [ ] A lógica duplicada foi centralizada num único lugar
- [ ] O resultado retornado pela função continua **idêntico** ao original (rode antes e depois pra confirmar)

---
