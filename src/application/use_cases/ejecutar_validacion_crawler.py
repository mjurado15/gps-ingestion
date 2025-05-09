# Este archivo define la acción de validar crawler.
# Se usa para validar URLs u orígenes de datos automáticos.

from domain.ports.validador_crawler import ValidadorCrawler
from application.factory_validador import obtener_validador_crawler

class EjecutarValidacionCrawler:
    def __init__(self, provider: str):
        self.validador: ValidadorCrawler = obtener_validador_crawler(provider)

    def ejecutar(self, datos: dict) -> bool:
        return self.validador.validar(datos)
