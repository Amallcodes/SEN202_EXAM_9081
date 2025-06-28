from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
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