from rest_framework import serializers

class Persona:
    NOMBRE = "Isaias"
    
    def __int__(self):
        Persona.NOMBRE = "Isaias"
        self.nombre = "ISaiass"


class PersonSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=6,error_messages={"name":"Este campo supera la longitud permitida"})
    last_name = serializers.CharField(max_length=8,error_messages={"last_name":"Este campo supera la longitud permitida"})
    
    def validate_name(self,validate_data):
        ...