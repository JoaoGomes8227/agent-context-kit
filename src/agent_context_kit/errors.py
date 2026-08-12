"""Erros públicos e seguros do Kit.

Nenhuma mensagem desta camada deve carregar payload, caminho de evidência ou
credencial. O detalhe técnico fica apenas no processo local que o originou.
"""
from __future__ import annotations


class ContextKitError(Exception):
    """Erro esperado que pode ser mostrado ao operador sem conteúdo privado."""

    code = "context_kit_error"
    public_message = "O Kit não conseguiu concluir esta operação."

    def __init__(self, public_message: str | None = None) -> None:
        super().__init__(public_message or self.public_message)
        self.public_message = public_message or self.public_message


class ValidationError(ContextKitError):
    code = "validation_error"
    public_message = "Os dados enviados não obedecem ao contrato do Kit."


class NotConnectedError(ContextKitError):
    code = "not_connected"
    public_message = "Esta fonte ainda não está conectada."


class ConnectorError(ContextKitError):
    """Falha externa com código seguro para recibos e interface."""

    def __init__(self, code: str, public_message: str) -> None:
        super().__init__(public_message)
        self.code = code


class RateLimitError(ContextKitError):
    code = "rate_limited"
    public_message = "Muitas consultas em pouco tempo. Aguarde um minuto e tente de novo."


def safe_error_code(error: Exception) -> str:
    """Converte exceções internas em uma classificação sem vazar detalhes."""
    if isinstance(error, ContextKitError):
        return error.code
    return "internal_error"
