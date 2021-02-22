import csv
import io
import threading
import requests
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .serializers import GeoCodeSerializer


class GeoCodeAPIView(APIView):
    serializer_class = GeoCodeSerializer
    permission_classes = (AllowAny,)

    def request_handler(self, payload, row, w):
        resp = requests.get(url=settings.MAP_QUEST_API_URL, params=payload)
        if resp.status_code == 200:
            row.update(resp.json().get('results')[0].get('locations')[0].get('latLng'))
        w.writerow(row)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        decoded_file = file.read().decode()
        io_string = io.StringIO(decoded_file)
        reader = csv.DictReader(io_string)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="export.csv"'
        w = csv.DictWriter(response, fieldnames=["Address", "lat", "lng"])
        w.writeheader()

        for row in reader:
            payload = {
                "key": settings.MAP_QUEST_API_KEY,
                "inFormat": "json",
                "outFormat": "json",
                "location": row.get('Address'),
                "maxResults": "1"
            }
            t1 = threading.Thread(target=self.request_handler, args=(payload, row, w))
            t1.start()
            t1.join()

        return response
