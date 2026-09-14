from unittest.mock import Mock
from recomendador import recomendar_roupa

def test_recomenda_casaco_quando_frio():
  # Arrange
  api_falsa = Mock()
  api_falsa.buscar_temperatura.return_value = 10

  # Act
  resultado = recomendar_roupa("Maceio", api_falsa)

  # Assert 
  assert resultado == "casaco"

def test_recomenda_blusa_quando_ameno():
  api_falsa = Mock()
  api_falsa.buscar_temperatura.return_value = 20
  resultado = recomendar_roupa("Maceio", api_falsa)
  assert resultado == "blusa"

def test_recomenda_camiseta_quando_quente():
  api_falsa = Mock()
  api_falsa.buscar_temperatura.return_value = 30
  resultado = recomendar_roupa("Maceio", api_falsa)
  assert resultado == "camiseta"