from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from opendp_apps.exec_eng.models import Run, Status, Results
from opendp_apps.exec_eng.serializers import RunSerializer, StatusSerializer, ResultsSerializer

class RunViewSet(viewsets.ModelViewSet):
    queryset = Run.objects.all()
    serializer_class = RunSerializer

class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class ResultsViewSet(viewsets.ModelViewSet):
    queryset = Results.objects.all()
    serializer_class = ResultsSerializer
