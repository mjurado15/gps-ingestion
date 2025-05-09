import requests
from typing import Optional, List

from domain.repositories.step_repository import StepRepository
from domain.entities.step import Step
from domain.entities.status import Status


BASE_URL = "http://localhost:8000/api/v1/steps"


class StepRepositoryImpl(StepRepository):
    def get_all_by_flow_id(flow_id: str) -> List[Step]:
        try:
            response = requests.get(BASE_URL, params={"flow_id": flow_id})
            if not response.ok:
                if response.status_code == 404:
                    return []

                raise Exception(f"status_code={response.status_code} - {response.text}")

            steps_data = response.json()
            return [
                Step(
                    id=step_data["id"],
                    flow_id=step_data["flow_id"],
                    name=step_data["name"],
                    status=step_data["status"],
                    detail=step_data["detail"],
                )
                for step_data in steps_data
            ]

        except Exception as e:
            raise Exception("Error al obtener los steps: " + str(e))

    def get_by_id(id: str) -> Optional[Step]:
        try:
            response = requests.get(f"{BASE_URL}/{id}")
            if not response.ok:
                if response.status_code == 404:
                    return None

                raise Exception(f"status_code={response.status_code} - {response.text}")

            step_data = response.json()
            return Step(
                id=step_data["id"],
                flow_id=step_data["flow_id"],
                name=step_data["name"],
                status=step_data["status"],
                detail=step_data["detail"],
            )
        except Exception as e:
            raise Exception("Error al obtener el step: " + str(e))

    def create_many(steps: List[Step]) -> List[Step]:
        try:
            created_steps: List[Step] = []
            for step in steps:
                response = requests.post(BASE_URL, json=step.model_dump(exclude={"id"}))
                if not response.ok:
                    raise Exception(
                        f"STEP={step.name} - status_code={response.status_code} - {response.text}"
                    )

                step_data = response.json()
                created_steps.append(
                    Step(
                        id=step_data["id"],
                        flow_id=step_data["flow_id"],
                        name=step_data["name"],
                        status=step_data["status"],
                        detail=step_data["detail"],
                    )
                )
            return created_steps
        except Exception as e:
            raise Exception("Error al crear el step: " + str(e))

    def update_status(step_id: str, status: Status) -> Step:
        try:
            response = requests.patch(f"{BASE_URL}/{step_id}", json=status.model_dump())

            if not response.ok:
                raise Exception(f"status_code={response.status_code} - {response.text}")

            step_data = response.json()
            return Step(
                id=step_data["id"],
                flow_id=step_data["flow_id"],
                name=step_data["name"],
                status=step_data["status"],
                detail=step_data["detail"],
            )
        except Exception as e:
            raise Exception("Error al actualizar el status del step: " + str(e))
