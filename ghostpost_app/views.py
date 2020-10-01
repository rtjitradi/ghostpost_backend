from rest_framework import viewsets

from ghostpost_app.models import BoastsRoastsModel
from ghostpost_app.serializers import BoastRoastSerializer, UpvoteSerializer, DownvoteSerializer


# Create your views here.
class BoastRoastViewSet(viewsets.ModelViewSet):
    queryset = BoastsRoastsModel.objects.all()
    serializer_class = BoastRoastSerializer
