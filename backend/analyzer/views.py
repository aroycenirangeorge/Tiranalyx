from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from .parser import parse_log

@api_view(['GET'])
def health(request):
    return Response({
        "status": "running",
        "message": "Tiranalyx backend is working!"
    })


@api_view(["POST"])
def upload_log(request):

    uploaded_file = request.FILES.get("file")

    if not uploaded_file:
        return Response(
            {"error": "No file uploaded"},
            status=400
        )

    parsed_logs = parse_log(uploaded_file)

    return Response(parsed_logs)