class Pedido:
    def __init__(self, itens: list):
        self.itens = itens
        self.valor_base = sum(item['valor'] for item in itens)
        print(f"Pedido criado com valor base de R${self.valor_base:.2f}")

    def calcular_valor(self) -> float:
        return self.valor_base