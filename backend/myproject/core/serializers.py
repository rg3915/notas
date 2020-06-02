from rest_framework import serializers
from .models import Grade


class GradeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Grade
        fields = (
            'id',
            'name',
            'grade1',
            'grade2',
        )
