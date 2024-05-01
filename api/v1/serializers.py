from rest_framework import serializers

from luggage.models import Luggage


class LuggageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Luggage
        fields = [
            "status1",
            "status2",
            "status3",
            "status4",
        ]
