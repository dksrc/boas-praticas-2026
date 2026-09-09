from calculadora import calcular_desconto


def test_calcular_desconto_cliente_vip():
  # Arrange
  preco = 100
  tipo = "vip"

  # Act
  resultado = calcular_desconto(preco, tipo)

  # Assert
  assert resultado == 80

def test_desconto_ouro():
  resultado = calcular_desconto(100, "ouro")
  assert resultado == 85