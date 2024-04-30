from rest_framework import serializers

from luggage.models import Luggage


class LuggageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Luggage
        fields = [
            "is_status1",
            "is_status2",
            "is_status3",
            "is_status4",
        ]
