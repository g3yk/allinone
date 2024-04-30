from rest_framework import generics, permissions, response

from luggage.models import Luggage

from .serializers import LuggageSerializer


class LuggageView(generics.UpdateAPIView):
    queryset = Luggage.objects.all()
    serializer_class = LuggageSerializer
    lookup_field = "luggage_id"
    permission_classes = [permissions.IsAdminUser]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return response.Response({"message": "updated successfully"})
        else:
            return response.Response({"message": "failed"})
