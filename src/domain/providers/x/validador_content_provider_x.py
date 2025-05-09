# Validador personalizado para provider_x.
# Agrega una regla: solo pasa si el tipo es "video".

from domain.ports.validador_content import ValidadorContentBase

class ValidadorContentProviderX(ValidadorContentBase):
    def validar(self, datos: dict) -> bool:
        return super().validar(datos) and datos.get("tipo") == "video"
