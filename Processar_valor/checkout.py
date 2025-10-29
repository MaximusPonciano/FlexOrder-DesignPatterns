from abc import ABC, abstractmethod

class EstrategiaFrete(ABC):
    @abstractmethod
    def calcular(self, valor_base_pedido: float):
        ...

class FreteNormal(EstrategiaFrete):
    def calcular(self, valor_base_pedido: float):
        custo_frete = valor_base_pedido * 0.05
        print(f"Frete Normal: R${custo_frete:.2f}")
        return custo_frete

class FreteExpresso(EstrategiaFrete):
    def calcular(self, valor_base_pedido: float):
        custo_frete = valor_base_pedido * 0.10 + 15.00
        print(f"Frete Expresso (com taxa): R${custo_frete:.2f}")
        return custo_frete

class FreteTeletransporte(EstrategiaFrete):
    def calcular(self):
        custo_frete = 50.00
        print(f"Frete Teletransporte: R${custo_frete:.2f}")
        return custo_frete

class Pagamento(ABC):
    @abstractmethod
    def processarValor(self, valor_final: float):
        ...

class PagamentoPix(Pagamento):
    def processarValor(self, valor_final: float):
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
        

frete = FreteExpresso()
frete.calcular(1000)

pagamento = PagamentoPix()
pagamento.processarValor(200)
