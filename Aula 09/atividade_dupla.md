# Atividade em Dupla - Branch, Pull Request e Code Review

> **Formato:** em dupla | **Entrega:** os dois PRs revisados e mergeados

Nesta atividade vocês vão viver o ciclo completo do trabalho em equipe: cada um trabalha na sua branch, abre um Pull Request, e **revisa o código do colega**. É o que times profissionais fazem todo dia.

---

## Visão geral do que vocês vão fazer

1. **Setup:** um de vocês cria o repositório e adiciona o outro como colaborador.
2. **Cada um** pega uma tarefa (Aluno 1 ou Aluno 2), cria sua branch e faz a tarefa.
3. **Cada um** abre um Pull Request caprichado.
4. **Vocês revisam o PR um do outro**: usando o vocabulário e feedback construtivo.
5. **Cada um** responde à revisão, ajusta o necessário, e faz o merge após aprovação.

Decidam agora quem vai ser o **dono do repositório**.

---

## PASSO 1 - Setup do repositório compartilhado

**O dono do repositório:**

1. Cria um repositório novo no GitHub (ex: `code-review-dupla`), pode ser público.
2. Vai em **Settings → Collaborators → Add people**.
3. Adiciona o colega pelo nome de usuário do GitHub.

**O colega convidado:** 4. Aceita o convite (chega por email ou nas notificações do GitHub - o ícone de sino).

**Os dois:** 5. Clonam o repositório na máquina:

```bash
git clone https://github.com/DONO/code-review-dupla.git
cd code-review-dupla
```

6. O dono adiciona o arquivo base `calculadora.py` (abaixo), commita e dá push na main:

```bash
# criar o arquivo calculadora.py com o conteúdo da próxima seção
git add calculadora.py
git commit -m "chore: adiciona calculadora base"
git push
```

7. O colega dá `git pull` pra receber o arquivo base.

---

## O código base (`calculadora.py`)

```python
def calc(a, b, op):
    if op == "soma":
        return a + b
    elif op == "sub":
        return a - b
    elif op == "mult":
        return a * b
    elif op == "div":
        return a / b


if __name__ == "__main__":
    print(calc(10, 5, "soma"))
    print(calc(10, 5, "sub"))
    print(calc(10, 5, "mult"))
    print(calc(10, 5, "div"))
```

---

## PASSO 2 - Cada um cria sua branch e faz sua tarefa

**Importante:** cada um cria a branch a partir da main atualizada.

### 🔵 Aluno 1 - Tarefa: adicionar operação de potência

Crie sua branch:

```bash
git switch -c feat-potencia
```

Adicione ao `calc` uma operação de potência (`"pot"`), que eleva `a` à potência `b`. Por exemplo, `calc(2, 3, "pot")` deve retornar 8.

Faça o commit com boa mensagem e dê push:

```bash
git add calculadora.py
git commit -m "feat: adiciona operação de potência"
git push -u origin feat-potencia
```

### 🟢 Aluno 2 - Tarefa: tratar a divisão por zero

Crie sua branch:

```bash
git switch -c fix-divisao-zero
```

O código atual **quebra** se alguém fizer `calc(10, 0, "div")` - divisão por zero. Faça a divisão tratar esse caso, retornando algo apropriado em vez de quebrar (você decide o quê - pense no que faz sentido).

Faça o commit e dê push:

```bash
git add calculadora.py
git commit -m "fix: trata divisão por zero"
git push -u origin fix-divisao-zero
```

---

## PASSO 3 - Cada um abre seu Pull Request

Cada um vai ao GitHub e abre um PR da sua branch para a `main`. Capriche, seguindo a anatomia que aprendemos:

- **Título** claro, no padrão Conventional Commits (o mesmo do commit serve).
- **Descrição:** o que mudou e por quê.
- **Como testar:** diga ao revisor como verificar. Ex: "rode `calculadora.py` e teste com `calc(2, 3, 'pot')`".

Clique em **Create pull request**.

> ✅ **Checkpoint:** os dois PRs estão abertos no repositório. Cada um consegue ver o PR do outro na aba **Pull requests**.

---

## PASSO 4 Revisem o PR um do outro

Agora troquem: **cada um revisa o PR do colega.**

1. Abra o PR do colega, vá na aba **Files changed**.
2. Leia o código com atenção. Pergunte-se:
   - Funciona? Tem algum caso que quebra?
   - Os nomes são claros?
   - Dá pra melhorar algo?
   - Tem algum problema que preciso apontar?
3. Comente em **linhas específicas** (passe o mouse na linha, clique no `+` azul).
4. **Use o vocabulário:**
   - `nit:` para detalhes pequenos (não bloqueia)
   - `sugestão:` para melhorias opcionais (não bloqueia)
   - `por curiosidade:` para perguntas genuínas (não bloqueia)
   - **sem prefixo** para problemas que precisam ser resolvidos (bloqueia)
5. **Lembre da regra de ouro:** comente o **código**, não a pessoa. Seja específico e gentil.

Faça pelo menos **2 comentários** no PR do colega. Tente incluir pelo menos um elogio ao que está bom - review também reconhece acertos!

> 💡 **Dica:** o código base tinha problemas antes de vocês mexerem (nomes como `calc`, `a`, `b`, `op`; o retorno vazio para operação inválida). Se o colega não corrigiu esses, ou se a mudança dele introduziu algo revisável, é material para comentar. Mas foquem na mudança que ele fez.

---

## PASSO 5 - Respondam à revisão e façam o merge

Cada um, no seu próprio PR:

1. **Leia** os comentários que recebeu.
2. **Responda** cada um: concorde, discuta, ou explique. (Ex: "boa, ajustei!" ou "preferi manter assim porque...").
3. Se houver comentário **bloqueante**, ajuste o código: faça a mudança, commit e push na mesma branch (o PR atualiza sozinho).
4. Quando o colega **aprovar** (ou vocês concordarem que está bom), faça o **merge** pelo botão verde **Merge pull request**.
5. Se aparecer conflito no segundo merge, resolvam juntos (Aula 8). Com estas tarefas isso normalmente não acontece, mas pode.

> ✅ **Entrega final:** os dois PRs revisados, com comentários trocados, e mergeados na main.

---

## Critério de conclusão

- [ ] Setup feito: os dois no mesmo repositório
- [ ] Cada um fez sua tarefa na sua branch
- [ ] Cada um abriu um PR com título e descrição caprichados
- [ ] Cada um fez pelo menos 2 comentários no PR do colega
- [ ] Os comentários usam o vocabulário (`nit:`, `sugestão:`, etc.) e falam do código, não da pessoa
- [ ] Cada um respondeu à revisão recebida
- [ ] Os dois PRs foram mergeados

---

## Deu erro? Dúvidas comuns

**O convite de colaborador não funcionou.**
O colega precisa **aceitar** o convite - ele chega por email ou no sino de notificações do GitHub. Sem aceitar, ele não tem acesso de escrita. Confira em Settings → Collaborators se aparece "pending" (pendente).

**Não consigo comentar numa linha específica.**
Vá na aba **Files changed** do PR (não na aba Conversation). Passe o mouse sobre a linha do código - aparece um `+` azul à esquerda. Clique nele.

**Apareceu um conflito ao mergear o segundo PR.**
Normal! Os dois mexeram no mesmo arquivo. Resolvam como na Aula 8: o GitHub tem um botão "Resolve conflicts" na tela do PR, ou vocês resolvem localmente (pull, resolver, push).

**Não sei o que comentar - o código do colega está bom.**
Sempre dá pra comentar algo: um elogio ("gostei de como você tratou o caso zero"), uma pergunta ("por curiosidade, pensou em usar X?"), ou uma sugestão pequena. Review não é só achar defeito - é conversar sobre o código.

---
