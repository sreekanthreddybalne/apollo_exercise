from rest_framework import serializers

class XMLDataSerializer(serializers.Serializer):
    """
    Serializer for handling file submission on API endpoint
    """
    file = serializers.FileField()