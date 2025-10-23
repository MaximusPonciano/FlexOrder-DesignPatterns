#---------------Forma de pagamento------------#
from abc import ABC, abstractmethod

class pagamento:
    @abstractmethod
    def pagar(self, valor_final):
        pass
class pagamentoBoleto(pagamento):
    def pagar(self, valor_final):
          print(f"Pagamento{valor_final:.2f}feito no boleto")
        
    
class pagamentoPix(pagamento):
      def pagar(self, valor_final):
             print(f"Pagamento R$ {valor_final:.2f} feito no pix")

class pagamentoCartao(pagamento):
      def pagar(self, valor_final):
              print(f"Processando R${valor_final:.2f} via Cartão de Crédito...")

class pedido:
    def __init__(self, valor, metodo_pagamento: pagamento):
        self.valor = valor
        self.metodo_pagamento = metodo_pagamento

class Desconto:
    def aplicarDesconto(self, pedido: pedido):
        if isinstance(pedido.metodo_pagamento, pagamentoPix):
            desconto = pedido.valor * 0.95
            pedido.valor = desconto
            print("Aplicando 5% de desconto PIX.")

            
