# Este archivo define un contrato para validar "contenido".
# Es como decir: "Si vas a validar contenido, tenés que hacer esto".

from abc import ABC, abstractmethod

# Puertos que tienen logica de negocio base y metodos abstractos a implementar.
class ValidadorContent(ABC):
    @abstractmethod
    def validar(self, datos: dict) -> bool:
        pass
