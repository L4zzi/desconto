from dataclasses import dataclass


@dataclass
class CriarPedidoInputDTO:
    """Dados de entrada necessários para criar um pedido."""

    cliente: str
    valor_original: float
    tipo_desconto: str
