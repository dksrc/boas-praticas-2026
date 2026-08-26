# Exercício 8 - Calculadora de Envio

## Sua tarefa

### Nome: MATHEUS JOSÉ SILVA

Você recebeu uma classe que **funciona**, mas viola dois princípios do SOLID. Calcula o custo conforme a transportadora, monta a etiqueta e o registro.

Ela tem **dois problemas**:

1. **Responsabilidades misturadas (viola SRP).** A classe faz de tudo: cálculo, formatação de texto e criação do registro. Separe cada responsabilidade em sua própria classe, cada uma com um só motivo pra mudar.

2. **`if/elif` por tipo (viola OCP).** Há um `if/elif` que decide o comportamento conforme o transportadora (correios/jadlog/loggi). Refatore para **polimorfismo** (uma classe por tipo) ou uma estrutura equivalente, de forma que adicionar um tipo novo **não exija** mexer no código existente.

## Regras

1. Separe as responsabilidades misturadas em classes menores (SRP).
2. Troque o `if/elif` por polimorfismo ou estrutura equivalente (OCP).
3. **Mantenha o comportamento**: mesmo input, mesmo output. Rode antes e depois pra confirmar.

---

## Código original (`exercicio_8_envio.py`):

```python
class CalculadoraEnvio:
    def calcular(self, produto, peso, transportadora):
        if transportadora == "correios":
            custo = peso * 2.0
        elif transportadora == "jadlog":
            custo = peso * 2.5
        elif transportadora == "loggi":
            custo = peso * 3.0
        else:
            custo = 0
        etiqueta = "Produto: " + produto + " | Transportadora: " + transportadora + " | Custo: " + str(custo)
        registro = {"produto": produto, "peso": peso, "transportadora": transportadora, "custo": custo}
        return etiqueta, registro

if __name__ == "__main__":
    c = CalculadoraEnvio()
    e, r = c.calcular("Livro", 2, "jadlog")
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
