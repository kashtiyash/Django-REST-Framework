from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']

    def validate_roll(self, value):
        # Field level validation
        if value >= 100 or value <= 0:
            raise serializers.ValidationError("Roll must be between 1 and 100")
        return value

    def validate(self,data):
        # Object level validation
        name = data.get('name')
        city = data.get('city')

        if name.lower() == "Orange" and city.lower() != "Nagpur":
            raise serializers.ValidationError("Orange must be from Nagpur")
        return data
