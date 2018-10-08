from rest_framework import serializers

from app.models import Pet


class PetSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Pet
        fields = '__all__'
