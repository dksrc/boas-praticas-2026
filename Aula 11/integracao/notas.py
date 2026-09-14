def calcular_media_turma(caminho_arquivo):
  with open(caminho_arquivo) as f:
    linhas = f.readlines()
  notas = [float(linha.strip()) for linha in linhas if linha.strip()]
  if not notas:
    return 0
  return sum(notas) / len(notas)