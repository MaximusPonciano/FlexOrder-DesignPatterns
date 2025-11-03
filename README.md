# Exercicio_Estruturais_Comportamentais# FlexOrder-DesignPatterns

## Objetivo
Refatorar um módulo de processamento de pedidos monolítico, aplicando padrões de projeto para melhorar **acoplamento**, **coesão** e aderência aos princípios **SOLID** (em especial SRP e OCP).

## Arquitetura
O projeto demonstra três padrões principais:
- ****: implementado para métodos de pagamento (`pagamento.py`) e cálculo de frete (`frete.py`). Permite trocar comportamentos em tempo de execução sem modificar clientes.
- **Decorator**: implementado em `decorators.py` para aplicar descontos e taxas de embalagem em camadas, sem alterar a classe `Pedido`.
- **Facade**: `checkout_facade.py` provê uma interface simples `concluir_transacao(...)` que orquestra o processo inteiro (cálculo, frete, pagamento, subsistemas).

## Como os padrões resolvem as violações do código legado
- **Violação SRP (classe "deus")**: o código antigo concentrava descontos, frete, pagamento e finalização em uma única classe. Agora cada responsabilidade está em sua própria classe (Pedido, Estratégias, Decorators, Facade, Estoque, GeradorNotaFiscal).
- **Violação OCP**: antes, adicionar um novo tipo de frete/pagamento exigia editar métodos com `elif`. Agora você cria uma nova subclasse de `Frete` ou `Pagamento` sem alterar o código existente.
- **Complexidade de interação**: `finalizar_compra()` era monolítico. `checkout.somarValor()` encapsula a orquestração e fornece interface clara para o cliente.

## Como rodar
1. Clone o repositório.
2. Execute:
```bash
python main.py
