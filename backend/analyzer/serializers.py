from rest_framework import serializers


class LogUploadSerializer(serializers.Serializer):
    file = serializers.FileField()