from .pedido import Pedido
from .frete import Frete
from .pagamento import Pagamento
from .embalagem import Embalagem

class ProcessarPedido:
    def __init__(self, pedido: Pedido, frete: Frete, pagamento: Pagamento, embalagem: Embalagem):
        self.pedido = pedido
        self.frete = frete
        self.pagamento = pagamento
        self.embalagem = embalagem

    def somarValor(self):
        valor_base = self.pedido.calcular_valor()
        valor_frete = self.frete.calcular(valor_base)
        valor_embalagem = self.embalagem.calcular_taxa()
        total = valor_base + valor_frete + valor_embalagem

        print(f"\nValor total com frete e embalagem: R${total:.2f}")
        self.pagamento.processarValor(total)