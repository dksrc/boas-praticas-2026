# Exercício 7 - Locação de Veículo

## Sua tarefa

### Nome: CARLOS HENRIQUE BATISTA DE ANICETO

Você recebeu uma classe que **funciona**, mas viola dois princípios do SOLID. Determina a diária conforme a categoria, calcula o total, monta contrato e registro.

Ela tem **dois problemas**:

1. **Responsabilidades misturadas (viola SRP).** A classe faz de tudo: cálculo, formatação de texto e criação do registro. Separe cada responsabilidade em sua própria classe, cada uma com um só motivo pra mudar.

2. **`if/elif` por tipo (viola OCP).** Há um `if/elif` que decide o comportamento conforme o categoria (economico/suv/luxo). Refatore para **polimorfismo** (uma classe por tipo) ou uma estrutura equivalente, de forma que adicionar um tipo novo **não exija** mexer no código existente.

## Regras

1. Separe as responsabilidades misturadas em classes menores (SRP).
2. Troque o `if/elif` por polimorfismo ou estrutura equivalente (OCP).
3. **Mantenha o comportamento**: mesmo input, mesmo output. Rode antes e depois pra confirmar.

---

## Código original (`exercicio_7_locacao.py`):

```python
class LocacaoVeiculo:
    def alugar(self, cliente, categoria, dias):
        if categoria == "economico":
            diaria = 80
        elif categoria == "suv":
            diaria = 150
        elif categoria == "luxo":
            diaria = 300
        else:
            diaria = 0
        total = diaria * dias
        contrato = "Cliente: " + cliente + " | Categoria: " + categoria + " | Dias: " + str(dias) + " | Total: " + str(total)
        registro = {"cliente": cliente, "categoria": categoria, "dias": dias, "total": total}
        return contrato, registro

if __name__ == "__main__":
    l = LocacaoVeiculo()
    c, r = l.alugar("Diego", "suv", 3)
    print(c)
    print(r)
```

## Critério de "pronto"

- [ ] A classe original foi quebrada em classes menores, cada uma com uma responsabilidade
- [ ] O `if/elif` por tipo virou polimorfismo (uma classe por tipo) ou estrutura equivalente
- [ ] Adicionar um tipo novo agora não exige mexer no código que já existe (teste mentalmente: como você adicionaria um tipo a mais?)
- [ ] O resultado (o que a função/classe retorna e imprime) é **idêntico** ao original
- [ ] Você rodou antes e depois e comparou

---
