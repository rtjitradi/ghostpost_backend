from rest_framework import serializers
from ghostpost_app.models import BoastsRoastsModel


# https://stackoverflow.com/questions/30274591/all-fields-in-modelserializer-django-rest-framework
# https://www.django-rest-framework.org/api-guide/serializers/#specifying-which-fields-to-include
# https://www.django-rest-framework.org/api-guide/relations/
# Worked with Sohail and Albina too on the planning/beginning stage before finishing separately
class BoastRoastSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BoastsRoastsModel
        fields = '__all__'


class UpvoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BoastsRoastsModel
        fields = '__all__'


class DownvoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BoastsRoastsModel
        fields = '__all__'
