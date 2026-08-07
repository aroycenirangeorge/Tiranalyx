from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from .parser import parse_log
from .serializers import LogUploadSerializer


@api_view(["GET"])
def health(request):
    return Response({
        "status": "running",
        "message": "Tiranalyx backend is working!"
    })


@api_view(["POST"])
@parser_classes([MultiPartParser, FormParser])
def upload_log(request):

    serializer = LogUploadSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(
            serializer.errors,
            status=400
        )

    uploaded_file = serializer.validated_data["file"]

    parsed_logs = parse_log(uploaded_file)

    return Response(parsed_logs)