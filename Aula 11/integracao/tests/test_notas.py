from notas import calcular_media_turma

def test_calcular_media_de_arquivo(tmp_path):
  # Arrange
  arquivo = tmp_path / "notas.csv"
  arquivo.write_text("8.0\n6.0\n10.0\n")

  # Act
  media = calcular_media_turma(str(arquivo))

  # Assert
  assert media == 8.0

def test_arquivo_vazio_retorna_zero(tmp_path):
  arquivo = tmp_path / "notas.csv"
  arquivo.write_text("")
  media = calcular_media_turma(str(arquivo))
  assert media == 0

def test_ignora_linhas_em_branco(tmp_path):
  arquivo = tmp_path / "notas.csv"
  arquivo.write_text("7.0\n\n9.0\n\n")
  media = calcular_media_turma(str(arquivo))
  assert media == 8.0