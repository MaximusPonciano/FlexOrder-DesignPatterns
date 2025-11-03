from Processar_valor.pedido import Pedido
from Processar_valor.frete import FreteExpresso
from Processar_valor.pagamento import PagamentoPix
from Processar_valor.embalagem import Embalagem
from Processar_valor.processar_pedido import ProcessarPedido

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
