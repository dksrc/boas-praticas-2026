# Exercício 4 - Gerenciador de Assinatura

## Sua tarefa

### Nome: ANTONIO ANDRADE GOMES JÚNIOR

Você recebeu uma classe que **funciona**, mas viola dois princípios do SOLID. Determina preço e limite conforme o plano, monta a fatura e o registro.

Ela tem **dois problemas**:

1. **Responsabilidades misturadas (viola SRP).** A classe faz de tudo: cálculo, formatação de texto e criação do registro. Separe cada responsabilidade em sua própria classe, cada uma com um só motivo pra mudar.

2. **`if/elif` por tipo (viola OCP).** Há um `if/elif` que decide o comportamento conforme o plano (basico/pro/enterprise). Refatore para **polimorfismo** (uma classe por tipo) ou uma estrutura equivalente, de forma que adicionar um tipo novo **não exija** mexer no código existente.

## Regras

1. Separe as responsabilidades misturadas em classes menores (SRP).
2. Troque o `if/elif` por polimorfismo ou estrutura equivalente (OCP).
3. **Mantenha o comportamento**: mesmo input, mesmo output. Rode antes e depois pra confirmar.

---

## Código original (`exercicio_4_assinatura.py`):

```python
class GerenciadorAssinatura:
    def assinar(self, cliente, plano):
        if plano == "basico":
            preco = 29.90
            limite = 5
        elif plano == "pro":
            preco = 59.90
            limite = 20
        elif plano == "enterprise":
            preco = 149.90
            limite = 100
        else:
            preco = 0
            limite = 0
        fatura = "Cliente: " + cliente + " | Plano: " + plano + " | Preco: " + str(preco)
        dados = {"cliente": cliente, "plano": plano, "preco": preco, "limite_usuarios": limite}
        return fatura, dados

if __name__ == "__main__":
    g = GerenciadorAssinatura()
    f, d = g.assinar("Empresa X", "pro")
    print(f)
    print(d)
```

## Critério de "pronto"

- [ ] A classe original foi quebrada em classes menores, cada uma com uma responsabilidade
- [ ] O `if/elif` por tipo virou polimorfismo (uma classe por tipo) ou estrutura equivalente
- [ ] Adicionar um tipo novo agora não exige mexer no código que já existe (teste mentalmente: como você adicionaria um tipo a mais?)
- [ ] O resultado (o que a função/classe retorna e imprime) é **idêntico** ao original
- [ ] Você rodou antes e depois e comparou

---
