from abc import ABC, abstractmethod
from typing import Optional, List

from domain.entities.flow import Flow
from domain.entities.step import Step
from domain.entities.status import Status


class FlowRepository(ABC):
    @abstractmethod
    def get_by_id(id: str) -> Optional[Flow]:
        pass

    @abstractmethod
    def create(flow: Flow, steps: List[Step]) -> Flow:
        pass

    @abstractmethod
    def update_status(flow_id: str, status: Status) -> Flow:
        pass
