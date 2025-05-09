from pydantic import BaseModel


class Workflow(BaseModel):
    id: str
    name: str
    description: str
    step_fn_id: (
        str  # entiendo que tiene el identificador del flujo dentro de la step function
    )
    steps: ["crawler"]
    steps: ["crawler", "metadata"]
    steps: ["content", "crawler", "trascoding"]
