# Exercício 3 - Autenticação com Tentativas

## Sua tarefa

### Nome: MATHEUS FERREIRA DA SILVA BARROS

Você recebeu uma função que **funciona**, mas tem **vários problemas misturados**. Autentica um usuário, contando tentativas e bloqueando após 3 falhas.

Este código junta tudo que vimos hoje. Você vai precisar:

1. **Configurar um logger** e trocar todos os `print` por chamadas de logger.
2. **Escolher o nível certo** de cada mensagem (DEBUG / INFO / WARNING / ERROR / CRITICAL) - pense na gravidade de cada uma, não troque no automático.
3. **Proteger os dados sensíveis**: tem dado pessoal sendo logado (procure com atenção - nem tudo está óbvio). Mascare, troque por um identificador, ou não logue.
4. **Eliminar a duplicação** (DRY): há lógica repetida em mais de um lugar. Encontre e centralize.

> **Atenção:** os problemas não estão sinalizados no código. Faz parte do exercício **identificar** onde cada um está. Leia com cuidado.

## Tempo: 40 minutos

---

## Código original (`exercicio_3_login.py`):

```python
def autenticar(usuario, senha_digitada):
    print("Tentativa de login de " + usuario["email"] + " com senha " + senha_digitada)
    if usuario["bloqueado"]:
        print("Usuario bloqueado")
        return "bloqueado"
    if usuario["senha"] != senha_digitada:
        usuario["tentativas"] = usuario["tentativas"] + 1
        print("Senha incorreta. Tentativa " + str(usuario["tentativas"]))
        if usuario["tentativas"] >= 3:
            usuario["bloqueado"] = True
            print("Usuario bloqueado apos 3 tentativas: " + usuario["email"])
        return "senha_incorreta"
    print("Login bem sucedido para " + usuario["email"] + " token " + usuario["token"])
    return "sucesso"

if __name__ == "__main__":
    u = {"email": "c@x.com", "senha": "abc123", "token": "tok_secreto_xyz", "bloqueado": False, "tentativas": 0}
    print("R1:", autenticar(u, "errada"))
    print("R2:", autenticar(u, "abc123"))
```

## Critério de "pronto"

- [ ] Nenhum `print` sobrou - tudo é logger
- [ ] Cada mensagem está num nível coerente com sua gravidade
- [ ] Nenhum dado sensível (CPF, cartão, email, telefone, conta, endereço, diagnóstico...) aparece cru no log
- [ ] A lógica duplicada foi centralizada num único lugar
- [ ] O resultado retornado pela função continua **idêntico** ao original (rode antes e depois pra confirmar)

---
