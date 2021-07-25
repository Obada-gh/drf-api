from django.db import models
from django.shortcuts import render
from rest_framework import generics

from .models import rtx
from .serializer import GpusSerializer
# Create your views here.

class GpusListView(generics.ListCreateAPIView):
    serializer_class = GpusSerializer
    queryset = rtx.objects.all()


class GpusDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GpusSerializer
    queryset = rtx.objects.all()


