# Validador de crawler personalizado para provider_x.
# Solo acepta si el origen es "noticias".

from adapters.providers.base.validador_crawler_base import ValidadorCrawlerBase

class ValidadorCrawlerProviderX(ValidadorCrawlerBase):
    def validar(self, datos: dict) -> bool:
        return super().validar(datos) and datos.get("origen") == "noticias"
