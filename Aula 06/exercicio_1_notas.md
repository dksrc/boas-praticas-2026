# Exercício 1 - Sistema de Notas

## Sua tarefa

### Nome: ALEX SANDRO RODRIGUES NOBRE JUNIOR

Você recebeu uma classe que **funciona**, mas viola dois princípios do SOLID. Calcula média de um aluno, determina o conceito, formata um relatório e cria um registro.

Ela tem **dois problemas**:

1. **Responsabilidades misturadas (viola SRP).** A classe faz de tudo: cálculo, formatação de texto e criação do registro. Separe cada responsabilidade em sua própria classe, cada uma com um só motivo pra mudar.

2. **`if/elif` por tipo (viola OCP).** Há um `if/elif` que decide o comportamento conforme o conceito (A/B/C/D). Refatore para **polimorfismo** (uma classe por tipo) ou uma estrutura equivalente, de forma que adicionar um tipo novo **não exija** mexer no código existente.

## Regras

1. Separe as responsabilidades misturadas em classes menores (SRP).
2. Troque o `if/elif` por polimorfismo ou estrutura equivalente (OCP).
3. **Mantenha o comportamento**: mesmo input, mesmo output. Rode antes e depois pra confirmar.

---

## Código original (`exercicio_1_notas.py`):

```python
class SistemaNotas:
    def processar(self, aluno, notas):
        # calcula a média
        media = sum(notas) / len(notas)
        # determina o conceito (if/elif candidato a polimorfismo/tabela)
        if media >= 9:
            conceito = "A"
        elif media >= 7:
            conceito = "B"
        elif media >= 5:
            conceito = "C"
        else:
            conceito = "D"
        # formata um relatorio (responsabilidade de formatacao)
        relatorio = "Aluno: " + aluno + " | Media: " + str(media) + " | Conceito: " + conceito
        # "salva" no banco (responsabilidade de persistencia)
        registro = {"aluno": aluno, "media": media, "conceito": conceito}
        return relatorio, registro


if __name__ == "__main__":
    s = SistemaNotas()
    rel, reg = s.processar("Ana", [8, 9, 10])
    print(rel)
    print(reg)
```

## Critério de "pronto"

- [ ] A classe original foi quebrada em classes menores, cada uma com uma responsabilidade
- [ ] O `if/elif` por tipo virou polimorfismo (uma classe por tipo) ou estrutura equivalente
- [ ] Adicionar um tipo novo agora não exige mexer no código que já existe (teste mentalmente: como você adicionaria um tipo a mais?)
- [ ] O resultado (o que a função/classe retorna e imprime) é **idêntico** ao original
- [ ] Você rodou antes e depois e comparou

---
