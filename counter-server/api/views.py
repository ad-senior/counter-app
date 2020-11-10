from django.db.models import F
from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import Counter
from api.serializers import CounterSerializer


class CounterView(APIView):
    """
    Get and Update the count value.
    """

    def get(self, request, **kwargs):
        counter = Counter.objects.all().first()
        serializer = CounterSerializer(counter)
        response = {'value': serializer.data['count_number']}

        return Response(response)

    def post(self, request, **kwargs):
        counter = Counter.objects.first()
        counter.count_number -= 1
        counter.save()

        response = {'value': counter.count_number}

        return Response(response)


class CounterReset(APIView):
    """
    Reset the count value.
    """

    def post(self, request, **kwargs):
        counter = Counter.objects.first()
        counter.count_number = 2
        counter.save()

        response = {'value': counter.count_number}

        return Response(response)
