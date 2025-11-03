from pedido import Pedido
from frete import FreteExpresso
from pagamento import PagamentoPix
from embalagem import Embalagem
from processar_pedido import ProcessarPedido

if __name__ == "__main__":
    print("\n========================= NOVA ARQUITETURA =========================")

    itens_p1 = [
        {'nome': 'Capa da Invisibilidade', 'valor': 150.0},
        {'nome': 'Poção de Voo', 'valor': 80.0}
    ]

    pedido = Pedido(itens_p1)
    frete = FreteExpresso()
    pagamento = PagamentoPix()
    embalagem = Embalagem(True)

    checkout = ProcessarPedido(pedido, frete, pagamento, embalagem)
    checkout.somarValor()
