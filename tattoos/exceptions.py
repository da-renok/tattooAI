from rest_framework import status
from rest_framework.exceptions import APIException


class SketchGenerationUnavailable(APIException):
    status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    default_detail = "Sketch generation is temporarily unavailable."
    default_code = "sketch_generation_unavailable"


class SketchRequestDenied(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Please describe an idea for a tattoo."
    default_code = "sketch_request_denied"
