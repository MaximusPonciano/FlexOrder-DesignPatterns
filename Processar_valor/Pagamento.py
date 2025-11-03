from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def processarValor(self, valor_produto: float):
        ...

class PagamentoPix(Pagamento):
    def processarValor(self, valor_produto: float):
        valor_produto *= 0.95
        print(f"Processando R${valor_produto:.2f} via PIX...")
        print("    -> Pagamento com PIX APROVADO (QR Code gerado).")
        return True 

class PagamentoBoleto(Pagamento):
    def processarValor(self, valor_produto: float):
        print(f"Processando R${valor_produto:.2f} via Boleto...")
        print("    -> Boleto gerado com sucesso.")
        return True 

class PagamentoCredito(Pagamento):
    def processarValor(self, valor_produto: float):
        print(f"Processando R${valor_produto:.2f} via Crédito...")
        if valor_produto < 1000:
            print("    -> Pagamento com Crédito APROVADO.")
            return True  
        else:
            print("    -> Pagamento com Crédito REJEITADO (limite excedido).")
            return False 

