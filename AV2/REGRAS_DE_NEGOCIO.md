# Regras de Negócio - Gilded Rose

Este documento descreve **o que o sistema deve fazer**. É o comportamento que sua refatoração precisa **preservar**. Leia com atenção antes de mexer no código.

---

## O contexto

A "Gilded Rose" é uma pequena loja que vende itens. Todo item tem dois valores que mudam a cada dia:

- **`sell_in`**: o número de dias que restam para vender o item.
- **`quality`**: o quão valioso o item é.

Ao final de cada dia, o sistema roda uma atualização (o método que atualiza todos os itens), diminuindo os dois valores conforme as regras abaixo.

---

## Regras gerais (para itens normais)

1. Ao final de cada dia, `sell_in` e `quality` de cada item **diminuem em 1**.
2. Quando a data de venda passou (`sell_in < 0`), a `quality` degrada **duas vezes mais rápido** (perde 2 por dia em vez de 1).
3. A `quality` de um item **nunca é negativa** (o mínimo é 0).
4. A `quality` de um item **nunca passa de 50** (o máximo é 50).

---

## Itens especiais

Alguns itens não seguem as regras normais:

### Aged Brie (queijo envelhecido)

- **Aumenta** de qualidade com o tempo, em vez de diminuir.
- Quanto mais velho, melhor: ganha 1 de qualidade por dia.
- Depois de vencido (`sell_in < 0`), aumenta **duas vezes mais rápido** (ganha 2 por dia).
- Respeita o teto de qualidade 50.

### Sulfuras, Hand of Ragnaros (item lendário)

- **Nunca** precisa ser vendido (`sell_in` não muda).
- **Nunca** perde qualidade (`quality` não muda).
- Sua qualidade é fixa em 80 (e não respeita o limite de 50, por ser lendário).
- Em resumo: **Sulfuras nunca muda**, nem sell_in nem quality.

### Backstage passes (ingressos de show)

- Como o Aged Brie, **aumentam** de qualidade com o tempo.
- Mas o aumento acelera conforme o show se aproxima:
  - Faltando **mais de 10 dias** (`sell_in >= 11`): aumenta 1 por dia.
  - Faltando **10 dias ou menos** (`sell_in` de 6 a 10): aumenta **2** por dia.
  - Faltando **5 dias ou menos** (`sell_in` de 1 a 5): aumenta **3** por dia.
- **Depois do show** (`sell_in < 0`): a qualidade despenca para **0** (o ingresso não vale mais nada).
- Respeita o teto de qualidade 50.

---

## A feature que VOCÊS vão adicionar

### Conjured Mana Cake (item conjurado)

- Itens "Conjured" (Conjurados) degradam a qualidade **duas vezes mais rápido** que itens normais.
- Ou seja:
  - Antes de vencer: perde **2** de qualidade por dia (o normal perde 1).
  - Depois de vencido: perde **4** de qualidade por dia (o normal perde 2).
- Como todos os itens, a qualidade **nunca fica negativa**.

> **Atenção:** esta regra ainda **não existe** no código legado. Ela é a feature nova que vocês vão implementar depois de refatorar. No código atual, um item com nome "Conjured Mana Cake" seria tratado como um item normal - vocês vão mudar isso.

---

## Restrição importante

Existe uma regra que vale para **todos** os itens e que vocês **não podem violar**:

> Um item **nunca** tem a qualidade acima de 50, exceto o Sulfuras, que é fixo em 80.

E vale lembrar: **nenhum item tem qualidade negativa.**

---

## Resumo em tabela

| Item                 | sell_in    | quality antes de vencer | quality depois de vencer | Limites    |
| -------------------- | ---------- | ----------------------- | ------------------------ | ---------- |
| Normal               | -1/dia     | -1/dia                  | -2/dia                   | 0 a 50     |
| Aged Brie            | -1/dia     | +1/dia                  | +2/dia                   | 0 a 50     |
| Sulfuras             | nunca muda | nunca muda              | nunca muda               | fixo em 80 |
| Backstage            | -1/dia     | +1, +2 (≤10d), +3 (≤5d) | vira 0                   | 0 a 50     |
| **Conjurado** (novo) | -1/dia     | **-2/dia**              | **-4/dia**               | 0 a 50     |

> Use esta tabela como referência rápida, mas leia as regras completas acima, os detalhes de borda (o que acontece exatamente no dia do vencimento, nos limites de qualidade) são onde os testes mais pegam problemas.
