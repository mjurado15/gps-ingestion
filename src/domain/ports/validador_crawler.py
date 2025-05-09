# Este archivo define un contrato para validar "crawler" (por ejemplo, URLs que se scrapean).
# Se usa igual que el de contenido, pero para otra parte del sistema.

from abc import ABC, abstractmethod

# Puertos que tienen logica de negocio base y metodos abstractos a implementar.
class ValidadorCrawler(ABC):
    @abstractmethod
    def validar(self, datos: dict) -> bool:
        pass
