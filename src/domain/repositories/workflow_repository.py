from abc import ABC, abstractmethod
from typing import Optional, Literal, List

from domain.entities.workflow import Workflow


class WorkflowRepository(ABC):
    # @abstractmethod
    # def get_one(
    #     provider_id: str,
    #     action: Literal["creation", "update"],
    #     modified_sections: List[str],
    # ) -> Optional[Workflow]:
    #     pass

    @abstractmethod
    def get_all_by_provider_id(provider_name: str) -> List[Workflow]:
        pass
