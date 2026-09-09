def calcular_desconto(preco, tipo_cliente):
  if tipo_cliente == "vip":
    return preco * 0.8
  elif tipo_cliente == "ouro":
    return preco * 0.9
  return preco