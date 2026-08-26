# Exercício 6 - Venda de Ingresso

## Sua tarefa

### Nome: ALAN PEDRO DIAS

Você recebeu uma classe que **funciona**, mas viola dois princípios do SOLID. Calcula o preço conforme o tipo de ingresso, monta o ticket e a venda.

Ela tem **dois problemas**:

1. **Responsabilidades misturadas (viola SRP).** A classe faz de tudo: cálculo, formatação de texto e criação do registro. Separe cada responsabilidade em sua própria classe, cada uma com um só motivo pra mudar.

2. **`if/elif` por tipo (viola OCP).** Há um `if/elif` que decide o comportamento conforme o tipo (inteira/meia/vip). Refatore para **polimorfismo** (uma classe por tipo) ou uma estrutura equivalente, de forma que adicionar um tipo novo **não exija** mexer no código existente.

## Regras

1. Separe as responsabilidades misturadas em classes menores (SRP).
2. Troque o `if/elif` por polimorfismo ou estrutura equivalente (OCP).
3. **Mantenha o comportamento**: mesmo input, mesmo output. Rode antes e depois pra confirmar.

---

## Código original (`exercicio_6_ingresso.py`):

```python
class VendaIngresso:
    def vender(self, comprador, tipo, preco_base):
        if tipo == "inteira":
            preco = preco_base
        elif tipo == "meia":
            preco = preco_base * 0.5
        elif tipo == "vip":
            preco = preco_base * 1.8
        else:
            preco = preco_base
        ticket = "Comprador: " + comprador + " | Tipo: " + tipo + " | Preco: " + str(preco)
        venda = {"comprador": comprador, "tipo": tipo, "preco": preco}
        return ticket, venda

if __name__ == "__main__":
    v = VendaIngresso()
    t, venda = v.vender("Carla", "meia", 100)
    print(t)
    print(venda)
```

## Critério de "pronto"

- [ ] A classe original foi quebrada em classes menores, cada uma com uma responsabilidade
- [ ] O `if/elif` por tipo virou polimorfismo (uma classe por tipo) ou estrutura equivalente
- [ ] Adicionar um tipo novo agora não exige mexer no código que já existe (teste mentalmente: como você adicionaria um tipo a mais?)
- [ ] O resultado (o que a função/classe retorna e imprime) é **idêntico** ao original
- [ ] Você rodou antes e depois e comparou

---
