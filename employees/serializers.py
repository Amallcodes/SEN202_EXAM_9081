from rest_framework import serializers
from .models import Manager, Intern

class ManagerSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField(read_only=True)
    has_company_card = serializers.BooleanField(read_only=True)

    class Meta:
        model = Manager
        fields = ['id', 'first_name', 'last_name', 'email', 'date_joined', 'department', 'has_company_card', 'role']

    def get_role(self, obj):
        return obj.get_role()

class InternSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField(read_only=True)
    mentor = serializers.StringRelatedField()

    class Meta:
        model = Intern
        fields = ['id', 'first_name', 'last_name', 'email', 'date_joined', 'mentor', 'internship_end', 'role']

    def get_role(self, obj):
        return obj.get_role()