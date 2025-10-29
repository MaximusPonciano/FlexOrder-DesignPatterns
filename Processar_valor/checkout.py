from abc import ABC, abstractmethod

class Pedido:
    def __init__(self, itens: list):
        self.itens = itens
        self.valor_base = sum(item['valor'] for item in itens)
        print(f"Pedido criado com valor base de R${self.valor_base:.2f}")

    def calcular_valor(self) -> float:
        return self.valor_base
    
###################################################################################################################################################################################################################################################################

class Frete(ABC):
    @abstractmethod
    def calcular(self, valor_base_pedido: float):
        ...

class FreteNormal(Frete):
    def calcular(self, valor_base_pedido: float):
        custo_frete = valor_base_pedido * 0.05
        print(f"Frete Normal: R${custo_frete:.2f}")
        return custo_frete

class FreteExpresso(Frete):
    def calcular(self, valor_base_pedido: float):
        custo_frete = valor_base_pedido * 0.10 + 15.00
        print(f"Frete Expresso (com taxa): R${custo_frete:.2f}")
        return custo_frete

class FreteTeletransporte(Frete):
    def calcular(self):
        custo_frete = 50.00
        print(f"Frete Teletransporte: R${custo_frete:.2f}")
        return custo_frete
    
###################################################################################################################################################################################################################################################################

class Pagamento(ABC):
    @abstractmethod
    def processarValor(self, valor_final: float):
        ...

class PagamentoPix(Pagamento):
    def processarValor(self, valor_final: float):
        if valor_final == valor_final:
            valor_final = valor_final * 0.95

    
        print(f"Processando R${valor_final:.2f} via PIX...")
        print("    -> Pagamento com PIX APROVADO (QR Code gerado).")
        return True 

class PagamentoBoleto(Pagamento):
    def processarValor(self, valor_final: float):
        print(f"Processando R${valor_final:.2f} via Boleto...")
        print("    -> Boleto gerado com sucesso.")
        return True 

class PagamentoCredito(Pagamento):
    def processarValor(self, valor_final: float):
        print(f"Processando R${valor_final:.2f} via Credito...")
        
        if valor_final < 1000:
            print("    -> Pagamento com Credito APROVADO.")
            return True  
        else:
            print("    -> Pagamento com Credito REJEITADO (limite excedido).")
            return False 
        


###################################################################################################################################################################################################################################################################        
itens_p1 = [
    {'nome': 'Capa da Invisibilidade', 'valor': 150.0},
    {'nome': 'Poção de Voo', 'valor': 80.0}
]

pedido = Pedido(itens_p1)

pagamento = PagamentoPix()
pagamento.processarValor(pedido.valor_base)

frete = FreteExpresso()
frete.calcular(pedido.valor_base)
