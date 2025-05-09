from abc import ABC, abstractmethod
from typing import Optional

from domain.entities.content import Content
from domain.entities.flow import FlowWithContent


class ContentRepository(ABC):
    @abstractmethod
    def get_last_version(content_id: str) -> Optional[Content]:
        pass

    @abstractmethod
    def add_to_flow(content: Content, flow_id: str) -> FlowWithContent:
        pass
