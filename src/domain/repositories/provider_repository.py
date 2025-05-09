from abc import ABC, abstractmethod
from typing import Optional

from domain.entities.provider import Provider


class ProviderRepository(ABC):
    @abstractmethod
    def get_by_name(provider_name: str) -> Optional[Provider]:
        pass
