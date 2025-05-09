import requests
from typing import Optional
from requests.exceptions import HTTPError

from domain.repositories.provider_repository import ProviderRepository
from domain.entities.provider import Provider


BASE_URL = "http://localhost:8000/api/v1/providers"


class ProviderRepositoryImpl(ProviderRepository):
    def get_by_name(provider_name: str) -> Optional[Provider]:
        try:
            response = requests.get(BASE_URL, params={"name": provider_name})
            response.raise_for_status()
            # if not response.ok:
            #     if response.status_code == 404:
            #         return None

            #     raise Exception(f"status_code={response.status_code} - {response.text}")

            data = response.json()
            provider_data = data[0]
            return Provider(
                id=provider_data["id"],
                description=provider_data["description"],
                is_active=provider_data["status"],
            )
        # except HTTPError as e:
        #     HTTPError.
        except Exception as e:
            raise Exception("Error al obtener el proveedor: " + str(e))
