# Lambda para validar datos de crawler (URLs u orígenes).
# Igual que la anterior, pero con otro tipo de datos.

import json
from application.use_cases.ejecutar_validacion_crawler import EjecutarValidacionCrawler


def handler(event, context):
    datos = json.loads(event["body"])
    provider = datos.get("provider", "default")

    caso = EjecutarValidacionCrawler(provider)

    if caso.ejecutar(datos):
        return { "statusCode": 200, "body": "Validación de crawler exitosa" }
    else:
        return { "statusCode": 400, "body": "Validación de crawler fallida" }
