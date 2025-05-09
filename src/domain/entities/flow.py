from domain.entities.status import Status


class Flow(Status):
    id: str
    workflow_id: str
    provider_name: str


class FlowWithContent(Flow):
    content_id: str
    content: dict[str, any]
