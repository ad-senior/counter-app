from api.models import Counter
from rest_framework import serializers


# This Serializer is useful when we receive any data from frontend through API.
# However, in this test task, this serializer is not needed as we don't receive
# any data from frontend.
class CounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counter
        fields = '__all__'
