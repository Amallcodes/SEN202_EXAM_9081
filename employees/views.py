from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Manager, Intern
from .serializers import ManagerSerializer, InternSerializer

# Create your views here.

class StaffRoleList(APIView):
    def get(self, request):
        managers = Manager.objects.all()
        interns = Intern.objects.all()
        data = []

        for manager in managers:
            serializer = ManagerSerializer(manager)
            data.append(serializer.data)

        for intern in interns:
            serializer = InternSerializer(intern)
            data.append(serializer.data)

        return Response(data)

class ManagerListCreateView(generics.ListCreateAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

class ManagerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

class InternListCreateView(generics.ListCreateAPIView):
    queryset = Intern.objects.all()
    serializer_class = InternSerializer

class InternRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Intern.objects.all()
    serializer_class = InternSerializer