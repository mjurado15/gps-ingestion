from domain.entities.status import Status


class Step(Status):
    id: str
    flow_id: str
    name: str
