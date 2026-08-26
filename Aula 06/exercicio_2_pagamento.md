# Exercício 2 - Processador de Pagamento

## Sua tarefa

### Nome: ANTONIO CARLOS MELO XAVIER

Você recebeu uma classe que **funciona**, mas viola dois princípios do SOLID. Calcula a taxa conforme a forma de pagamento, monta o recibo e o registro.

Ela tem **dois problemas**:

1. **Responsabilidades misturadas (viola SRP).** A classe faz de tudo: cálculo, formatação de texto e criação do registro. Separe cada responsabilidade em sua própria classe, cada uma com um só motivo pra mudar.

2. **`if/elif` por tipo (viola OCP).** Há um `if/elif` que decide o comportamento conforme o forma de pagamento (pix/débito/crédito). Refatore para **polimorfismo** (uma classe por tipo) ou uma estrutura equivalente, de forma que adicionar um tipo novo **não exija** mexer no código existente.

## Regras

1. Separe as responsabilidades misturadas em classes menores (SRP).
2. Troque o `if/elif` por polimorfismo ou estrutura equivalente (OCP).
3. **Mantenha o comportamento**: mesmo input, mesmo output. Rode antes e depois pra confirmar.

---

## Código original (`exercicio_2_pagamento.py`):

```python
class ProcessadorPagamento:
    def processar(self, valor, forma):
        if forma == "pix":
            taxa = 0
        elif forma == "debito":
            taxa = valor * 0.02
        elif forma == "credito":
            taxa = valor * 0.05
        else:
            taxa = 0
        total = valor + taxa
        recibo = "Pagamento de " + str(valor) + " via " + forma + " | Taxa: " + str(taxa) + " | Total: " + str(total)
        log = {"valor": valor, "forma": forma, "taxa": taxa, "total": total}
        return recibo, log

if __name__ == "__main__":
    p = ProcessadorPagamento()
    r, l = p.processar(100, "credito")
    print(r)
    print(l)
```

## Critério de "pronto"

- [ ] A classe original foi quebrada em classes menores, cada uma com uma responsabilidade
- [ ] O `if/elif` por tipo virou polimorfismo (uma classe por tipo) ou estrutura equivalente
- [ ] Adicionar um tipo novo agora não exige mexer no código que já existe (teste mentalmente: como você adicionaria um tipo a mais?)
- [ ] O resultado (o que a função/classe retorna e imprime) é **idêntico** ao original
- [ ] Você rodou antes e depois e comparou

---
