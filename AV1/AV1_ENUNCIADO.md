# AV1 Prática - Refatoração de Sistema Legado

## Treinamento de Boas Práticas para o Desenvolvimento de Software

### Avaliação dos Primeiros Dois Módulos de Boas Práticas (Aulas 2 a 6)

> **Prazo:** 08/09/2026 18h | **Entrega:** repositório ou arquivo com o código refatorado + relatório

---

## Contexto

Você foi contratado para dar manutenção no sistema de uma biblioteca. O sistema **funciona** - empresta livros, processa devoluções, calcula multas e gera relatórios. Mas foi escrito por alguém que nunca ouviu falar de boas práticas: é um único arquivo, uma única classe que faz tudo, com nomes obscuros, funções gigantes, código repetido e vários outros problemas.

Sua missão é **refatorar** esse sistema aplicando tudo que aprendemos nas Aulas 2 a 6, **sem quebrar o que já funciona**, e depois **estendê-lo** com novas funcionalidades, provando que sua refatoração deixou o código realmente flexível.

Este é o tipo de trabalho que você mais fará como desenvolvedor profissional: pegar um código que existe e melhorá-lo. É também um aquecimento para o Projeto Final.

---

## O que você recebe

O arquivo `biblioteca_legado.py`, com um sistema funcional de biblioteca. **Rode-o primeiro** e entenda o que ele faz antes de mexer. Anote a saída, ela é seu "gabarito de comportamento".

---

## Parte 1 - Refatoração (obrigatória)

O código tem problemas de **todas** as aulas do módulo. Eu vou te dizer **quais categorias** de problema existem, mas **não vou apontar as linhas**, parte da avaliação é você caçar, decidir e justificar. Encontre e corrija:

### A. Qualidade e Code Smells (Aula 2)

Há **nomes péssimos** (variáveis e atributos de uma letra, abreviações obscuras), **números mágicos** espalhados (valores soltos sem explicação) e **código duplicado**. Identifique e elimine.

### B. Nomenclatura e Funções Pequenas (Aula 3)

Há pelo menos uma **função gigante** que faz coisas demais. Aplique nomes intencionais e quebre em funções/métodos menores, cada um com uma responsabilidade clara.

### C. Aninhamento e Tratamento de Erros (Aula 4)

Há **aninhamento excessivo** (vários `if` dentro de `if`, formando "setas" para a direita). Refatore com **guard clauses** e deixe o caminho feliz no nível 0. Há também pelo menos um **`except` engolido** (`except: pass`), trate adequadamente.

> **Atenção especial:** o código legado tem um **bug** escondido, causado justamente pela ordem errada das validações no meio do aninhamento. Uma refatoração correta com guard clauses vai **corrigir** esse bug naturalmente. Encontre-o (dica: o que acontece se você tentar emprestar para um usuário que não existe?) e conserte. Documente isso no relatório.

### D. Logging e Princípios (Aula 5)

O sistema usa `print` para tudo. Substitua por **logging** com níveis apropriados. **Crítico:** há **dados sensíveis** (CPF, email) sendo impressos, isso viola a LGPD. Garanta que dados pessoais **não** apareçam nos logs (mascare, remova ou use identificadores). Aplique **DRY, KISS e YAGNI** onde couber.

### E. SOLID (Aula 6)

A classe atual viola o **SRP** (uma classe fazendo cálculo, persistência, formatação, tudo junto), separe as responsabilidades. E viola o **OCP**: adicionar um novo tipo de usuário exige mexer em `if/elif` em **vários lugares**. Refatore para que adicionar um tipo novo **não exija** tocar no código existente (provavelmente com polimorfismo).

### Regra de ouro da Parte 1

**O comportamento válido deve ser preservado.** Mesmos empréstimos, mesmas multas, mesmos relatórios. Rode antes e depois e compare. (A única mudança de comportamento aceitável, e desejável, é a correção do bug mencionado em C.)

---

## Parte 2 - Extensão (obrigatória)

Agora prove que sua refatoração valeu a pena. Implemente as **três** funcionalidades novas abaixo. Se você refatorou bem, cada uma será rápida e limpa. Se você sentir que precisa "quebrar" muita coisa para adicionar, é sinal de que a refatoração da Parte 1 não ficou boa, **volte e melhore**.

### Extensão 1 - Novo tipo de usuário: "professor" (testa seu OCP)

Adicione um tipo de usuário `professor` com estas regras: limite de **15** empréstimos, prazo de **60** dias, multa de **R$ 0/dia** (professores não pagam multa).

> Se seu OCP estiver correto, isso deve ser adicionar uma classe/estrutura nova **sem modificar** a lógica de empréstimo existente.

### Extensão 2 - Novo formato de relatório (testa seu SRP)

Além do relatório atual, crie um **relatório resumido** que mostra apenas totais (ex: "Livros: 3/5 disponíveis | Usuários: 4").

> Se você separou a formatação da lógica de negócio (SRP), isso deve ser criar um novo formatador **sem tocar** na lógica da biblioteca.

### Extensão 3 - Nova regra de negócio: reserva

Permita que um usuário **reserve** um livro que está indisponível (quantidade 0). A reserva só é aceita se o livro existir e estiver indisponível.

> Isso testa se sua estrutura ficou clara o suficiente para você saber **onde** encaixar uma regra nova.

---

## Parte 3 - Relatório (obrigatório, curto)

Escreva um relatório de **no máximo 1 página** (pode ser um `.md`) contendo:

1. **Lista dos problemas que você encontrou**, organizados pelas categorias A-E acima. Uma linha por problema (ex: "SRP: a classe `Sistema` fazia cálculo, persistência e formatação juntos").
2. **Uma frase de justificativa por categoria**, explicando sua decisão de refatoração.
3. **O bug que você encontrou e corrigiu** (o da Parte 1-C): qual era, por que acontecia, como você corrigiu.

Este relatório é o que me mostra que você **entendeu** o que fez, não apenas mexeu no código até funcionar. Capriche, é curto, mas vale.

---

## Bônus (opcionais, valem pontos extras)

- **[+] Testes de caracterização:** escreva testes simples (pode ser com `assert` ou `pytest`) que provem que o comportamento foi preservado entre o legado e o refatorado. Isso é um aquecimento direto para o Projeto Final.
- **[+] Diagrama de classes:** um diagrama simples (pode ser feito à mão e fotografado, ou em qualquer ferramenta) mostrando as classes/responsabilidades depois da refatoração.
- **[+] README do projeto:** um `README.md` explicando o que o sistema faz e como rodá-lo.

---

## Como entregar

1. O código refatorado (organizado em arquivos/módulos como você achar melhor, separar em vários arquivos é encorajado).
2. O relatório (Parte 3).
3. Os bônus, se fez algum.

Entregue via link de repositório GitHub ou arquivo zipado, na plataforma.

---

## Critérios de avaliação (resumo - rubrica completa à parte)

| Parte                                     | Peso           |
| ----------------------------------------- | -------------- |
| Parte 1 - Refatoração (as 5 categorias)   | 60%            |
| Parte 2 - Extensão (as 3 funcionalidades) | 25%            |
| Parte 3 - Relatório                       | 15%            |
| Bônus                                     | até +15% extra |

**Preservação de comportamento é pré-requisito:** uma refatoração "bonita" que quebra o funcionamento vale menos que uma modesta que preserva. Refatorar é melhorar a forma **sem** mudar o comportamento.

---

## Dicas

- **Comece rodando o legado** e salvando a saída. Ela é seu gabarito.
- **Refatore em pequenos passos**, rodando o código a cada passo. Não tente reescrever tudo de uma vez.
- **Use os conceitos com nome:** quando for justificar no relatório, use o vocabulário certo (SRP, OCP, guard clause, DRY, code smell).
- **A Parte 2 é seu termômetro:** se estender está difícil, sua refatoração da Parte 1 pode melhorar. Use isso a seu favor.
- **Não precisa ser perfeito.** Foque em aplicar bem o que aprendeu. Um trabalho honesto e bem justificado vale muito.

Bom trabalho! Este é o tipo de coisa que separa quem "faz o código funcionar" de quem "faz software de qualidade".
