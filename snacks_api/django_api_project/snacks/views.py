from django.shortcuts import render
from .models import Snack
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import SnackSerializer




class SnackListView(ListAPIView):  # Use ListAPIView here
    queryset = Snack.objects.all()  # Remove ListCreateAPIView from this line
    serializer_class = SnackSerializer

class SnackDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer

# Create your views here.
