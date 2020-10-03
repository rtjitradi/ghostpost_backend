from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ghostpost_app.models import BoastsRoastsModel
from ghostpost_app.serializers import BoastRoastSerializer


# Create your views here.
# Worked with Sohail and Albina too on the planning/beginning stage then we finished separately
class BoastRoastViewSet(viewsets.ModelViewSet):
    queryset = BoastsRoastsModel.objects.all()
    serializer_class = BoastRoastSerializer

# https://www.django-rest-framework.org/api-guide/routers/
# action detail=True for single object / detail=False for entire collection
# https://docs.djangoproject.com/en/3.1/ref/models/querysets/
# https://www.django-rest-framework.org/api-guide/generic-views/
# https://www.django-rest-framework.org/tutorial/2-requests-and-responses/ and https://www.django-rest-framework.org/api-guide/status-codes/
    @action(detail=False)
    def boasts(self, request, pk=None):
        boasts_bydatetime = BoastsRoastsModel.objects.filter(is_boast=True).order_by('-post_datetime')
        serializer = self.get_serializer(boasts_bydatetime, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def roasts(self, request, pk=None):
        roasts_bydatetime = BoastsRoastsModel.objects.filter(is_boast=False).order_by('-post_datetime')
        serializer = self.get_serializer(roasts_bydatetime, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def upvote(self, request, pk=None):
        boast_or_roast = BoastsRoastsModel.objects.get(id=pk)
        boast_or_roast.upvotes += 1
        boast_or_roast.save()
        return Response({'status': 'looks fine'})

    @action(detail=True, methods=['post'])
    def downvote(self, request, pk=None):
        boast_or_roast = BoastsRoastsModel.objects.get(id=pk)
        boast_or_roast.downvotes -= 1
        boast_or_roast.save()
        return Response({'status': 'looks fine'})
