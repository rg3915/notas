from rest_framework import viewsets
from .models import Grade
from .serializers import GradeSerializer


class GradeViewSet(viewsets.ModelViewSet):
    '''
    This viewset automatically provides `list` and `detail` actions.
    '''
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
