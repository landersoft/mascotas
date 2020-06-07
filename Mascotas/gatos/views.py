from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import GatoSerializer
from .models import Gato
from django.contrib.auth.decorators import login_required
# Create your views here.


class GatoViewSet(viewsets.ModelViewSet):
    queryset = Gato.objects.all().order_by('nombre')
    serializer_class = GatoSerializer


@login_required
def add(request):
    return render(request, 'index.html')
