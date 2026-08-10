from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from .parser import parse_log
from .serializers import LogUploadSerializer
from .analyzer import analyze_logs
from .ai_context import build_ai_context
from .ai_service import analyze_with_ai


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

    # Step 1: Parse raw log file
    parsed_logs = parse_log(uploaded_file)

    # Step 2: Deterministic analysis
    analysis = analyze_logs(parsed_logs)

    # Step 3: Build compact AI context
    ai_context = build_ai_context(analysis)

    # Step 4: AI reasoning
    ai_result = analyze_with_ai(ai_context)

    return Response({
        "logs": parsed_logs,
        "analysis": analysis,
        "ai_analysis": ai_result
    })