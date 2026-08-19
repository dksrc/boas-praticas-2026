def sacar(conta, valor):
    if conta is None:
        return "Conta não encontrada"
    
    if not conta["ativa"]:
        return "Conta inativa"
    
    if valor <= 0:
        return "Valor inválido"
    
    if valor > conta["saldo"]:
        return "Saldo insuficiente"
    
    conta["saldo"] = conta["saldo"] - valor
    return f"Saque de R$ {valor:.2f} realizado. Saldo: R$ {conta['saldo']:.2f}"


if __name__ == "__main__":
    conta = {"ativa": True, "saldo": 1000.0}
    print(sacar(conta, 300))
    print(sacar(conta, 5000))
    print(sacar(None, 100))
