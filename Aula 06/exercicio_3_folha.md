# Exercício 3 - Folha de Pagamento

## Sua tarefa

### Nome: LARISSA LARA DA SILVA

Você recebeu uma classe que **funciona**, mas viola dois princípios do SOLID. Calcula o bônus conforme o cargo, monta o contracheque e os dados.

Ela tem **dois problemas**:

1. **Responsabilidades misturadas (viola SRP).** A classe faz de tudo: cálculo, formatação de texto e criação do registro. Separe cada responsabilidade em sua própria classe, cada uma com um só motivo pra mudar.

2. **`if/elif` por tipo (viola OCP).** Há um `if/elif` que decide o comportamento conforme o cargo (junior/pleno/senior). Refatore para **polimorfismo** (uma classe por tipo) ou uma estrutura equivalente, de forma que adicionar um tipo novo **não exija** mexer no código existente.

## Regras

1. Separe as responsabilidades misturadas em classes menores (SRP).
2. Troque o `if/elif` por polimorfismo ou estrutura equivalente (OCP).
3. **Mantenha o comportamento**: mesmo input, mesmo output. Rode antes e depois pra confirmar.

---

## Código original (`exercicio_3_folha.py`):

```python
class FolhaPagamento:
    def calcular(self, nome, salario_base, cargo):
        if cargo == "junior":
            bonus = salario_base * 0.1
        elif cargo == "pleno":
            bonus = salario_base * 0.2
        elif cargo == "senior":
            bonus = salario_base * 0.35
        else:
            bonus = 0
        total = salario_base + bonus
        contracheque = "Funcionario: " + nome + " | Base: " + str(salario_base) + " | Bonus: " + str(bonus) + " | Total: " + str(total)
        dados = {"nome": nome, "base": salario_base, "bonus": bonus, "total": total}
        return contracheque, dados

if __name__ == "__main__":
    f = FolhaPagamento()
    c, d = f.calcular("Bruno", 5000, "senior")
    print(c)
    print(d)
```

## Critério de "pronto"

- [ ] A classe original foi quebrada em classes menores, cada uma com uma responsabilidade
- [ ] O `if/elif` por tipo virou polimorfismo (uma classe por tipo) ou estrutura equivalente
- [ ] Adicionar um tipo novo agora não exige mexer no código que já existe (teste mentalmente: como você adicionaria um tipo a mais?)
- [ ] O resultado (o que a função/classe retorna e imprime) é **idêntico** ao original
- [ ] Você rodou antes e depois e comparou

---
