import requests
from typing import Optional

from domain.repositories.content_repository import ContentRepository
from domain.entities.content import Content
from domain.entities.flow import FlowWithContent

BASE_URL = "http://localhost:8000/api/v1/content"


class ContentRepositoryImpl(ContentRepository):
    def get_last_version(id: str) -> Optional[Content]:
        try:
            response = requests.get(f"{BASE_URL}/{id}/last_version")
            if not response.ok:
                if response.status_code == 404:
                    return None

                raise Exception(f"status_code={response.status_code} - {response.text}")

            content_data = response.json()
            return Content(
                id=content_data["id"],
                title=content_data["title"],
                description=content_data["description"],
                metadata=content_data["metadata"],
            )
        except Exception as e:
            raise Exception(
                "Error al obtener la última versión del contenido: " + str(e)
            )

    def add_to_flow(content: Content, flow_id: str) -> Content:
        try:
            response = requests.post(
                f"{BASE_URL}/{flow_id}/add_content", json=content.to_dict()
            )
            if not response.ok:
                raise Exception(f"status_code={response.status_code} - {response.text}")

            flow_data = response.json()
            return FlowWithContent(
                id=flow_data["id"],
                workflow_id=flow_data["workflow_id"],
                provider_id=flow_data["provider_id"],
                content=flow_data["content"],
                status=flow_data["status"],
                detail=flow_data["detail"],
            )
        except Exception as e:
            raise Exception("Error al agregar contenido al flow: " + str(e))
