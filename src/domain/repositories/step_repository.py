from abc import ABC, abstractmethod
from typing import Optional, List

from domain.entities.step import Step
from domain.entities.status import Status


class StepRepository(ABC):
    # @abstractmethod
    # def get_all_by_flow_id(flow_id: str) -> List[Step]:
    #     pass

    # @abstractmethod
    # def get_by_id(id: str) -> Optional[Step]:
    #     pass

    # @abstractmethod
    # def create_many(steps: List[Step]) -> List[Step]:
    #     pass

    @abstractmethod
    def update_status(step_id: str, status: Status) -> Step:
        pass
