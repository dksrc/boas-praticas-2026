# Exercício 5 - Serviço de Notificação

## Sua tarefa

### Nome: ALUIZIO ANTÔNIO ALVES MENEZES

Você recebeu uma classe que **funciona**, mas viola dois princípios do SOLID. Determina prefixo e custo conforme o canal, monta o envio e o registro.

Ela tem **dois problemas**:

1. **Responsabilidades misturadas (viola SRP).** A classe faz de tudo: cálculo, formatação de texto e criação do registro. Separe cada responsabilidade em sua própria classe, cada uma com um só motivo pra mudar.

2. **`if/elif` por tipo (viola OCP).** Há um `if/elif` que decide o comportamento conforme o canal (email/sms/push). Refatore para **polimorfismo** (uma classe por tipo) ou uma estrutura equivalente, de forma que adicionar um tipo novo **não exija** mexer no código existente.

## Regras

1. Separe as responsabilidades misturadas em classes menores (SRP).
2. Troque o `if/elif` por polimorfismo ou estrutura equivalente (OCP).
3. **Mantenha o comportamento**: mesmo input, mesmo output. Rode antes e depois pra confirmar.

---

## Código original (`exercicio_5_notificacao.py`):

```python
class ServicoNotificacao:
    def notificar(self, destinatario, mensagem, canal):
        if canal == "email":
            prefixo = "[EMAIL]"
            custo = 0.01
        elif canal == "sms":
            prefixo = "[SMS]"
            custo = 0.10
        elif canal == "push":
            prefixo = "[PUSH]"
            custo = 0.0
        else:
            prefixo = "[?]"
            custo = 0
        envio = prefixo + " para " + destinatario + ": " + mensagem
        registro = {"destinatario": destinatario, "canal": canal, "custo": custo}
        return envio, registro

if __name__ == "__main__":
    s = ServicoNotificacao()
    e, r = s.notificar("ana", "Ola", "sms")
    print(e)
    print(r)
```

## Critério de "pronto"

- [ ] A classe original foi quebrada em classes menores, cada uma com uma responsabilidade
- [ ] O `if/elif` por tipo virou polimorfismo (uma classe por tipo) ou estrutura equivalente
- [ ] Adicionar um tipo novo agora não exige mexer no código que já existe (teste mentalmente: como você adicionaria um tipo a mais?)
- [ ] O resultado (o que a função/classe retorna e imprime) é **idêntico** ao original
- [ ] Você rodou antes e depois e comparou

---
