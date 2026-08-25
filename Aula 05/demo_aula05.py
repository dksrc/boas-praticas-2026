import logging

logger = logging.getLogger("PAGAMENTO")
logger.setLevel(logging.ERROR)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(
    "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
))

logger.addHandler(handler)

TAXA_PAGAMENTO = 0.03
DESCONTO_VIP = 0.10
FRETE_PADRAO = 20
LIMITE_FRETE_GRATIS = 1000

def mascarar_cartao(numero):
    return f"**** **** **** {numero[-4:]}"

def calcular_subtotal(itens):
    return sum(item["preco"] * item["qtd"] for item in itens)

def aplicar_taxa_pagamento(valor):
    return valor + (valor * TAXA_PAGAMENTO)

def processar_pedido(pedido):
    logger.info("Iniciando processamento do pedido %s", pedido["id"])

    total = calcular_subtotal(pedido["itens"])
    logger.debug("Subtotal calculado: %s", total)

    if pedido["cliente_vip"]:
        total = total - (total * DESCONTO_VIP)
    logger.debug("Total apos desconto VIP: %s", total)

    if total > LIMITE_FRETE_GRATIS:
        frete = 0
    else:
        frete = FRETE_PADRAO
    total_com_frete = total + frete

    if pedido["forma_pagamento"] == "cartao":
        logger.info("Processando cartao %s", mascarar_cartao(pedido["num_cartao"]))
        if total_com_frete > pedido["limite_cartao"]:
            logger.error("ERRO: limite insuficiente para o cartao %s", mascarar_cartao(pedido["num_cartao"]))
            return None
        total_final = aplicar_taxa_pagamento(total_com_frete)
    elif pedido["forma_pagamento"] == "boleto":
        total_final = aplicar_taxa_pagamento(total_com_frete)
    else:
        logger.warning("Forma de pagamento desconhecida %s", pedido["forma_pagamento"])
        return None

    logger.info("Pedido %s processado. Total final: %s", pedido["id"], total_final)
    return total_final


if __name__ == "__main__":
    pedido1 = {
        "id": 101, "email": "ana@email.com", "cpf": "12345678901",
        "cliente_vip": True, "forma_pagamento": "cartao",
        "num_cartao": "1234567890123456", "limite_cartao": 5000,
        "itens": [{"preco": 500, "qtd": 2}, {"preco": 200, "qtd": 1}],
    }
    print("Resultado:", processar_pedido(pedido1))
