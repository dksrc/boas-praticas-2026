# Atividade - Teste de Integração e Pipeline de CI

Nesta atividade você vai aplicar as duas frentes práticas do dia: escrever um **teste de integração** e configurar um **pipeline de CI** que roda seus testes automaticamente.

---

## PARTE 1 - Teste de integração

### A função a testar

Crie um arquivo `processador.py` com esta função:

```python
def contar_linhas_validas(caminho_arquivo):
    """Lê um arquivo e conta quantas linhas não estão vazias."""
    with open(caminho_arquivo) as f:
        linhas = f.readlines()
    return sum(1 for linha in linhas if linha.strip())
```

Ela abre um arquivo, lê as linhas, e conta quantas **não** estão vazias.

### Sua tarefa

Escreva testes de integração para ela usando o `tmp_path` do pytest (como na demonstração). Crie `test_processador.py` com testes que cubram:

1. **Caso normal:** um arquivo com algumas linhas preenchidas → conta certo.
2. **Linhas vazias no meio:** um arquivo com linhas em branco entre as preenchidas → ignora as vazias.
3. **Arquivo vazio:** um arquivo sem nada → retorna 0.

Lembre da receita do teste de integração:

```python
def test_algo(tmp_path):
    arquivo = tmp_path / "dados.txt"      # define um arquivo na pasta temporária
    arquivo.write_text("...conteúdo...")  # escreve de verdade
    resultado = contar_linhas_validas(str(arquivo))  # a função lê o arquivo real
    assert resultado == ...               # verifica
```

### Rode

```bash
pytest -v
```

Todos verdes? Ótimo. Confira também a cobertura:

```bash
pytest --cov=processador --cov-report=term-missing
```

---

## PARTE 2 - Pipeline de CI

Agora você vai fazer seus testes rodarem **automaticamente** a cada push, no GitHub Actions.

> **Pré-requisito:** você precisa de um repositório no GitHub com seu código e seus testes já lá. Pode usar o repositório do seu projeto, ou criar um pequeno só pra praticar.

### Passo 1 - Criar a estrutura de pastas

No seu repositório, crie a pasta e o arquivo do workflow:

```
.github/
└── workflows/
    └── testes.yml
```

### Passo 2 - Escrever o workflow

Coloque isto no `testes.yml`:

```yaml
name: Testes

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  testar:
    runs-on: ubuntu-latest
    steps:
      - name: Baixar o código
        uses: actions/checkout@v4

      - name: Configurar Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Instalar dependências
        run: pip install -r requirements.txt

      - name: Rodar a suíte de testes
        run: pytest -v
```

> ⚠️ **Atenção à indentação!** YAML é como Python: a indentação importa e tem que ser com espaços (não tab). Um espaço a mais ou a menos quebra o arquivo.

### Passo 3 - Criar o requirements.txt

O workflow roda `pip install -r requirements.txt`, então esse arquivo precisa existir na raiz do repositório, listando o que seu projeto precisa:

```
pytest
pytest-cov
```

### Passo 4 - Subir e ver funcionar

Faça commit e push dos novos arquivos:

```bash
git add .github/workflows/testes.yml requirements.txt
git commit -m "ci: adiciona pipeline de testes"
git push
```

Vá no seu repositório no GitHub, aba **Actions**. Você verá o pipeline rodando (bolinha amarela), e em segundos ele fica **verde** (passou) ou **vermelho** (falhou).

---

## Critério de conclusão

- [ ] Parte 1: `test_processador.py` com pelo menos 3 testes de integração usando `tmp_path`
- [ ] Todos os testes passam (`pytest -v` verde)
- [ ] Parte 2: arquivo `.github/workflows/testes.yml` criado
- [ ] `requirements.txt` criado
- [ ] O pipeline aparece na aba Actions e fica **verde**

---

## Deu erro? Dúvidas comuns

**"O tmp_path não funciona / dá erro"**
Confirme que você colocou `tmp_path` como **parâmetro** da função de teste: `def test_algo(tmp_path):`. O pytest injeta ele automaticamente - você não cria, só recebe.

**"O pipeline ficou vermelho no passo de instalar dependências"**
Provavelmente falta o `requirements.txt` na raiz, ou ele está vazio. O workflow roda `pip install -r requirements.txt` - esse arquivo tem que existir com as dependências.

**"O YAML deu erro de sintaxe"**
Quase sempre é indentação. YAML usa espaços (não tab), e a indentação tem que ser consistente. Cada nível são 2 espaços. Copie o modelo com cuidado.

**"O pipeline não apareceu na aba Actions"**
Confirme que o arquivo está exatamente em `.github/workflows/testes.yml` (com o ponto no começo de `.github`) e que você deu push. O GitHub só reconhece workflows nesse caminho.

**"Os testes passam na minha máquina mas o CI falha"**
Esse é o ponto da aula! Provavelmente uma dependência que você tem instalada localmente mas não está no `requirements.txt`. O CI roda num ambiente limpo - tudo que ele precisa tem que estar declarado.

---
