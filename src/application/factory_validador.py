# Esta fábrica se encarga de decidir qué validador usar según el proveedor.
# Si viene provider_x, usamos su clase especial. Si no, usamos la base.

from domain.ports.validador_content import ValidadorContentBase
from adapters.providers.x.validador_content_provider_x import ValidadorContentProviderX
from domain.ports.validador_crawler import ValidadorCrawlerBase
from adapters.providers.x.validador_crawler_provider_x import ValidadorCrawlerProviderX

def obtener_validador_content(provider: str):
    if provider == "provider_x":
        return ValidadorContentProviderX()
    return ValidadorContentBase()

def obtener_validador_crawler(provider: str):
    if provider == "provider_x":
        return ValidadorCrawlerProviderX()
    return ValidadorCrawlerBase()
