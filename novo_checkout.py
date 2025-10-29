from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def processarValor(self, valor_final: float) -> bool:
        ...

class PagamentoPix(Pagamento):
    def processarValor(self, valor_final: float) -> bool:
        print(f"Processando R${valor_final:.2f} via PIX...")
        print("    -> Pagamento com PIX APROVADO (QR Code gerado).")
        return True 

class PagamentoBoleto(Pagamento):
    def processarValor(self, valor_final: float) -> bool:
        print(f"Processando R${valor_final:.2f} via Boleto...")
        print("    -> Boleto gerado com sucesso.")
        return True 

class PagamentoCredito(Pagamento):
    def processarValor(self, valor_final: float) -> bool:
        print(f"Processando R${valor_final:.2f} via Credito...")
        
        if valor_final < 1000:
            print("    -> Pagamento com Credito APROVADO.")
            return True  
        else:
            print("    -> Pagamento com Credito REJEITADO (limite excedido).")
            return False 


pagamento_credito = PagamentoCredito()
    

pagamento_credito.processarValor(10000)
 
