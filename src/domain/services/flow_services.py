from domain.repositories.workflow_repository import WorkflowRepository
from domain.repositories.flow_repository import FlowRepository
from domain.repositories.step_repository import StepRepository
from domain.entities.workflow import Workflow
from domain.entities.flow import Flow
from domain.entities.step import Step


class FlowService:
    def __init__(
        self,
        workflow_repo: WorkflowRepository,
        flow_repo: FlowRepository,
        step_repo: StepRepository,
    ):
        self.workflow_repo = workflow_repo
        self.flow_repo = flow_repo
        self.step_repo = step_repo

    def create_flow_with_steps(self, provider_id: str, workflow: Workflow, flow: Flow):
        # Podria realizarse la busqueda del workflow aqui pero depende de muchos parametros!!!
        # workflow = self.workflow_repo.get_by_provider_id(provider_id)
        # if not workflow:
        #     raise ValueError("Workflow not found")

        flow = self.flow_repo.create(
            flow=Flow(
                workflow_id=workflow.id,
                provider_id=provider_id,
                status="Pending",
                detail=None,
            )
        )
        steps = [
            Step(flow_id=flow.id, name=f"Step {i+1}", status="Pending", detail=None)
            for i in range(5)
        ]
        steps = self.step_repo.create_many(steps=steps)
        return flow, steps
