# Este archivo define la acción de validar contenido.
# Usa un validador (que puede variar según el proveedor).

from domain.ports.validador_content import ValidadorContent
from application.factory_validador import obtener_validador_content

class EjecutarValidacionContent:
    def __init__(self, provider: str):
        self.validador: ValidadorContent = obtener_validador_content(provider)

    def ejecutar(self, datos: dict) -> bool:
        return self.validador.validar(datos)
