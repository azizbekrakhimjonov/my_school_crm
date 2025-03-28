from django.shortcuts import render

from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.status import *

from .models import Subject
from .serializers import SubjectSerializer

class SubjectList(APIView):
    def get(self, request):
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data, status=HTTP_200_OK)