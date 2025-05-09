import requests
from typing import Optional

from domain.repositories.flow_repository import FlowRepository
from domain.entities.flow import Flow
from domain.entities.status import Status


BASE_URL = "http://localhost:8000/api/v1/flows"


class FlowRepositoryImpl(FlowRepository):
    def get_by_id(id: str) -> Optional[Flow]:
        try:
            response = requests.get(f"{BASE_URL}/{id}")
            if not response.ok:
                if response.status_code == 404:
                    return None

                raise Exception(f"status_code={response.status_code} - {response.text}")

            flow_data = response.json()
            return Flow(
                id=flow_data["id"],
                workflow_id=flow_data["workflow_id"],
                provider_id=flow_data["provider_id"],
                status=flow_data["status"],
                detail=flow_data["detail"],
            )
        except Exception as e:
            raise Exception("Error al obtener el flow: " + str(e))

    def create(flow: Flow) -> Flow:
        try:
            response = requests.post(
                BASE_URL,
                json=flow.model_dump(exclude={"id"}),
            )
            if not response.ok:
                raise Exception(f"status_code={response.status_code} - {response.text}")

            flow_data = response.json()
            return Flow(
                id=flow_data["id"],
                workflow_id=flow_data["workflow_id"],
                provider_id=flow_data["provider_id"],
                status=flow_data["status"],
                detail=flow_data["detail"],
            )
        except Exception as e:
            raise Exception("Error al crear el flow: " + str(e))

    def update_status(flow_id: str, status: Status) -> Flow:
        try:
            response = requests.patch(
                f"{BASE_URL}/{flow_id}",
                json=status.model_dump(),
            )

            if not response.ok:
                raise Exception(f"status_code={response.status_code} - {response.text}")

            flow_data = response.json()
            return Flow(
                id=flow_data["id"],
                workflow_id=flow_data["workflow_id"],
                provider_id=flow_data["provider_id"],
                status=flow_data["status"],
                detail=flow_data["detail"],
            )
        except Exception as e:
            raise Exception("Error al actualizar el status del flow: " + str(e))
