class FreteBase:
    def custo_base(self, peso, distancia):
        return peso * 0.5 + distancia * 0.1

    def calcular(self, peso, distancia):
        raise NotImplementedError

class FreteEconomico(FreteBase):
    def calcular(self, peso, distancia):
        return self.custo_base(peso, distancia)

class FreteExpresso(FreteBase):
    def calcular(self, peso, distancia):
        return self.custo_base(peso, distancia) * 2

class FreteSedex(FreteBase):
    def calcular(self, peso, distancia):
        return self.custo_base(peso, distancia) * 3

class FretePremium(FreteBase):
    def calcular(self, peso, distancia):
        return self.custo_base(peso, distancia) * 4

TIPOS_FRETE = {
    "economico": FreteEconomico,
    "expresso": FreteExpresso,
    "sedex": FreteSedex,
    "premium": FretePremium
}

def calcular_frete(peso, distancia, tipo):
    classe = TIPOS_FRETE.get(tipo)
    if classe is None:
        return 0
    return classe().calcular(peso, distancia)
    

if __name__ == "__main__":
    print("Economico:", calcular_frete(10, 100, "economico"))
    print("Expresso:", calcular_frete(10, 100, "expresso"))
    print("Sedex:", calcular_frete(10, 100, "sedex"))
    print("Premium:", calcular_frete(10, 100, "premium"))
