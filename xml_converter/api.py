from http import HTTPStatus
from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .serializers import XMLDataSerializer
from .utils import convert_xml_to_dict

class ConverterViewSet(ViewSet):
    # Note this is not a restful API
    # We still use DRF to assess how well you know the framework
    parser_classes = [MultiPartParser]

    @action(methods=["POST"], detail=False, url_path="convert")
    def convert(self, request, **kwargs):
        def error_response():
            """
            Error response used wherever needed
            """
            return Response(
                "The data is not valid!. Please ensure a proper XML file is submitted.",
                status=HTTPStatus.NOT_ACCEPTABLE)
        try:
            file = request.FILES['file']
        except KeyError:
            return error_response()
        serializer = XMLDataSerializer(data=request.data)
        if not file or not serializer.is_valid():
            return error_response()
        data = convert_xml_to_dict(file)
        return JsonResponse(data)
