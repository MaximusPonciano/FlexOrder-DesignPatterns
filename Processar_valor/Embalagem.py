class Embalagem:
    def __init__(self, usar_embalagem: bool):
        self.usar_embalagem = usar_embalagem
        self.taxa = 5.00 if usar_embalagem else 0.00

    def calcular_taxa(self):
        if self.usar_embalagem:
            print(f"Taxa de embalagem: R${self.taxa:.2f}")
        return self.taxa
