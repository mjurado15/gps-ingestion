# Esta función Lambda es llamada por AWS cuando llega algo para validar contenido.
# Es la entrada al sistema, como una puerta que recibe visitantes.

import json
from application.use_cases.ejecutar_validacion_content import EjecutarValidacionContent

def handler(event, context):
    datos = json.loads(event["body"])
    provider = datos.get("provider", "default")

    caso = EjecutarValidacionContent(provider)

    if caso.ejecutar(datos):
        return { "statusCode": 200, "body": "Validación de contenido exitosa" }
    else:
        return { "statusCode": 400, "body": "Validación de contenido fallida" }
