from abc import ABC, abstractmethod

# ==============================================================

class Pedido:
    def __init__(self, itens: list):
        self.itens = itens
        self.valor_base = sum(item['valor'] for item in itens)
        print(f"Pedido criado com valor base de R${self.valor_base:.2f}")

    def calcular_valor(self) -> float:
        return self.valor_base


# ==============================================================

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


# ==============================================================
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


# ==============================================================

class Embalagem:
    def __init__(self, usar_embalagem: bool):
        self.usar_embalagem = usar_embalagem
        self.taxa = 5.00 if usar_embalagem else 0.00

    def calcular_taxa(self):
        if self.usar_embalagem:
            print(f"Taxa de embalagem: R${self.taxa:.2f}")
        return self.taxa


# ==============================================================
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
