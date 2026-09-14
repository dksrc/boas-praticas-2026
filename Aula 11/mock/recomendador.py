def recomendar_roupa(cidade, cliente_api):
  temp = cliente_api.buscar_temperatura(cidade)
  if temp < 15:
    return "casaco"
  elif temp < 25:
    return "blusa"
  else:
    return "camiseta"