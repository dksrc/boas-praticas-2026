# Projeto Final - Refatoração do Gilded Rose

## Treinamento de Boas Práticas para o Desenvolvimento de Software

### Avaliação Integradora, Todos os Módulos

> **Prazo:** 21/09/2026 - 18h | **Formato:** em dupla | **Peso:** projeto final do curso
> **Entrega:** repositório no GitHub com todo o processo (código, histórico, PRs, testes, documentação)

---

## Visão geral

Vocês receberam o **Gilded Rose**, um sistema de gerenciamento de inventário de uma loja, escrito da pior forma possível. Ele **funciona**, mas é um pesadelo: uma função gigante, aninhamento profundo, nomes indecifráveis, números mágicos, duplicação, e complexidade ciclomática altíssima. É o retrato de tudo que este curso ensinou vocês a combater.

A missão de vocês: **transformar esse código em algo de qualidade profissional**, aplicando **tudo** que aprenderam, do primeiro ao último módulo, e usando o processo de trabalho em equipe (branches, Pull Requests, revisão cruzada) que times reais usam.

Este projeto cobra **todos os módulos do curso**:

- **Módulos 1 e 2:** qualidade, code smells, clean code, nomenclatura, funções pequenas, guard clauses, SOLID.
- **Módulo 3:** Git com branches, commits convencionais, Pull Requests e code review entre vocês.
- **Módulo 4:** testes automatizados com boa cobertura, e documentação.

---

## O que vocês recebem

- `gilded_rose.py`, o código legado.
- `REGRAS_DE_NEGOCIO.md`, as regras que o sistema deve seguir (o comportamento a preservar).

> **Primeiro passo, antes de tudo:** rodem o código, leiam as regras de negócio, e **entendam o que ele faz** antes de mexer. Vocês não podem preservar um comportamento que não entenderam.

---

## As três frentes do trabalho

### Frente 1 - Refatoração (Módulos 1 e 2)

Transformem o `gilded_rose.py` em código limpo, aplicando o que aprenderam. O código tem problemas de **todas** as aulas de código:

- **Code smells e nomes ruins** (Aulas 2-3): `att`, `x`, nomes de itens repetidos como strings mágicas. Renomeiem tudo, eliminem números e strings mágicas.
- **Função gigante** (Aula 3): o método `att` faz tudo. Quebrem em funções/métodos pequenos e coesos.
- **Aninhamento profundo e guard clauses** (Aula 4): há `if` dentro de `if` dentro de `if`. Achatem com guard clauses, caminho feliz no nível 0.
- **DRY, KISS** (Aula 5): há lógica duplicada. Centralizem.
- **SOLID** (Aula 6): a lógica de cada tipo de item está toda misturada. Separem as responsabilidades (SRP) e estruturem para que adicionar um tipo novo **não** exija mexer no código existente (OCP).

O comportamento deve ser **preservado**. O sistema refatorado tem que fazer exatamente o que o original faz. Vocês vão provar isso com testes.

### Frente 2 - Feature nova: item "Conjurado" (Módulos 1, 2 e a prova do OCP)

Depois de refatorar, adicionem um novo tipo de item: **"Conjured Mana Cake"** (Conjurado). Regra dele:

> Itens Conjurados degradam a qualidade **duas vezes mais rápido** que itens normais.

Ou seja: um item normal perde 1 de qualidade por dia (2 depois de vencido); um Conjurado perde 2 por dia (4 depois de vencido). Como todo item, a qualidade nunca fica negativa.

> **Esta feature é o teste da sua refatoração.** Se vocês aplicaram bem o OCP na Frente 1, adicionar o Conjurado será rápido e limpo, uma classe nova, sem tocar no resto. Se estiver difícil, com você tendo que mexer em vários lugares, é sinal de que a refatoração pode melhorar. Usem isso como termômetro.

### Frente 3 - Testes e Documentação (Módulo 4)

- **Testes:** escrevam uma suíte de testes com `pytest` que cubra o comportamento de **todos** os tipos de item (normal, Aged Brie, Sulfuras, Backstage, e o Conjurado novo). Incluam casos de borda (limites de qualidade 0 e 50, vencimento). Meçam a **cobertura** e busquem uma cobertura alta e significativa (lembrem: cobertura alta com testes bons, não testes vazios).
  - **Dica:** escrevam **testes de caracterização** ANTES de refatorar, testes que capturam o comportamento do legado. Aí, conforme refatoram, rodam os testes e sabem na hora se preservaram o comportamento. É a rede de segurança da refatoração.
- **Documentação:** um `README.md` explicando o que o sistema faz, como rodar, e como rodar os testes. E docstrings nas classes/funções principais.

---

## O processo é parte da entrega (Módulo 3)

Este é o ponto que diferencia o projeto final: **não basta entregar código bom, vocês têm que trabalhar como um time de verdade.** O histórico do Git será avaliado.

Regras obrigatórias de processo:

1. **Trabalhem em branches.** Nada de commitar direto na `main`. Cada tarefa (refatorar um tipo de item, adicionar o Conjurado, escrever testes) vive em sua branch.

2. **Commits atômicos e convencionais.** Um commit por mudança lógica, com mensagens no padrão Conventional Commits (`feat:`, `fix:`, `refactor:`, `test:`, `docs:`). O histórico deve contar a história do trabalho.

3. **Integrem via Pull Requests.** Toda branch entra na `main` por um PR, nunca por merge direto.

4. **Revisão cruzada obrigatória.** Cada PR deve ser **revisado pelo outro membro da dupla** antes do merge. Usem o vocabulário do review (`nit:`, `sugestão:`, bloqueante), comentem em linhas específicas, e deem feedback construtivo (código, não pessoa). O merge só acontece depois da revisão do colega.

5. **Setup:** um de vocês cria o repositório e adiciona o outro como colaborador (Settings → Collaborators). Assim os dois trabalham no mesmo repositório e revisam os PRs um do outro.

> A ideia: quando eu olhar o repositório de vocês, o histórico deve mostrar duas pessoas trabalhando em branches, abrindo PRs, revisando o código um do outro, e integrando com cuidado. Exatamente como um time profissional.

---

## Divisão sugerida do trabalho

Vocês se organizam como quiserem, mas aqui vai uma sugestão de ritmo:

- **Dias 1-2:** os dois entendem o legado juntos, leem as regras, e escrevem **testes de caracterização** do comportamento atual. (Ótima primeira dupla de PRs.)
- **Dias 3-5:** refatoração, dividida entre vocês por tipo de item ou por frente. Cada um em suas branches, revisando os PRs do outro.
- **Dia 6:** adicionar a feature Conjurado (com testes) e completar a cobertura de testes.
- **Dia 7:** documentação (README + docstrings) e revisão geral.
- **Dia 8:** revisão final, garantir que tudo está mergeado, testes passando, e preparar a apresentação.

> **Trabalhem em paralelo de verdade.** A graça da dupla é os dois contribuírem. Um repositório onde só uma pessoa commitou não cumpre o Módulo 3, mesmo que o código seja bom.

---

## Como entregar

O link do repositório no GitHub, contendo:

1. O código refatorado (organizado como acharem melhor).
2. A feature Conjurado implementada e testada.
3. A suíte de testes (`pytest` passando).
4. O `README.md` e as docstrings.
5. O histórico completo: branches, commits convencionais, PRs revisados por ambos.

---

## Critérios de avaliação

| Frente                    | O que se avalia                                                   | Peso |
| ------------------------- | ----------------------------------------------------------------- | ---- |
| Refatoração (M1-M2)       | Code smells, nomes, funções pequenas, guard clauses, SOLID        | 30%  |
| Feature Conjurado (M1-M2) | Implementada, correta, encaixada de forma limpa                   | 10%  |
| Testes (M4)               | Cobertura significativa, casos de borda, comportamento preservado | 20%  |
| Documentação (M4)         | README claro + docstrings                                         | 10%  |
| Processo Git (M3)         | Branches, commits convencionais, PRs, **revisão cruzada**         | 25%  |
| Apresentação              | Clareza ao explicar as decisões                                   | 5%   |

**Preservação de comportamento é pré-requisito:** uma refatoração linda que quebra o funcionamento vale menos que uma modesta que preserva.

---

## Dicas finais

- **Testes de caracterização primeiro.** É o maior truque da refatoração de legado: capture o comportamento em testes ANTES de mexer, e refatore com a rede de segurança rodando.
- **Refatorem em pequenos passos**, rodando os testes a cada passo. Não reescrevam tudo de uma vez.
- **A feature Conjurado é seu termômetro de OCP.** Difícil de adicionar = refatoração incompleta.
- **Dividam o trabalho e revisem de verdade.** O code review entre vocês não é formalidade, é onde vocês pegam problemas um do outro e aprendem juntos.
- **Usem o vocabulário certo** ao justificar (no PR, no README, na apresentação): SRP, OCP, guard clause, code smell, cobertura. Mostra domínio.

Este projeto é o retrato de tudo que vocês aprenderam. Caprichem, é o trabalho que fecha o curso e o que vocês vão poder mostrar como portfólio.
