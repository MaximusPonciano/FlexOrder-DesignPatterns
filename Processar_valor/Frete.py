from abc import ABC, abstractmethod

class Frete(ABC):
    @abstractmethod
    def calcular(self, valor_base_pedido: float):
        ...

class FreteNormal(Frete):
    def calcular(self, valor_base_pedido: float):
        custo = valor_base_pedido * 0.05
        print(f"Frete Normal: R${custo:.2f}")
        return custo

class FreteExpresso(Frete):
    def calcular(self, valor_base_pedido: float):
        custo = valor_base_pedido * 0.10 + 15.00
        print(f"Frete Expresso (com taxa): R${custo:.2f}")
        return custo

class FreteTeletransporte(Frete):
    def calcular(self, valor_base_pedido: float):
        custo = 50.00
        print(f"Frete Teletransporte: R${custo:.2f}")
        return custo