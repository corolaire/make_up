from rest_framework import serializers

class PersonSerializers(serializers.Serializer):
    name = serializers.CharField()
    last_name = serializers.CharField()